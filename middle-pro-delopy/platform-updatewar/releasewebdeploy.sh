#!/bin/bash

DAY=`date +%Y-%m-%d-%H:%M:%S`

#the old files for backup
OLD_FILE_PATH=/xiniu/backup/

#path of the shell script log
SHELL_LOG_PATH=/xiniu/log

#mkdir folder
mkdir -p $OLD_FILE_PATH
mkdir -p $SHELL_LOG_PATH

echo '=============================adp==================================='>>$SHELL_LOG_PATH/log_build.log
Web=$1
Version=$2
mode=$3
applocal=$4
appport=$5

if [ -z "$mode" ]; then
mode="yes"
fi

#Stop Service
time_now_1=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_1 'Begin to stop the webserver.....'>>$SHELL_LOG_PATH/log_build.log
/xiniu/jetty-$Web/bin/jetty.sh stop
time_now_2=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_2 'End to stop the webserver.....'>>$SHELL_LOG_PATH/log_build.log

#Del
echo '*******************************************************'>>$SHELL_LOG_PATH/log_build.log
time_now_5=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_5 'Begin to delete the files: ' root.war>>$SHELL_LOG_PATH/log_build.log
rm -f /xiniu/jetty-$Web/webapps/root.war
time_now_6=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_6 'End to delete the files....'>>$SHELL_LOG_PATH/log_build.log

#CP
echo '*******************************************************'>>$SHELL_LOG_PATH/log_build.log
time_now_7=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_7 'Begin to copy the build files: ' $Web-$Version.war>>$SHELL_LOG_PATH/log_build.log
cp -f $applocal$Web-$Version.war /xiniu/jetty-$Web/webapps/root.war
time_now_8=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_8 'End to copy the build files.....'>>$SHELL_LOG_PATH/log_build.log

#autoconfig
echo '*******************************************************'>>$SHELL_LOG_PATH/log_build.log
time_now_11=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_11 'Begin to autoconfig the files: ' root.war>>$SHELL_LOG_PATH/log_build.log
if [ "$mode" = "yes" ]; then
autoconfig /xiniu/jetty-$Web/webapps/root.war -c UTF-8 -s ssh://xiniu@10.173.83.161:/xiniu/antx.properties
elif [ "$mode" = "no" ]; then
autoconfig /xiniu/jetty-$Web/webapps/root.war -c UTF-8 -I
fi
time_now_12=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_12 'End to autoconfig the files:.....'>>$SHELL_LOG_PATH/log_build.log

#Start Service
echo '*******************************************************'>>$SHELL_LOG_PATH/log_build.log
time_now_13=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_13 'Begin to restart the webserver....'>>$SHELL_LOG_PATH/log_build.log
echo "Starting Jetty......"
/xiniu/jetty-$Web/bin/jetty.sh start > /dev/null 2>&1
###################################################################################################
jettyport=`netstat -ant |grep LISTEN | grep $appport | awk '{print $4}' | awk -F : '{print $2}' | head -n 1`
if [[ $jettyport = $appport ]]
then
        echo "Starting Jetty: OK"
else
        echo "Starting Jetty: FAILED"
fi
###################################################################################################
time_now_14=`date +%Y-%m-%d" "%H:%M:%S`
echo $time_now_14 'End to restart the webserver....'>>$SHELL_LOG_PATH/log_build.log
