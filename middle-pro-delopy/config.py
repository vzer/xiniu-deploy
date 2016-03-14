#!/usr/bin/env python
#coding=utf-8
__author__ = 'vzer'
#远端客户端属性
clientserviceLocalPath="/xiniu/client-updateapps/"
clientwebLocalPath="/xiniu/client-updatewar/"
clientjobLocalPath="/xiniu/client-updateapps/"
clientmeilocalPatch="/xiniu/tigerhill-patch/"
clientmeiremotePatch="/usr/local/jetty/work/jetty-0.0.0.0-80-root.war-_-any-"

########################################生产环境变量配置############################################################

#++++++++++++++++++++++++++++++++++++++++生产platform平台环境++++++++++++++++++++++++++++++++++++++++++++++++++#
#后台服务主机ip地址集合
proplatserviceLocalPath="/xiniu/platform-updateapps/"
proplatserviceScriptFile="releaseservicedeploy.sh"
ProducePlatformServiceIp=(
    {"foundation":(("10.173.83.161",30002,),("10.132.180.10",30002,),),},
    {"platform":(("10.173.83.161",30003,),("10.132.180.10",30003,),),},
    {"logistics":(("10.173.83.161",30004,),("10.132.180.10",30004,),),},
    {"financial":(("10.173.83.161",30005,),("10.132.180.10",30005,),),},
    {"backend":(("10.173.87.46",30002,),("10.132.179.236",30002,),),},
    {"marketplace":(("10.173.87.46",30003,),("10.132.179.236",30003,),),},
    {"distribution":(("10.173.87.46",30004,),("10.132.179.236",30004,),),},
    {"mall":(("10.132.181.210",30001,),),},
)

#前台web主机ip地址集合
#前台web地址信息
proplatwebLocalPath="/xiniu/platform-updatewar/"
proplatwebScriptFile="releasewebdeploy.sh"
proplatwebrestartFile="restartjetty.sh"
ProducePlatformWebIp=(
    {"auth":(("10.173.84.205",30001,),("10.132.180.28",30001,),),},
    {"employee":(("10.173.84.205",30002,),("10.173.84.205",30002,),),},
    {"web-distribution-ec":(("10.173.84.205",30003,),("10.132.180.28",30003,),),},
    {"open":(("10.153.197.206",30002,),("10.132.180.21",30002,),),},
    {"web-backend":(("10.153.197.206",30003,),("10.132.180.21",30003,),),},
    {"web-distribution":(("10.153.197.206",30004,),("10.132.180.21",30004,),),},
    {"service":(("10.153.195.137",30001,),("10.132.180.31",30001,),),},
    {"web-financial":(("10.153.195.137",30003,),("10.132.180.31",30003,),),},
    {"web-logistics":(("10.153.195.137",30002,),("10.132.180.31",30002,),),},
    {"web-mall":(("10.132.181.238",30001,),),},
    {"web-mall-admin":(("10.132.181.238",30002,),),},

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
    {"foundation":(("10.132.180.19",30002,),),},
    {"platform":(("10.132.180.19",30003,),),},
    {"logistics":(("10.132.180.19",30004,),),},
    {"financial":(("10.132.180.19",30005,),),},
    {"backend":(("10.132.180.25",30002,),),},
    {"marketplace":(("10.132.180.25",30003,),),},
    {"distribution":(("10.132.180.25",30004,),),},
    {"mall":(("10.132.181.216",30001,),),},
)

#前台web主机ip地址集合
#前台web地址信息
preplatwebLocalPath="/xiniu/platform-updatewar/"
preplatwebScriptFile="releaseprewebdeploy.sh"
PrePlatformWebIp=(
    {"auth":(("10.132.180.14",30001,),),},
    {"employee":(("10.132.180.14",30002,),),},
    {"web-distribution-ec":(("10.132.180.14",30003,),),},
    {"open":(("10.132.180.34",30002,),),},
    {"web-backend":(("10.132.180.34",30003,),),},
    {"web-distribution":(("10.132.180.34",30004,),),},
    {"service":(("10.132.180.37",30001,),),},
    {"web-financial":(("10.132.180.37",30003,),),},
    {"web-logistics":(("10.132.180.37",30002,),),},
    {"web-mall":(("10.132.181.206",30001,),),},
    {"web-mall-admin":(("10.132.181.206",30002,),),},
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
password="xiniunet_#zhongheng"

