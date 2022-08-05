#!/bin/bash
if [ -d "/root/nginx-1.22.0" ]; then
    exit 0
else
    cd /tmp
    wget http://nginx.org/download/nginx-1.22.0.tar.gz
    tar xzvf nginx-1.22.0.tar.gz
fi
cd nginx-1.22.0

# 配置（指定安装目录）
./configure --prefix=/root/nginx-1.22.0 --with-http_stub_status_module --with-http_gzip_static_module --with-http_ssl_module
make && make install

# 检查是否成功
/root/nginx-1.22.0/sbin/nginx -V
