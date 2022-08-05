#!/bin/bash

cd /root/aircraft-vue-django/

# start uwsgi
/usr/local/bin/uwsgi --ini uwsgi.ini
/usr/local/bin/uwsgi --reload /tmp/aircraft-vue-django.pid

# generate static files
python manage.py collectstatic

# start nginx
mv -b /root/aircraft-vue-django/config/nginx.conf /root/nginx-1.22.0/conf/nginx.conf
/root/nginx-1.22.0/sbin/nginx