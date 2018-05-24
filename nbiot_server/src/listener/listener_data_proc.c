#include "listener_data_proc.h"
#include "config_file_ctrl_device.h"
#include "msg_queue.h"

int doproc_listener(int msg_id,int server_fd)
{
//	int server_fd;
//	int ret;
//	struct sockaddr_in ser_addr;
//	int server_port = 0;
//	char* ipaddress = NULL;
//
//	server_port = GetIniKeyInt_with1("server","port",CONFIG_FILE_PATH);
//    ipaddress = GetIniKeyString_with1("server", "ip", CONFIG_FILE_PATH);
//    printf("server_ip: %s, port: %d\n",ipaddress,server_port);
//	if(0 == server_port)
//	{
//		server_port = 20111;
//		printf("*get port form config failed! ,using defaul port:%d\n",server_port);
//	}
//
//	if(!strcmp(ipaddress,""))
//	{
//		ipaddress = "127.0.0.1";
//		printf("*get server_ip form config failed! ,using defaul server_ip:%s\n",ipaddress);
//	}
//
//    //创建socket对象
//    server_fd = socket(AF_INET,SOCK_DGRAM,0);//AF_INET:IPV4; SOCK_DGRAM:UDP
//    if(server_fd < 0)
//    {
//    	printf("create socket fail! \n");
//    	return -1;
//    }
//
//    //创建网络通信对象
//    memset(&ser_addr,0,sizeof(ser_addr));
//    ser_addr.sin_family =AF_INET;
//    ser_addr.sin_port =htons(server_port);//IP地址，需要进行网络序转换
//    ser_addr.sin_addr.s_addr=inet_addr(ipaddress);
//
//    //绑定socket对象与通信链接
//    ret =bind(server_fd,(struct sockaddr*)&ser_addr,sizeof(ser_addr));
//    if(ret < 0)
//    {
//        printf("listener udp socket bind failed\n");
//        return -1;
//
//    }
//    printf("ser_addr.sin_port:%d\n",ser_addr.sin_port);
    //处理接收到的数据
    handle_udp_msg(server_fd,msg_id);
//	close(server_fd);
	return 0;
}

void handle_udp_msg(int fd, int msg_id)
{
	printf("listener process: in handle_udp_msg...\n");
    char buf[_SIZE_];  //接收缓冲区，1024字节
    char buf_add[_SIZE_ + 20];
    socklen_t len;
    int count;
    struct sockaddr_in clent_addr;  //clent_addr用于记录发送方的地址信息
    //nbiot_message iot_msg;
    //char imsi[15];

    uint16_t id;
    int i;
    int send_message_len = 0;
    while(1)
    {
        memset(buf, 0, sizeof(buf));
        memset(buf_add,0,sizeof(buf_add));
        //memset(&iot_msg,0,sizeof(iot_msg));
        len = sizeof(clent_addr);
        count = recvfrom(fd, buf, _SIZE_, 0, (struct sockaddr*)&clent_addr, &len);  //recvfrom是拥塞函数，没有数据就一直拥塞
        if(count == -1)
        {
            printf("recieve data fail!\n");
            return;
        }
        printf("listener process: fd:%d, clent_addr port:%d,ip:%s\n",fd,clent_addr.sin_port,inet_ntoa(clent_addr.sin_addr));

        //将要放入消息队列的数据中加入client_addr ,fd
        memcpy(buf_add,&fd,sizeof(fd));
        memcpy(buf_add+4,&clent_addr,len);
        memcpy(buf_add+4+len,buf,sizeof(buf));

        //向消息队列中写消息并发送
        printf("listener process:send_msg...\n");
        printf("listener process:msg_pid = %d\n",msg_id);
        send_message_len = sizeof(buf_add);
        send_msg(msg_id,ser_send_type,buf_add,send_message_len);
        printf("listener process(%d): msg -d:%d\n",getpid(),msg_id);
        printf("listener process(%d): ser_send_type :%d\n",getpid(),ser_send_type);

        memcpy(&id,buf,sizeof(id));
        printf("listener process: receive from client idx = %d\n",id);
        //printf("client:%s\n",buf);  //打印client发过来的信息
        //memcpy(imsi,buf+3,sizeof(iot_msg.IMSI));
        //printf("client:%s",imsi);
//        memset(buf, 0, BUFF_LEN);
//        sprintf(buf, "I have recieved %d bytes data!\n", count);  //回复client
//        printf("server:%s\n",buf);  //打印自己发送的信息给
        printf("listener process(pid:%d), port:%d, addr:%s\n",getpid(),clent_addr.sin_port,inet_ntoa(clent_addr.sin_addr));
//        sendto(fd, buf_add, BUFF_LEN, 0, (struct sockaddr*)&clent_addr, len);  //发送信息给client，注意使用了clent_addr结构体指针

    }
}

