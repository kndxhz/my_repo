@echo off
title 启动固定ipv6
echo 请使用管理员权限运行！！！（已使用请忽略）
echo 请使用管理员权限运行！！！（已使用请忽略）
echo 请使用管理员权限运行！！！（已使用请忽略）
set /p ip= 请输入你的ipv6前缀：
set ipb=%ip%114:514:1919:810
echo 新ip：%ipb%
netsh interface ipv6 set privacy state=disable
netsh interface set interface 以太网 admin=disable
netsh interface set interface 以太网 admin=enable
timeout /t 10 /nobreak
netsh interface ipv6 show addresses
set /p aip= 请输入上文以太网的原来的ipv6地址：
netsh interface ipv6 add address 以太网 %ipb%
netsh interface ipv6 delete address 以太网 %aip%
echo 全部完成！
pause