#define BLINKER_WIFI
#define BLINKER_MIOT_OUTLET
#include <Blinker.h>
#include <WiFiUdp.h>
#include <WakeOnLan.h>
#include <ESP8266WiFi.h>
#include <ESP8266Ping.h>
#include <WiFiClient.h> // 新增WiFi客户端库

char auth[] = "your id";
char ssid[] = "your wifi id";
char pswd[] = "your wifi pwd";
const int port = 29763;

bool PCState = 0;
const char *MACAddress = "your pc MAC";
IPAddress ip(192, 168, 31, 154);//你的电脑ip地址（必须要是静态！！！）
BlinkerButton button("btn-pc");

WiFiUDP udp;
WakeOnLan wol(udp);
WiFiClient myclient; // 新增WiFi客户端对象

void change_state(const String & state){
    if (state == "on"){   
      digitalWrite(LED_BUILTIN, LOW);
      wol.sendMagicPacket(MACAddress);
      BlinkerMIOT.powerState(state);
    } else if (state == "off") { // 新增关机功能
      digitalWrite(LED_BUILTIN, LOW);
      if (myclient.connect(ip, port)) {
        myclient.write("shutdown");
        myclient.stop();
      }
      BlinkerMIOT.powerState(state);
    }
    PCState = state == "on" ? 1 : 0;
    BUILTIN_SWITCH.print(state);
    button.print(state);

    BlinkerMIOT.powerState(state);
    BlinkerMIOT.print();
    delay(1500);    
    digitalWrite(LED_BUILTIN, HIGH);
}

void switch_callback(const String & state)
{
    BLINKER_LOG("APP列表开关状态: ", state);
    change_state(state);
}

void button_callback(const String & state)
{
    BLINKER_LOG("APP按钮状态: ", state);
    change_state(state);
    Blinker.vibrate();
}

void miotPowerState(const String & state)
{
    BLINKER_LOG("小爱同学状态: ", state);
    change_state(state);
}

void dataRead(const String &data) {
    BLINKER_LOG("Blinker readString: ", data);
    Blinker.vibrate();
    uint32_t BlinkerTime = millis();
    Blinker.print("millis", BlinkerTime);
    if (myclient.connect(ip, port)) {
        myclient.write(data.c_str()); // 修改这行代码
        myclient.stop();
    }
}


void miotQuery(int32_t queryCode, uint8_t num)
{
    BLINKER_LOG("AliGenie Query outlet: ", num,", codes: ", queryCode);

    switch (queryCode)
    {
        case BLINKER_CMD_QUERY_ALL_NUMBER :
            BLINKER_LOG("MIOT Query All");
            BlinkerMIOT.powerState(PCState ? "on" : "off");
            BlinkerMIOT.print();
            break;
        case BLINKER_CMD_QUERY_POWERSTATE_NUMBER :
            BLINKER_LOG("MIOT Query Power State");
            BlinkerMIOT.powerState(PCState ? "on" : "off");
            BlinkerMIOT.print();
            break;
        default :
            BlinkerMIOT.powerState(PCState ? "on" : "off");
            BlinkerMIOT.print();
            break;
    }
}
  
void heartbeat()
{    
    PCState = Ping.ping(ip) ? 1 : 0;
    BUILTIN_SWITCH.print(PCState ? "on" : "off");
    button.print(PCState ? "on" : "off");
    BLINKER_LOG("心跳检测PC状态",PCState);
}
 
void setup()
{
    Serial.begin(115200);
    BLINKER_DEBUG.stream(Serial);
    
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, HIGH);  
  
    Blinker.begin(auth, ssid, pswd);
    Blinker.attachData(dataRead);
    Blinker.attachHeartbeat(heartbeat);
    BUILTIN_SWITCH.attach(switch_callback);
    button.attach(button_callback);
    
    while (WiFi.status() != WL_CONNECTED) {
          delay(500);
          Serial.print(".");
    }
    wol.setRepeat(3, 100); 

    BUILTIN_SWITCH.print(PCState ? "on" : "off");
    button.print(PCState ? "on" : "off");
  
    BlinkerMIOT.attachPowerState(miotPowerState);
}
 
void loop()
{
    Blinker.run();
}
