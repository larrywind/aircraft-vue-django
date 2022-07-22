# aircraft

## 简介

本项目采用vue3+django，实现了一套简单的飞机大战游戏，渲染使用pixijs

## 构建项目

需要以下组件：
```
Node: 12.16.3
npm: 6.14.4
python3: 3.7
mariadb: 10.5.6
```
安装mariadb
```
yum --allowerasing install mariadb-server mariadb -y
systemctl start mariadb
```
在文件夹`./aircraft`下运行`pre_install.sh`部署npm和node环境

```
bash pre_install.sh
```

在文件夹`./aircraft`下运行`install.sh`安装依赖

```
bash install.sh
```

在文件夹`/aircraft`下运行以下指令开启服务

```
python3 manage.py runserver 0.0.0.0:<your port>
```