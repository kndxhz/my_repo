@echo off
title ipv6��ַ�ϳ�
echo ˵������ipv6��ַ�Զ�����[]��Ȼ����϶˿�
set /p ipv6=������ipv6��ַ...
set /p port=������˿�...
echo �ϳɺ��ipv6��ַΪ��
echo [%ipv6%]:%port%
start "" "http://[%ipv6%]:%port%"
pause
%0