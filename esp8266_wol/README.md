# esp8266_wol
这是一个基于esp8266的WOL服务器，可以发送WOL包，搭配易语言客户端，可以实现媒体控制、开关机等功能</br>
同时接入点灯+小爱同学，实现外网操作</br>
媒体控制是通过网易云默认快捷键实现的，所以你不能改快捷键或切后台（改了自己改易语言客户端代码，也可以利用全局快捷键实现后台切换）</br>
点灯客户端可用指令（点灯客户端输入）
```
shutdown
按钮开关机
上一曲
下一曲
音量加
音量减
喜欢
收藏
暂停
播放
```
小爱同学可用指令
```
开电脑
关电脑
```
点灯界面配置
```
{¨config¨{¨headerColor¨¨transparent¨¨headerStyle¨¨dark¨¨background¨{¨img¨¨assets/img/bg/2.jpg¨}}¨dashboard¨|{¨type¨¨btn¨¨ico¨¨fal fa-power-off¨¨mode¨Ê¨t0¨´´¨t1¨¨文本2¨¨bg¨Ê¨cols¨Í¨rows¨Í¨key¨¨btn-pc¨´x´Ë´y´Í¨lstyle¨Ë¨clr¨¨#00A90C¨}{ß9¨deb¨ßDÉßHÉßIÑßJÍßK¨debug¨´x´É´y´ÉßMÊ}{ß9¨inp¨ßHÊßIÑßJËßK¨inp-u6l¨´x´É´y´Ñ}{ß9¨tim¨ßHÉßIËßJËßK¨timing¨´x´É´y´¤A}÷¨actions¨|¦¨cmd¨¦¨switch¨‡¨text¨‡¨on¨¨打开?name¨¨off¨¨关闭?name¨—÷¨triggers¨|{¨source¨ßX¨source_zh¨¨开关状态¨¨state¨|ßZßb÷¨state_zh¨|¨打开¨¨关闭¨÷}÷¨rt¨|÷}
```
