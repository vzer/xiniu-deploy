#!/usr/bin/env python
#coding=utf-8
__author__ = 'vzer'
#远端客户端属性
clientserviceLocalPath="/xiniu/client-updateapps/"
clientwebLocalPath="/xiniu/client-updatewar/"
clientjobLocalPath="/xiniu/client-updateapps/"
########################################生产环境变量配置############################################################

#++++++++++++++++++++++++++++++++++++++++生产platform平台环境++++++++++++++++++++++++++++++++++++++++++++++++++#
#后台服务主机ip地址集合
proplatserviceLocalPath="/xiniu/platform-updateapps/"
proplatserviceScriptFile="releaseservicedeploy.sh"
ProducePlatformServiceIp=(
    {"data":("192.168.0.35",),},
    {"distribution":("192.168.0.37",),},
    {"foundation":("192.168.0.33",),},
    {"financial":("192.168.0.38",),},
    {"integration":("192.168.0.42",),},
    {"log":("192.168.0.36",),},
    {"membership":("192.168.0.43",),},
    {"master":("192.168.0.34",),},
    {"promotion":("192.168.0.44",),},
    {"security":("192.168.0.39",),},
    {"workflow":("192.168.0.40",),},
    {"ecommerce":("192.168.0.41",),},
    {"statics":("192.168.0.45",),},
    {"reporting":("192.168.0.46",),},
    {"contents":("192.168.0.48",),},
    {"logistics":("192.168.0.47",),},
    {"tigerhill-customization":("192.168.0.49",),},
    {"mailqueue":("192.168.0.52",),},
    {"monitor":("192.168.0.53",),},

)

#前台web主机ip地址集合
#前台web地址信息
proplatwebLocalPath="/xiniu/platform-updatewar/"
proplatwebScriptFile="releasewebdeploy.sh"
ProducePlatformWebIp=(
    {"api":("192.168.0.27",),},
    {"auth":("192.168.0.20",),},
    {"employee":("192.168.0.21",),},
    {"web-backend":("192.168.0.23",),},
    {"web-distribution":("192.168.0.24",),},
    {"web-financial":("192.168.0.25",),},
    {"my":("192.168.0.22",),},
    {"open":("192.168.0.26",),},
    {"web-site":("10.252.147.252",),},
    {"ecommerce-web":("192.168.0.28",),},
    {"tigerhill-mall":("192.168.0.29",),},
    {"tigerhill-b2b":("192.168.0.30",),},
    {"tigerhill-admin":("192.168.0.31",),},
    {"monitor-web":("192.168.0.51",),},
    {"admin-web":("192.168.0.50",),},
)

#job类主机ip地址
#job类工程地址信息
proplatjobLocalPath="/xiniu/updateapps/"
proplatjobScriptFile="queuedeploy.sh"
ProducePlatformJobIp=(
    {"":("","",),},
)
#++++++++++++++++++++++++++++++++++++++++生产platform平台环境++++++++++++++++++++++++++++++++++++++++++++++++++#
########################################生产环境变量配置############################################################



#账户信息
user="root"
password="root@huqiu"

