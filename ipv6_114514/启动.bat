@echo off
title �����̶�ipv6
echo ��ʹ�ù���ԱȨ�����У���������ʹ������ԣ�
echo ��ʹ�ù���ԱȨ�����У���������ʹ������ԣ�
echo ��ʹ�ù���ԱȨ�����У���������ʹ������ԣ�
set /p ip= ���������ipv6ǰ׺��
set ipb=%ip%114:514:1919:810
echo ��ip��%ipb%
netsh interface ipv6 set privacy state=disable
netsh interface set interface ��̫�� admin=disable
netsh interface set interface ��̫�� admin=enable
timeout /t 10 /nobreak
netsh interface ipv6 show addresses
set /p aip= ������������̫����ԭ����ipv6��ַ��
netsh interface ipv6 add address ��̫�� %ipb%
netsh interface ipv6 delete address ��̫�� %aip%
echo ȫ����ɣ�
pause