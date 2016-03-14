#!/usr/bin/env python
#coding=utf-8
__author__ = 'vzer'
#远端客户端属性
clientserviceLocalPath="/xiniu/client-updateapps/"
clientwebLocalPath="/xiniu/client-updatewar/"
clientjobLocalPath="/xiniu/client-updateapps/"
clientmeilocalPatch="/xiniu/mei-patch/mei_path/"
clientmeiremotePatch="/usr/local/jetty/work/jetty-0.0.0.0-80-root.war-_-any-"

########################################生产环境变量配置############################################################

#++++++++++++++++++++++++++++++++++++++++生产platform平台环境++++++++++++++++++++++++++++++++++++++++++++++++++#
#后台服务主机ip地址集合
proplatserviceLocalPath="/xiniu/platform-updateapps/"
proplatserviceScriptFile="releaseservicedeploy.sh"
ProducePlatformServiceIp=(
    {"data":("172.16.0.28","172.16.0.29",),},
    {"distribution":("172.16.0.32","172.16.0.33",),},
    {"foundation":("172.16.0.24","172.16.0.25",),},
    {"financial":("172.16.0.34","172.16.0.35",),},
    {"log":("172.16.0.30","172.16.0.31",),},
    {"master":("172.16.0.26","172.16.0.27",),},
    {"security":("172.16.0.36","172.16.0.37",),},
    {"workflow":("172.16.0.38","172.16.0.39",),},
    {"mei-ecommerce-app":("172.16.0.40","172.16.0.41",),},
    {"mei-customization-app":("172.16.0.42","172.16.0.43",),},

)

#前台web主机ip地址集合
#前台web地址信息
proplatwebLocalPath="/xiniu/platform-updatewar/"
proplatwebScriptFile="releasewebdeploy.sh"
proplatwebrestartFile="restartjetty.sh"
ProducePlatformWebIp=(
    {"api":("172.16.0.18","172.16.0.19",),},
    {"auth":("172.16.0.4","172.16.0.5",),},
    {"employee":("172.16.0.6","172.16.0.7",),},
    {"web-backend":("172.16.0.10","172.16.0.11",),},
    {"web-distribution":("172.16.0.12","172.16.0.13",),},
    {"web-financial":("172.16.0.14","172.16.0.15",),},
    {"my":("172.16.0.8","172.16.0.9",),},
    {"open":("172.16.0.16","172.16.0.17",),},
    {"mei-ecommerce-web":("172.16.0.20","172.16.0.21",),},
    {"mei-customization-web":("172.16.0.22","172.16.0.23",),},
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

########################################预发布环境变量配置############################################################
#++++++++++++++++++++++++++++++++++++++++预发布platform平台环境++++++++++++++++++++++++++++++++++++++++++++++++++#
#后台服务主机ip地址集合
preplatserviceLocalPath="/xiniu/platform-updateapps/"
preplatserviceScriptFile="releasepreservicedeploy.sh"
PrePlatformServiceIp=(
    {"data":("172.16.0.56",),},
    {"distribution":("172.16.0.58",),},
    {"foundation":("172.16.0.54",),},
    {"financial":("172.16.0.59",),},
    {"log":("172.16.0.57",),},
    {"master":("172.16.0.55",),},
    {"security":("172.16.0.60",),},
    {"workflow":("172.16.0.61",),},
    {"ecommerce":("172.16.0.62",),},
    {"mei-customization-app":("172.16.0.63",),},
)

#前台web主机ip地址集合
#前台web地址信息
preplatwebLocalPath="/xiniu/platform-updatewar/"
preplatwebScriptFile="releaseprewebdeploy.sh"
PrePlatformWebIp=(
    {"api":("172.16.0.51",),},
    {"auth":("172.16.0.44",),},
    {"employee":("172.16.0.45",),},
    {"web-backend":("172.16.0.47",),},
    {"web-distribution":("172.16.0.48",),},
    {"web-financial":("172.16.0.49",),},
    {"my":("172.16.0.46",),},
    {"open":("172.16.0.50",),},
    {"ecommerce-web":("172.16.0.52",),},
    {"mei-customization-web":("172.16.0.53",),},
)

#job类主机ip地址
#job类工程地址信息
preplatjobLocalPath="/xiniu/updateapps/"
preplatjobScriptFile="queuedeploy.sh"
PrePlatformJobIp=(
    {"":("","",),},
)
#++++++++++++++++++++++++++++++++++++++++预发布platform平台环境++++++++++++++++++++++++++++++++++++++++++++++++++#

########################################预发布环境变量配置############################################################




#账户信息
user="root"
password="9Tf78F9K"

