#!/bin/bash
echo -e "Starting Jetty ...\c"
nohup /usr/local/jetty/bin/jetty.sh restart > /dev/null 2>&1 &
COUNT=0
while [[ $COUNT -lt 1 ]]; do
    echo -e ".\c"
    sleep 1
    COUNT="nc -v -z 127.0.0.1 80|grep -c succeeded"

done

echo "OK!"
