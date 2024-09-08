@echo off
title ipv6地址合成
echo 说明：把ipv6地址自动加上[]，然后加上端口
set /p ipv6=请输入ipv6地址...
set /p port=请输入端口...
echo 合成后的ipv6地址为：
echo [%ipv6%]:%port%
start "" "http://[%ipv6%]:%port%"
pause
%0