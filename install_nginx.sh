#!/bin/bash
if [ -d "/root/nginx-1.9.9" ]; then
    exit 0
else
    cd /tmp
    wget http://nginx.org/download/nginx-1.9.9.tar.gz 
    tar xzvf nginx-1.9.9.tar.gz 
fi
cd nginx-1.9.9

# 配置（指定安装目录）
./configure --prefix=/root/nginx-1.9.9 --with-http_stub_status_module --with-http_gzip_static_module
make && make install

# 检查是否成功
/root/nginx-1.9.9/sbin/nginx -V
