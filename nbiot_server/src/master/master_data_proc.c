#include "master_data_proc.h"
#include "msg_queue.h"

void doproc_master(command_arr *commarr,int msg_id)
{
	char buf[_SIZE_];
	int send_message_len = sizeof(command_arr);
	int i;
	int cmd = 1;
	int cmd1 = 2;
	while(1)
	{
		memset(buf,0,sizeof(buf));
		printf("main process(master): doproc_master...,msg_id:%d\n",msg_id);
		sleep(10);
		//读取等待下发指令表，更新指令数组

		memcpy(&commarr->commd[0],&cmd,sizeof(int));
		memcpy(&commarr->commd[1],&cmd1,sizeof(int));

		memcpy(buf,commarr,sizeof(command_arr));
		//使用消息队列给worker 进程发送指令数据
		send_msg(msg_id,master_send_comm_type,buf,send_message_len);
		cmd++;
		cmd1++;
		//test
		printf("master process(%d): master_send_comm_type:%d\n",getpid(),master_send_comm_type);
		printf("master process(%d): send to worker command:",getpid());
		for(i=0;i<10;i++)
		{
			printf(" %d",buf[i]);
		}
		printf("\n");
	}

}

//创建listener进程
int create_listener_process(pid_t *pid_listener,int msgid,char listener_name[],listener_proc do_listener_proc,int server_fd)
{
	printf("*pid_listener before fork: %d\n",*pid_listener);
	//产生子进程
	*pid_listener = fork();
	printf("*pid_listener after fork: %d\n",*pid_listener);
	//进入listener子进程
	if(0 == *pid_listener)
	{
		//改变子进程listener 身份为nobody
//	    setuid(geteuid());
//	    setgid(getegid());
	    //修改子进程名称为“listener_process”
		prctl(PR_SET_NAME, "listener_process");
		//保存进程pid
		sprintf(listener_name, "%d", getpid());
		SetIniKeyString("process_pid","listener_process",listener_name,PROCESS_FILE_PATH);

		//listener子进程处理业务
		do_listener_proc(msgid,server_fd);
		return 0;
	}
	return 0;
}

//创建多个worker进程
int create_worker_processes(pid_t pid_worker[],int workercount,char workername[],worker_proc do_worker_proc)
{
	int i = 0;
	char value[64];
	memset(value,0,sizeof(value));
	//进入worker子进程
	for(i = 0; i < workercount; i++ )
	{

		if(0 == (pid_worker[i]=fork()))
		{

			sprintf(workername,"worker_process%d",i);
//		    setuid(geteuid());
//		    setgid(getegid());
		    prctl(PR_SET_NAME, workername);
			memset(value, 0, sizeof(value));
			int currentPid = getpid();
			sprintf(value, "%d", currentPid);
			SetIniKeyString("process_pid",workername,value,PROCESS_FILE_PATH);
			//worker子进程处理业务
		    do_worker_proc(currentPid);
			return 0;
		}
	}
	return 0;
}

//创建单个worker进程
int create_worker_process(pid_t *pid_worker,int i,char workername[],worker_proc do_worker_proc)
{
	char value[64];
	memset(value,0,sizeof(value));
	//进入worker子进程


	if(0 == (*pid_worker=fork()))
	{

		sprintf(workername,"worker_process%d",i);
//		    setuid(geteuid());
//		    setgid(getegid());
		prctl(PR_SET_NAME, workername);
		memset(value, 0, sizeof(value));
		int currentPid = getpid();
		sprintf(value, "%d", currentPid);
		SetIniKeyString("process_pid",workername,value,PROCESS_FILE_PATH);
		//worker子进程处理业务
		do_worker_proc(currentPid);
		return 0;
	}
	return 0;
}

int get_worker_count()
{
	int itmp = 0;
	int count = 0;
	itmp = GetIniKeyInt_with1("server","maxprocess",CONFIG_FILE_PATH);
	//读取配置文件失败，默认设置为2
	if(0 == itmp)
	{
		itmp = 2;
	}
	//保持配置的worker子进程个数与开启的子进程数量一致
	//循环时开启子进程个数=2*N-1，其中N为循环次数
	count = 2*(((float)itmp + 1)/2) -1;
	return count;
}

int create_udp_socket(int *server_fd)
{
	int ret;
	struct sockaddr_in ser_addr;
	int server_port = 0;
	char* ipaddress = NULL;

	server_port = GetIniKeyInt_with1("server","port",CONFIG_FILE_PATH);
    ipaddress = GetIniKeyString_with1("server", "ip", CONFIG_FILE_PATH);
    printf("server_ip: %s, port: %d\n",ipaddress,server_port);
	if(0 == server_port)
	{
		server_port = 20111;
		printf("*get port form config failed! ,using defaul port:%d\n",server_port);
	}

	if(!strcmp(ipaddress,""))
	{
		ipaddress = "127.0.0.1";
		printf("*get server_ip form config failed! ,using defaul server_ip:%s\n",ipaddress);
	}

    //创建socket对象
    *server_fd = socket(AF_INET,SOCK_DGRAM,0);//AF_INET:IPV4; SOCK_DGRAM:UDP
    if(*server_fd < 0)
    {
    	printf("create socket fail! \n");
    	return -1;
    }

    //创建网络通信对象
    memset(&ser_addr,0,sizeof(ser_addr));
    ser_addr.sin_family =AF_INET;
    ser_addr.sin_port =htons(server_port);//IP地址，需要进行网络序转换
    ser_addr.sin_addr.s_addr=inet_addr(ipaddress);

    //绑定socket对象与通信链接
    ret =bind(*server_fd,(struct sockaddr*)&ser_addr,sizeof(ser_addr));
    if(ret < 0)
    {
        printf("listener udp socket bind failed\n");
        return -1;

    }
    printf("ser_addr.sin_port:%d\n",ser_addr.sin_port);
	return 0;
}
