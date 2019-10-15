try:
    from django.conf.urls import include, url
except ImportError:
    from django.conf.urls.defaults import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]
