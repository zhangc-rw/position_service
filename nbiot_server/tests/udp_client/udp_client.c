//socket udp 客户端
#include<stdio.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<unistd.h>
#include<arpa/inet.h>

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include "udp_client.h"

#define SERVER_PORT 20111
#define BUFF_LEN 512
#define BUFF_LEN_ADD 514
#define SERVER_IP "172.0.5.182"

int pack_message(char msg[])
{
	char* temp_buf;
	uint16_t idx = 0;
	uint8_t format_ver = '1';/*格式版本号 1，	代表没有加密处理的原始数据格式
								2，	代表使用简单加密的格式
								3，	代表使用服务器公钥的加密格式*/
	nbiot_message iot_msg;
	memset(&iot_msg,0,sizeof(iot_msg));
	strcpy(iot_msg.IMSI,"460111174807818");
	iot_msg.create_time = 123456;
	iot_msg.msg_type = '1';
	iot_msg.base_station_num = 23;
	iot_msg.cell_num = 25;
	iot_msg.battery_level = '4';
	iot_msg.business_mode = '3';
	iot_msg.g_senser_mode = '1';
	strcpy(iot_msg.coordinate,"4717.11437N,00833.91522E");
	strcpy(iot_msg.speed,"01.636");
	strcpy(iot_msg.move_dir,"220.23");
	iot_msg.locate_time = 56984;


	temp_buf = msg;
	memcpy(temp_buf,&idx,sizeof(idx));
	temp_buf += 2;

	memcpy(temp_buf,&format_ver,sizeof(format_ver));
	temp_buf += 1;

	memcpy(temp_buf,iot_msg.IMSI,sizeof(iot_msg.IMSI));
	temp_buf += 15;

	memcpy(temp_buf,&iot_msg.create_time,sizeof(iot_msg.create_time));
	temp_buf += 4;

	memcpy(temp_buf,&iot_msg.msg_type,sizeof(iot_msg.msg_type));
	temp_buf += 1;

	memcpy(temp_buf,&iot_msg.base_station_num,sizeof(iot_msg.base_station_num));
	temp_buf += 2;

	memcpy(temp_buf,&iot_msg.cell_num,sizeof(iot_msg.cell_num));
	temp_buf += 4;

	memcpy(temp_buf,&iot_msg.battery_level,sizeof(iot_msg.battery_level));
	temp_buf += 1;

	memcpy(temp_buf,&iot_msg.business_mode,sizeof(iot_msg.business_mode));
	temp_buf += 1;

	memcpy(temp_buf,&iot_msg.g_senser_mode,sizeof(iot_msg.g_senser_mode));
	temp_buf += 1;

	memcpy(temp_buf,iot_msg.coordinate,sizeof(iot_msg.coordinate));
	temp_buf += 24;

	memcpy(temp_buf,iot_msg.speed,sizeof(iot_msg.speed));
	temp_buf += 6;

	memcpy(temp_buf,iot_msg.move_dir,sizeof(iot_msg.move_dir));
	temp_buf += 6;

	memcpy(temp_buf,&iot_msg.locate_time,sizeof(iot_msg.locate_time));
	temp_buf += 4;

	return 0;
}

void udp_msg_sender(int fd, struct sockaddr* dst)
{
	printf("in udp_msg_sender...\n");
    socklen_t len;
    struct sockaddr_in src;
    char buf[BUFF_LEN];
    char buf_add[BUFF_LEN_ADD];
    //char imsi[15];
    uint16_t id_num;
    uint16_t tmp = 0;
    int i;
    while(1)
    {
    	tmp++;
        //char buf[BUFF_LEN] = "TEST UDP MSG!\n";
    	memset(buf,0,sizeof(buf));
    	memset(buf_add,0,sizeof(buf_add));
    	pack_message(buf);
    	memcpy(buf,&tmp,sizeof(tmp));
        len = sizeof(*dst);
        //printf("client:%s\n",buf);  //打印自己发送的信息
        //memcpy(imsi,buf+3,15);
        //printf("client: IMSI %s",imsi);
        //memcpy(&id_num,buf,sizeof(id_num));
        //printf("client send idx = %d\n",id_num);

        sendto(fd, buf, BUFF_LEN, 0, dst, len);

		//test
        printf("udp client: sendto fd=%d\n",fd);
	    for(i=0;i<10;i++)
	    {
	    	printf("udp client: send to listener peocess:%d\n",buf[i]);
	    }
		//
	    printf("udp client: recvfrom fd=%d\n",fd);
	    printf("udp client, port:%d, addr:%s\n",src.sin_port,inet_ntoa(src.sin_addr));
        printf("client src port:%d\n",ntohs(src.sin_port));
        memset(buf, 0, BUFF_LEN);
        recvfrom(fd, buf, BUFF_LEN, 0, (struct sockaddr*)&src, &len);  //接收来自server的信息
		//test
        printf("udp client: receive from worker peocess:");
	    for(i=0;i<10;i++)
	    {
	    	printf(" %d",buf[i]);
	    }
	    printf("\n");
		//
//        printf("server:%s\n",buf);

        sleep(5);  //一秒发送一次消息
    }
}

/*
    client:
            socket-->sendto-->revcfrom-->close
*/

int main(int argc, char* argv[])
{
    int client_fd;
    struct sockaddr_in ser_addr;

    client_fd = socket(AF_INET, SOCK_DGRAM, 0);
    if(client_fd < 0)
    {
        printf("create socket fail!\n");
        return -1;
    }

    memset(&ser_addr, 0, sizeof(ser_addr));
    ser_addr.sin_family = AF_INET;
    //ser_addr.sin_addr.s_addr = inet_addr(SERVER_IP);
    //ser_addr.sin_addr.s_addr = htonl(INADDR_ANY);  //注意网络序转换
    ser_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
    ser_addr.sin_port = htons(SERVER_PORT);  //注意网络序转换
    printf("client dst port:%d\n",ser_addr.sin_port);
    udp_msg_sender(client_fd, (struct sockaddr*)&ser_addr);

    close(client_fd);

    return 0;
}


//int main()
//{
//    //创建socket对象
//    int sockfd=socket(AF_INET,SOCK_DGRAM,0);
//
//    //创建网络通信对象
//    struct sockaddr_in addr;
//    addr.sin_family =AF_INET;
//    addr.sin_port =htons(20111);
//    addr.sin_addr.s_addr = inet_addr("127.0.0.1");
//
//    while(1)
//    {
//        printf("请输入一个数字：");
//        char buf=0;
//        scanf("%hhd",&buf);
//        sendto(sockfd,&buf,
//        sizeof(buf),0,(struct sockaddr*)&addr,sizeof(addr));
//
//        socklen_t len=sizeof(addr);
//        recvfrom(sockfd,&buf,sizeof(buf),0,(struct sockaddr*)&addr,&len);
//
//        if(66 ==buf)
//        {
//            printf(" server 成功接受\n");
//        }
//        else
//        {
//            printf("server 数据丢失\n");
//        }
//
//    }
//    close(sockfd);
//
//}
