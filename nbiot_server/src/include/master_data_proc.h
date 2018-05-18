#include<stdio.h>
#include <unistd.h>
#include <sys/prctl.h>
#include "nbiot_device.h"
#include "config_file_ctrl_device.h"
#define LISTENER_SO_PATH "../lib/lib_listener_proc.so"
#define WORKER_SO_PATH "../lib/lib_worker_proc.so"






void doproc_master(command_arr *commarr,int msg_id);
typedef int (*listener_proc)();
typedef int (*worker_proc)();
void process_restart(int sign);
int create_listener_process(pid_t *pid_listener,int msgid,char listener_name[],listener_proc do_listener_proc,int server_fd);
int create_worker_processes(pid_t pid_worker[],int workercount,char workername[],worker_proc do_worker_proc);
int create_worker_process(pid_t *pid_worker,int i,char workername[],worker_proc do_worker_proc);
int get_worker_count();
int create_udp_socket(int *server_fd);
