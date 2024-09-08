@echo off
title 恢复固定ipv6
echo 请使用管理员权限运行！！！（已使用请忽略）
echo 请使用管理员权限运行！！！（已使用请忽略）
echo 请使用管理员权限运行！！！（已使用请忽略）
netsh interface ipv6 show addresses
set /p ip= 请输入上文你固定的ipv6地址：
netsh interface ipv6 set privacy state=enable
netsh interface ipv6 delete address 以太网 %ip%
netsh interface set interface 以太网 admin=disable
netsh interface set interface 以太网 admin=enable
echo 全部完成！
pause