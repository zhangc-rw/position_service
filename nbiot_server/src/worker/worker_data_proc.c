#include "worker_data_proc.h"
#include "msg_queue.h"

int doproc_worker(int pid)
{
	//建立消息队列:listener进程写，worker进程读取
    int msg_lis_id = get_msg_queue(_PATH_NAME_LISTEN,_PROJ_ID_LISTEN);
    if(msg_lis_id < 0)
    {
        return 1;
    }
    //建立消息队列:master进程写，worker进程读取
    int msg_work_id = get_msg_queue(_PATH_NAME_WORKER,_PROJ_ID_WORKER);
    if(msg_work_id < 0)
    {
        return 1;
    }

    pthread_t id_recv_listener_msg;
    pthread_t id_recv_worker_msg;
    char buf_add[_SIZE_+20];
    char buf[_SIZE_];
    char buf_command[_SIZE_];
    command_arr *commarr;
    //nbiot_message iot_msg;
    uint16_t idx = 0;
    int fd = 0;
    socklen_t len;
    struct sockaddr_in clent_addr;
    struct msqid_ds msg_listener_info;
    struct msqid_ds msg_worker_info;
    int i = 0;
    int ret = -1;
    int msg_listener_count = 0;
    int msg_worker_count = 0;

	while(1)
	{
		memset(buf_add,0,sizeof(buf_add));
		memset(buf,0,sizeof(buf));
		memset(&msg_listener_info,0,sizeof(msg_listener_info));
		memset(&msg_worker_info,0,sizeof(msg_worker_info));

		printf("worker process(pid:%d): doproc_worker...\n",pid);

		//判断listener进程发送的消息队列是否有消息
		ret = msgctl(msg_lis_id, IPC_STAT, &msg_listener_info);
		printf("worker process(%d):get msg_listen_id(%d) msgctl ret=%d, \n",pid,msg_lis_id,ret);
		printf("worker process(%d):get msg_listen_id(%d) msg_listen count=%d, \n",pid,msg_lis_id,msg_listener_info.msg_qnum);
		if(-1 == ret)
		{
			printf("worker process(%d):get msg_listen_id(%d) get info failed(%s), \n",pid,msg_lis_id,strerror(errno));
			continue;
		}
		//当前listener进程发送的消息队列中消息的数量
		msg_listener_count = msg_listener_info.msg_qnum;
//		if(msg_listener_count > 0)
//		{
//			//接收由listener进程发送的设备信息
//			ret = recv_msg(msg_listen_id,ser_send_type,buf_add);
//			if(-1 == ret)
//			{
//				printf("worker process(%d):reveive msg(msgid:%d) error,%s\n",pid,msg_listen_id,strerror(errno));
//				continue;
//			}
//
//		}
		printf("woker process（%d）:msg_listen_id = %d\n",pid,msg_lis_id);

		//判断mater进程发送的消息队列是否有消息
		ret = msgctl(msg_work_id, IPC_STAT, &msg_worker_info);
		printf("worker process(%d):get msg_worker_id(%d) msgctl ret=%d, \n",pid,msg_work_id,ret);
		printf("worker process(%d):get msg_worker_id(%d) msg_worker count=%d, \n",pid,msg_work_id,msg_worker_info.msg_qnum);
//		if(-1 == ret)
//		{
//			printf("worker process(%d):get msg_listen_id(%d) info failed(%s), \n",pid,msg_work_id,strerror(errno));
//			continue;
//		}
		//当前master进程发送的消息队列中消息的数量
		msg_worker_count = msg_worker_info.msg_qnum;
//		if(msg_worker_count > 0)
//		{
//			//接收由master进程发送的设备指令
//			ret = recv_msg(msg_worker_id,master_send_comm_type,buf_command);
//			if(-1 == ret)
//			{
//				printf("worker process(%d):reveive msg error,%s\n",pid,strerror(errno));
//			}
//		}
		printf("woker process（%d）:msg_worker_id = %d\n",pid,msg_work_id);

		//两个消息队列（设备消息和命令）同时有消息时才进行回复ACK
		if(msg_listener_count > 0 && msg_worker_count > 0)
		{
			printf("worker process(%d):进入接收。。。\n",pid);
			//接收由listener进程发送的设备信息
			ret = recv_msg(msg_lis_id,ser_send_type,buf_add);
			if(-1 == ret)
			{
				printf("worker process(%d):reveive msg(msgid:%d) error,%s\n",pid,msg_lis_id,strerror(errno));
				continue;
			}
			printf("worker process(%d):listener接收完毕。。。\n",pid);
			//接收由master进程发送的设备指令
			ret = recv_msg(msg_work_id,master_send_comm_type,buf_command);
			if(-1 == ret)
			{
				printf("worker process(%d):reveive msg error,%s\n",pid,strerror(errno));
			}



			//获取client 的 socket fd端口的套接口文件描述符
			memcpy(&fd,buf_add,sizeof(fd));
			memcpy(&clent_addr,buf_add+4,sizeof(clent_addr));
			len = sizeof(clent_addr);
			printf("worker process（%d）:clent_addr len :%d\n",pid,len);
			//取出设备上报的消息，不包含后加的socket fd和client_addr
			memcpy(buf,buf_add+20,sizeof(buf));

			memcpy(&idx,buf,sizeof(idx));
			printf("worker process %d: receive from listener process idx = %d\n",pid,idx);

			//回复ACK->标签设备 client
			printf("worker process(pid:%d), port:%d, addr:%s\n",getpid(),clent_addr.sin_port,inet_ntoa(clent_addr.sin_addr));
			memset(buf,0,sizeof(buf));

			//test
			printf("worker process(%d): recv from master command:",pid);
			for(i=0;i<10;i++)
			{
				printf(" %d",buf_command[i]);
			}
			printf("\n");
			//

			pack_ack_message(buf,idx);
			//发送信息给client，注意使用了clent_addr结构体指针
			sendto(fd, buf, BUFF_LEN, 0, (struct sockaddr*)&clent_addr, len);

			//test
			printf("worker process(%d): sednto fd=%d\n",pid,fd);
			printf("worker process(%d): sendto client:",pid);
		    for(i=0;i<10;i++)
		    {
		    	printf(" %d",buf[i]);
		    }
		    printf("\n");
			//
		}

		sleep(1);
	}

}

int pack_ack_message(char msg[],int idx)
{
	char* temp_buf;
	temp_buf = msg;

	memcpy(temp_buf,&idx,sizeof(idx));
	temp_buf += 2;
	int setFactory = 1;
	memcpy(temp_buf,&setFactory,sizeof(setFactory));
	temp_buf +=4;
	*temp_buf = 0x01;

	return 0;
}

int recv_listener_msg(void *arg)
{
	//建立消息队列:listener进程写，worker进程读取
    int msg_listen_id = get_msg_queue(_PATH_NAME_LISTEN,_PROJ_ID_LISTEN);
    if(msg_listen_id < 0)
    {
        return 1;
    }

	int ret = -1;
	char buf_add[_SIZE_+20];
	memset(buf_add,0,sizeof(buf_add));
	memcpy(buf_add,arg,sizeof(buf_add));
	while(1)
	{
		ret = recv_msg(msg_listen_id,ser_send_type,buf_add);
		if(-1 == ret)
		{
			printf("worker process(%d):reveive msg error,%s\n",getpid(),strerror(errno));

		}
		printf("woker process（%d）:msg_listen_id = %d\n",getpid(),msg_listen_id);
		sleep(5);
	}


	return 0;
}

int recv_worker_msg(void *arg)
{
    //建立消息队列:master进程写，worker进程读取
    int msg_worker_id = get_msg_queue(_PATH_NAME_WORKER,_PROJ_ID_WORKER);
    if(msg_worker_id < 0)
    {
        return 1;
    }

	int ret = -1;
	char buf_command[_SIZE_];
	memset(buf_command,0,sizeof(buf_command));
	memcpy(buf_command,arg,sizeof(buf_command));
	while(1)
	{
		ret = recv_msg(msg_worker_id,master_send_comm_type,buf_command);
		if(-1 == ret)
		{
			printf("worker process(%d):reveive msg error,%s\n",getpid(),strerror(errno));
		}
		sleep(5);
	}

	printf("woker process（%d）:msg_worker_id = %d\n",getpid(),msg_worker_id);
	return 0;
}
