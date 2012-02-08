#Overview
This app is a clone of [django-memcache-status](https://github.com/bartTC/django-memcache-status) modified to work with Redis. This app displays some statistics for your redis instance in the index view of your Django admin section.


#Notes
This app requires a redis cache backend. I recommend [django-redis-cache](https://github.com/sebleier/django-redis-cache).

#Usage
Add redis_status to your installed apps.