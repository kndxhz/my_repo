@echo off
title �ָ��̶�ipv6
echo ��ʹ�ù���ԱȨ�����У���������ʹ������ԣ�
echo ��ʹ�ù���ԱȨ�����У���������ʹ������ԣ�
echo ��ʹ�ù���ԱȨ�����У���������ʹ������ԣ�
netsh interface ipv6 show addresses
set /p ip= ������������̶���ipv6��ַ��
netsh interface ipv6 set privacy state=enable
netsh interface ipv6 delete address ��̫�� %ip%
netsh interface set interface ��̫�� admin=disable
netsh interface set interface ��̫�� admin=enable
echo ȫ����ɣ�
pause