#!/bin/bash
sh ./install.sh
/root/bin/uwsgi --ini wsgi.ini
/root/bin/uwsgi --reload /tmp/aircraft-vue-django.pid
mv -b /root/aircraft-vue-django/config/nginx.conf /root/nginx-1.9.9/conf/nginx.conf
/root/nginx-1.9.9/sbin/nginx