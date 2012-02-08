from django import template
from django.core.cache import cache

register = template.Library()

class CacheStats(template.Node):
    """
    Reads the cache stats out of the redis cache backend. Returns `None`
    if no cache stats supported.
    """
    def render(self, context):
        try:
            cache_stats = cache._client.info()

            #count database keys
            #thank you http://stackoverflow.com/a/4559015
            databases = dict(filter(lambda item: item[0].startswith('db'),cache_stats.iteritems()))

            cache_stats['total_keys'] = sum([vals['keys'] for db, vals in databases.items()])
            cache_stats['server'] = cache._server

        # The current cache backend does not provide any statistics
        except AttributeError:
            cache_stats = None
        context['cache_stats'] = cache_stats
        return ''

@register.tag
def get_cache_stats(parser, token):
    return CacheStats()

@register.filter
def prettyname(name):
    return ' '.join([word.capitalize() for word in name.split('_')])

@register.filter
def prettyvalue(value, key):
    return PrettyValue().format(key, value)

class PrettyValue(object):
    """
    Helper class that reformats the value. Looks for a method named
    ``format_<key>_value`` and returns that value. Returns the value
    as is, if no format method is found.
    """

    def format(self, key, value):
        try:
            func = getattr(self, 'format_%s_value' % key.lower())
            return func(value)
        except AttributeError:
            return value

    def format_used_memory_value(self, value):
        return "%s (%s)" % (value, self.human_bytes(value))

    def format_used_memory_peak_value(self, value):
        return "%s (%s)" % (value, self.human_bytes(value))

    def format_used_memory_rss_value(self, value):
        return "%s (%s)" % (value, self.human_bytes(value))

    def format_uptime_in_seconds_value(self, value):
        return "%s (%s)" % (value, self.fract_timestamp(int(value)))

    def format_last_save_time_value(self, value):
        from datetime import datetime
        return datetime.fromtimestamp(int(value)).strftime('%x %X')

    def fract_timestamp(self, s):
        years, s = divmod(s, 31556952)
        min, s = divmod(s, 60)
        h, min = divmod(min, 60)
        d, h = divmod(h, 24)
        return '%sy, %sd, %sh, %sm, %ss' % (years, d, h, min, s)

    def human_bytes(self, bytes):
        bytes = float(bytes)
        if bytes >= 1073741824:
            gigabytes = bytes / 1073741824
            size = '%.2fGB' % gigabytes
        elif bytes >= 1048576:
            megabytes = bytes / 1048576
            size = '%.2fMB' % megabytes
        elif bytes >= 1024:
            kilobytes = bytes / 1024
            size = '%.2fKB' % kilobytes
        else:
            size = '%.2fB' % bytes
        return size