#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/prctl.h>
#include <stdlib.h>
#include <unistd.h>
#include <dlfcn.h>
#include "listener_data_proc.h"
#include "master_data_proc.h"
#include "worker_data_proc.h"
#include "config_file_ctrl_device.h"
#include "msg_queue.h"
//#include "inirw.h"


#define MAX_WORKER_COUNT 4

pid_t pid_listener;
pid_t pid_worker[MAX_WORKER_COUNT];
int worker_count = 0;
int msg_listen_id;
int msg_worker_id;
char worker_arg[MAX_WORKER_COUNT];
int server_fd;

listener_proc do_listener_proc;
worker_proc do_worker_proc;

command_arr commandArr;

int main(int argc, char* argv[])
{
	char worker_name[64];
	char value[64];
	void* handle_listener = NULL;
	void* handle_worker = NULL;

	memset(pid_worker,0,sizeof(pid_worker));
	memset(worker_name,0,sizeof(worker_name));
	memset(value, 0, sizeof(value));
	memset(&commandArr,0,sizeof(commandArr));

	//获取最大worker子进程个数
	worker_count = get_worker_count();
	printf("worker_count = %d\n",worker_count);

	/*初始化listener子进程处理业务动态库
	 * dlopen 失败 返回0；打开失败--循环打开--直到成功为止*/
	while (!handle_listener)
	{
		handle_listener = dlopen(LISTENER_SO_PATH, RTLD_NOW);
		if(!handle_listener)
		{
			fprintf(stderr, "打开listener子进程处理业务动态库错误: %s\n", dlerror());
		}
	}
	//初始化listener子进程处理业务动态库
	while (!handle_worker)
	{
		handle_worker = dlopen(WORKER_SO_PATH, RTLD_NOW);
		if(!handle_worker)
		{
			fprintf(stderr, "打开worker子进程处理业务动态库错误: %s\n", dlerror());
		}
	}
	printf("初始化listener/worker子进程处理业务动态库成功！\n");
	//动态库函数绑定
	//listener进程处理函数
	do_listener_proc = (listener_proc)dlsym(handle_listener,"doproc_listener");
	//worker进程处理函数
	do_worker_proc = (worker_proc)dlsym(handle_worker,"doproc_worker");

	//创建消息队列:listener进程写，worker进程读取
	msg_listen_id = create_msg_queue(_PATH_NAME_LISTEN,_PROJ_ID_LISTEN);
	//创建消息队列:master进程写，worker进程读取
	msg_worker_id = create_msg_queue(_PATH_NAME_WORKER,_PROJ_ID_WORKER);

	//注册listener和worker进程重启消息
	signal(SIGCHLD,process_restart);

	//创建socket用于listener进程监听，worker进程回复设备
	create_udp_socket(&server_fd);

	//创建listener进程
	create_listener_process(&pid_listener,msg_listen_id,value,do_listener_proc,server_fd);
	//创建多个worker进程，个数为worker_count
	create_worker_processes(pid_worker,worker_count,worker_name,do_worker_proc);

	//master进程处理业务
	doproc_master(&commandArr,msg_worker_id);

	//删除消息队列
	destroy_msg(msg_listen_id);
	destroy_msg(msg_worker_id);

	close(server_fd);
	return 0;
}

void process_restart(int sign)
{
	pid_t pid;
	int i = 0;
	char temp_name[64];
	char value[64];
	int stat;
	pid = wait(&stat);

	memset(temp_name,0,sizeof(temp_name));
	memset(value,0,sizeof(value));

	printf("sig_restart pid = %d\n",pid);
	printf("worker_count = %d\n",worker_count);
	printf("pid_listener = %d\n",pid_listener);

	if(pid == pid_listener)
	{
		create_listener_process(&pid_listener,msg_listen_id,value,do_listener_proc,server_fd);
	}

	for(i = 0; i < worker_count; i++)
	{
		if(pid == pid_worker[i])
		{
			create_worker_process( &pid_worker[i],i,temp_name,do_worker_proc);
		}
	}
}
