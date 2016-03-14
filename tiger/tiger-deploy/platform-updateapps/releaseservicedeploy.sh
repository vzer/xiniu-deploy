#!/bin/bash

DAY=`date +%Y-%m-%d-%H:%M:%S`

#msg of the old files for backup
OLD_FILE_PATH=/xiniu/backup/

#path of the shell script log
SHELL_LOG_PATH=/xiniu/log

#mkdir folder
mkdir -p $OLD_FILE_PATH
mkdir -p $SHELL_LOG_PATH

echo '=============================adp==================================='>>$SHELL_LOG_PATH/log_build.log

#Stop Service
time_now_1=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_1 'Begin to stop the service.....'>>$SHELL_LOG_PATH/log_build.log
Service=$1
Version=$2
mode=$3
applocal=$4

if [ -z "$mode" ]; then
mode="yes"
fi

netstat -lnp | grep 20880 | awk '{print $7}' | sed 's/\/java/ /' | xargs kill -9
#/xiniu/Apps/$Service/v1.0.0/$Service-business-$Version/bin/stop.sh
time_now_2=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_2 'End to stop the service.....'>>$SHELL_LOG_PATH/log_build.log

#Backup
echo '*******************************************************'>>$SHELL_LOG_PATH/log_build.log
time_now_3=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_3 'Begin to backup the files: '$Service-business-$Version>>$SHELL_LOG_PATH/log_build.log
cp -r /xiniu/apps/$Service  $OLD_FILE_PATH/$Service-$DAY
time_now_4=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_4 'End to backup the files.....'>>$SHELL_LOG_PATH/log_build.log

#Del old backup
w=$(($(ls /xiniu/backup | wc -l)-5))
cd /xiniu/backup
if [ $(ls | wc -l) -gt 5 ]
    then
        rm -rf $(ls -rt | head -n$w)
    fi

#########################################

#Del
echo '*******************************************************'>>$SHELL_LOG_PATH/log_build.log
time_now_5=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_5 'Begin to delete the files: ' $Service-business-$Version>>$SHELL_LOG_PATH/log_build.log
rm -rf /xiniu/apps/$Service
time_now_6=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_6 'End to delete the files....'>>$SHELL_LOG_PATH/log_build.log

#CP
echo '*******************************************************'>>$SHELL_LOG_PATH/log_build.log
time_now_7=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_7 'Begin to copy the build files: ' $Service-business-$Version>>$SHELL_LOG_PATH/log_build.log
mkdir -p /xiniu/apps/$Service/$Version/
cp -r $applocal$Service-business-$Version-assembly.tar.gz /xiniu/apps/$Service/$Version
time_now_8=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_8 'End to copy the build files.....'>>$SHELL_LOG_PATH/log_build.log

#Extract
echo '*******************************************************'>>$SHELL_LOG_PATH/log_build.log
time_now_11=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_11 'Begin to uncompress the files: ' $Service-business-$Version>>$SHELL_LOG_PATH/log_build.log
cd /xiniu/apps/$Service/$Version
tar -zxvf /xiniu/apps/$Service/$Version/$Service-business-$Version-assembly.tar.gz
time_now_12=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_12 'End to uncompress the files:.....'>>$SHELL_LOG_PATH/log_build.log

#Autoconfig
echo '*******************************************************'>>$SHELL_LOG_PATH/log_build.log
time_now_15=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_15 'Begin to autoconfig: ' $Service-business-$Version>>$SHELL_LOG_PATH/log_build.log
cd /xiniu/apps/$Service/$Version
if [ "$mode" = "yes" ]; then
autoconfig $Service-business-$Version* -c UTF-8 -s ssh://xiniu@192.168.0.33:/xiniu/antx.properties
autoconfig $Service-business-$Version*/lib/$Service-business-$Version*.jar -c UTF-8 -s ssh://xiniu@192.168.0.33:/xiniu/antx.properties
elif [ "$mode" = "no" ]; then
autoconfig $Service-business-$Version -c UTF-8 -I
autoconfig $Service-business-$Version/lib/$Service-business-$Version.jar -c UTF-8 -I
fi
time_now_16=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_16 'End to uncompress the files:.....'>>$SHELL_LOG_PATH/log_build.log

#Start Service
echo '*******************************************************'>>$SHELL_LOG_PATH/log_build.log
time_now_13=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_13 'Begin to restart the system....'>>$SHELL_LOG_PATH/log_build.log
echo 'Start File is:' /xiniu/Apps/$Service/v1.0.0/$Service-business-$Version/bin/start.sh>>$SHELL_LOG_PATH/log_build.log
cd /xiniu/apps/$Service/$Version/$Service-business-$Version*/bin/
./start.sh
time_now_14=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_14 'End to restart the system....'>>$SHELL_LOG_PATH/log_build.log
