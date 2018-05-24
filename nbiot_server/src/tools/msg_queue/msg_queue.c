#include "msg_queue.h"
 const int ser_send_type=1;//server
 const int cli_send_type=2;//client
 const int master_send_comm_type = 3;
 int comm_msg_queue(int flag,char *pathname,int proj_id)
 {

	  key_t key = ftok(pathname,proj_id);
	  if(key == -1)
	  {
		   perror("ftok");
		   return -2;
	  }
	  int msg_id=msgget(key,flag);
      if(msg_id<0)
          perror("msgget");
      return msg_id;
}
int create_msg_queue(char *pathname,int proj_id)
{
      //int flag=IPC_CREAT|IPC_EXCL|0666;
	 int flag=IPC_CREAT|0666;
     return comm_msg_queue(flag,pathname,proj_id);
 }
 int get_msg_queue(char *pathname,int proj_id)
 {
     int flag=IPC_CREAT;
     return comm_msg_queue(flag,pathname,proj_id);
}

int recv_msg(int msg_id,int type,char* out)
{
    msg_t msg;
    memset(&msg,0,sizeof(msg));
    msg.mtype=type;
    size_t ret=msgrcv(msg_id,&msg,sizeof(msg.mtext),type,0);
    //size_t ret=msgrcv(msg_id,&msg,sizeof(msg.mtext),type,IPC_NOWAIT);
    if(ret<0)
    {
         perror("msgrcv");
         return 1;
    }
    //strcpy(out,msg.mtext);
    memcpy(out,msg.mtext,sizeof(msg.mtext));
    return 0;
}
int send_msg(int msg_id,int type,char* msg_in,int len)
{
     msg_t msg;
     memset(&msg,0,sizeof(msg));
     msg.mtype=type;
     //strncpy(msg.mtext,msg_in, strlen(msg_in)+1);
     memcpy(msg.mtext,msg_in,len);

     size_t  ret=msgsnd(msg_id,&msg,sizeof(msg.mtext),0);
     if(ret<0)
     {
          perror("msgsnd");
               return 2;
     }
      return 0;
 }
 int destroy_msg(int msg_id)
 {
	 int ret = msgctl(msg_id, IPC_RMID, NULL);

      if(ret == -1)
      {
          fprintf(stderr, "msgctl(IPC_RMID) failed\n");
      }
      return ret;
 }
