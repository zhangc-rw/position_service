#pragma once
#include<stdio.h>
#include<sys/ipc.h>
#include<sys/msg.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include <sys/types.h>
#include<time.h>
#include <errno.h>
extern const  int ser_send_type;//server
extern const int cli_send_type;//client
extern const int master_send_comm_type;
extern const int worker_recv_comm_type;
#define _PATH_NAME_LISTEN "/tmp"
#define _PROJ_ID_LISTEN 0x111
#define _PATH_NAME_WORKER "/tmp"
#define _PROJ_ID_WORKER 0x101
#define _SIZE_ 1024

int create_msg_queue(char *pathname,int proj_id);
int get_msg_queue(char *pathname,int proj_id);
int comm_msg_queue(int flag,char *pathname,int proj_id);
int recv_msg(int msg_id,int type,char* out);
int send_msg(int msg_id,int type,char* in,int len);
int destroy_msg(int msg_id);

  typedef struct msgbuf
  {
       long mtype;
       char mtext[_SIZE_];
  } msg_t;
