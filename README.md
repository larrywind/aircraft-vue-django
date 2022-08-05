# aircraft-vue-django

## 简介

本项目采用vue3+django，实现了一套简单的飞机大战游戏，渲染使用pixijs

## 获取代码
由于启用了lfs存储，故需要先安装git和git-lfs
```
yum install git git-lfs -y
git clone https://github.com/larrywind/aircraft-vue-django.git
```

## 构建项目

需要以下组件：
```
Node: 12.16.3
npm: 6.14.4
python3: 3.7
mariadb: 10.5.6
```
安装mariadb等依赖
```
yum install gcc libffi-devel python3-devel openssl-devel mysql-devel pcre-devel -y
yum --allowerasing install mariadb-server mariadb -y
systemctl start mariadb
```
在文件夹`./aircraft-vue-django`下运行`pre_install.sh`部署npm和node环境

```
bash pre_install.sh
```

在文件夹`./aircraft-vue-django`下运行`install.sh`安装依赖

```
bash install.sh
```
## 开启服务
#### 两种启动方式，django模式和nginx+uwsgi+django模式

- django模式
在文件夹`/aircraft-vue-django`下运行以下指令开启服务

```
bash build.sh
python3 manage.py runserver 0.0.0.0:<your port>
```

- nginx+uwsgi+django模式
```
bash build.sh
python3 manage.py runserver 0.0.0.0:<your port>
bash start_nginx.sh
```

## 附加说明
1. 项目中有不少配置写死了/root/aircraft-vue-django路径，部署时需要根据实际情况修改
2. ./config/nginx.conf中配置了https，启动前确保申请好了证书，或者删除https配置