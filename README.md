[![Build Status](https://travis-ci.org/nicholasserra/django-redis-status.svg?branch=master)](https://travis-ci.org/nicholasserra/django-redis-status)

# Overview
This app is a clone of [django-memcache-status](https://github.com/bartTC/django-memcache-status) modified to work with Redis. This app displays some statistics for your redis instance in the index view of your Django admin section.


# Notes
This app requires a redis cache backend. I recommend [django-redis-cache](https://github.com/sebleier/django-redis-cache).

# Installation
`django-redis-status` can be installed via pip.

```
pip install django-redis-status
```

# Usage
Add `redis_status` to your `INSTALLED_APPS`.
