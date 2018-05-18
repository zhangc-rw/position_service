#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/prctl.h>
#include <stdlib.h>

int main(void)
{
	pid_t childpid1, childpid2, childpid3;
	int status;
	int num;

	/* 这里不可以一下就创建完子进程，要用
	*要 创建-》判断-》使用-》return or exit.更不能这样如test2.c
	*childpid1 = fork();
	*childpid2 = fork();
	*childpid3 = fork();
	*/
	childpid1 = fork();												//创建
	if(0 == childpid1)												//判断
	{															   //进入

		//prctl(PR_SET_NAME, "worker_process1", NULL, NULL, NULL);
		prctl(PR_SET_NAME, "worker_process1");
		while(1)
		{
			printf("In child1 process\n");
			printf("\tchild pid = %d\n", getpid());
			sleep(1);
		}
		exit(EXIT_SUCCESS);											//退出
	}
	childpid2 = fork();
	if(0 == childpid2)
	{
		//prctl(PR_SET_NAME, "worker_process2", NULL, NULL, NULL);
		prctl(PR_SET_NAME, "worker_process2");
		while(1)
		{
			printf("In child2 processd\n");
			printf("\tchild pid = %d\n", getpid());
			sleep(1);
		}
		exit(EXIT_SUCCESS);
	}
	childpid3 = fork();
	if(0 == childpid3)
	{
		//prctl(PR_SET_NAME, "worker_process3", NULL, NULL, NULL);
		prctl(PR_SET_NAME, "worker_process3");
		while(1)
		{
			printf("In child3 process\n");
			printf("\tchild pid = %d\n", getpid());
			sleep(1);
		}
		exit(EXIT_SUCCESS);
	}
	//这里不可以用wait(NULL)，多个子进程是不可以用wait来等待的，它只会等待一个 其它都成僵尸了
	waitpid(childpid1, NULL, 0);
	waitpid(childpid2, NULL, 0);
	waitpid(childpid3, NULL, 0);
	puts("in parent");

	exit(EXIT_SUCCESS);

}
