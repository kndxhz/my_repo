# 我的项目
这是一个很杂的仓库，因为我有很多小项目，不方便单独开仓库，所以全部归纳在这仓库里
# ipv6_open
无需多言，这就是一个方便打开ipv6 URL的小工具
# ipv6_114514
这俩bat可以实现将你的家宽ipv6改为恶臭地址（恼
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
# 3in1
这是一个三码（微信、支付宝、QQ）合一的小程序</br>
可以实现基础的UA判断，返回不同内容</br>
但是微信需要长按扫描、支付宝可以直接跳转、QQ需要保存到相册（腾讯我超你妈）</br>
同时，欢迎大家给我打钱（</br>
<img src="./3in1/3in1.png">
# jtb
这是一个简单的，检测剪贴板更新并以toast提示出来的小东西</br>
用于防止剪贴板污染，尤其是进行比特币、波场转账等容易被污染且需要频繁复制粘贴的操作时
# kami
这是一个基于RSA非对称加密算法的卡密验证服务端</br>
需要客户端支持，大多数语言应该都支持RSA非对称加密</br>
使用双秘钥（双向链路，2公钥2私钥）+时间戳验证，保证不被篡改</br>
key.db是秘钥数据库，可以使用数据库查看软件（如Navicat）打开并生成、导入秘钥，快捷操作</br>
为了防止url参数过长/出现错误，使用PKCS#1+Hex加密，具体实现方式以及客户端对接方式可自行查看源码
# first_name
这个项目很简单</br>
就是专治学校里的那些谜语人的</br>
一天到晚正常名字不打,只会打拼音首字母</br>
使用这个程序,你只需要
1. 有python运行环境
2. 自己收集一份名字```names.txt```放在运行命令下,utf-8编码,一行一个名字(一般家长群都能找到)</br>
3. 运行```pip install pypinyin```安装依赖库</br>
4. ```python first_name.py```直接运行程序</br>