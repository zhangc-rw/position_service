#include "nbiot_device.h"

int doproc_worker(int pid);
int pack_ack_message(char msg[],int idx);
int recv_listener_msg(void *arg);
int recv_worker_msg(void *arg);
