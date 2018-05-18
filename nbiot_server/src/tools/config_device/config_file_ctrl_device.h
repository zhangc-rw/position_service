/*************************************************
 Copyright (c) 2014-2015  RongWei Company                          */
/*                 RongWei        版权所有 2014-2015  */
/*
 File name:      // CONFIG_FILE_CTRL_DEVICE.H
 Author:       Version:1.0        Date:  2014-10-22// 作者、版本及完成日期
 Description:    // 此头文件用于创建设备通用结构体。



 History:        // 修改历史记录列表，每条修改记录应包括修改日期、修改
 // 者及修改内容简述
 1. Date:2014-10-22
 Author:
 Modification:
 2. ...
 *************************************************/
#ifndef CONFIG_FILE_CTRL_DEVICE
#define CONFIG_FILE_CTRL_DEVICE
#include <pthread.h>
char *GetIniKeyString_with1(char *title,char *key,char *filename);
int SetIniKeyString(char *title,char *key,char *value,char *filename);
int SetIniKeyInt(char *title,char *key,int value,char *filename);
int GetIniKeyInt_with1(char *title,char *key,char *filename);
float GetIniKeyFloat_with1(char *title,char *key,char *filename);
int GetIniKeyInt_m(char *title,char *key,char *filename);
char *GetIniKeyString_m(char *title,char *key,char *filename);
float GetIniKeyfloat_m(char *title,char *key,char *filename);
int change_conf_value(float value, char* key, char* filename);
int config_run();
#endif
