#include<stdio.h>
#include<string.h>
#include<time.h>

typedef struct _nbiot_message{

	char IMSI[15];	/*15byte SIM卡IMSI号 例如：460111174807818；运营商分配的15位IMSI号码，对应的电信服务号码为13位。
	                通常人们知道的手机号如(+86)13901001234，在GSM网络中，这个号码的“学名”是“移动台ISDN号码(MSISDN)”。
	                但是，在运行中，与手机对应另外有一个号码，叫国际移动台识别码(IMSI)。该码才是GSM用户手机在全球惟一的标识码。
	                 IMSI号码可以从AT+CIMI指令返回值中获得。*/
	uint32_t  create_time;/*4byte 消息生成时间可以使用从运营商获得的时间，表示当前消息的生成时间。其值为长整型，代表从2018年1月1日零时起的秒数。*/
	uint8_t msg_type;/*1byte 消息类型正常心跳消息：1异常时通知消息：2紧急时改变工作模式通知:3*/
	uint16_t base_station_num;/*2byte 基站编号 two byte tracking area code (tac); +CEREG的返回信息中的tac值 */
	uint32_t cell_num; /*4byte 小区编号 four byte E-UTRAN cell ID；+CEREG的返回信息中的ci值*/
	uint8_t battery_level;/*电池电量 以0-255来表示当前电压大小，具体数据代表的电压值须根据测试结果来定*/
	uint8_t business_mode;/*1byte 当前业务模式 库存模式:1标准模式:2备战模式:3寻枪模式:4*/
	uint8_t g_senser_mode;/*1byte G-Senser激活模式 振动激活MCU:1跌落激活MCU:2*/
    char coordinate[24];   /*24byte 当前设备的坐标例如纬度4717.11437N，经度00833.91522E，将他们拼接起来一起发送，
	                      格式为：4717.11437N,00833.91522E。不需要发送定位数据时，用一个分号“;”代替。*/
    char speed[6];/*6byte 速度 例如：01.636，单位：节。1节=1海里/小时=1852米/小时。不需要发送定位数据时，用一个分号“;”代替。*/
    char move_dir[6]; /*6byte 运动方向 以正北为0度,顺时针起航向与正北的夹角。例如：220.23或者077.52。不需要发送定位数据时，用一个分号“；”代替。*/
    uint32_t locate_time;/*32byte 定位时间 获得上述定位信息的时间。
                            其值为长整型，代表从2018年1月1日零时起的秒数。不需要发送定位数据时，用一个分号“；”代替。*/
}nbiot_message;
