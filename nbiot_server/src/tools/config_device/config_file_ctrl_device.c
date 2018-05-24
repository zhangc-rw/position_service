#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <time.h>
#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <stdbool.h>
#include <semaphore.h>
#include <pthread.h>
#ifdef WIN32
#include <Windows.h>
#include <stdio.h>
#else
pthread_mutex_t config_mutex;
int config_flag = 1;
#define  MAX_PATH 260

#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#endif



/*************************************************
  Function:       // GetIniKeyString
  Description:    // 读取配置文件中的字符串。
  Calls:          //
  Called By:      // 外部调用
  Input:          //
  Output:         // 无
  Return:         // int ，返回值
  Others:         //
*************************************************/
char *GetIniKeyString_with1(char *title,char *key,char *filename)
{
    FILE *fp;
    char szLine[1024];
    static char tmpstr[1024];
    int rtnval;
    int i = 0;
    int flag = 0;
    char *tmp;

    pthread_mutex_lock(&config_mutex);
    if((fp = fopen(filename, "r")) == NULL)
    {
        printf("have   no   such   file \n");
        pthread_mutex_unlock(&config_mutex);
        return "";
    }
    while(!feof(fp))
    {
        rtnval = fgetc(fp);
        if(rtnval == EOF)
        {
            break;
        }
        else
        {
            szLine[i++] = rtnval;
        }
        if(rtnval == '\n')
        {
#ifndef WIN32
//            i--;
#endif
            szLine[--i] = '\0';
            i = 0;
            tmp = strchr(szLine, '=');

            if(( tmp != NULL )&&(flag == 1))
            {
                if(strstr(szLine,key)!=NULL)
                {
                    //注释行
                    if ('#' == szLine[0])
                    {
                    }
//                    else if ( '\/' == szLine[0] && '\/' == szLine[1] )
//                    {
//
//                    }
                    else
                    {
                        //找打key对应变量
                        strcpy(tmpstr,tmp+1);
                        fclose(fp);
                        pthread_mutex_unlock(&config_mutex);
                        return tmpstr;
                    }
                }
            }
            else
            {
            	strcpy(tmpstr,"!");
            	strcat(tmpstr,"[");
            	strcat(tmpstr, title);
                strcat(tmpstr,"]");
                if( strncmp(tmpstr,szLine,strlen(tmpstr)) == 0 )
                {
                    /*找到title*/
                    flag = 1;
                }
            }
        }
    }
    fclose(fp);
    pthread_mutex_unlock(&config_mutex);
    return "";
}

/*************************************************
  Function:       // GetIniKeyString
  Description:    // 读取配置文件中的字符串。
  Calls:          //
  Called By:      // 外部调用
  Input:          //
  Output:         // 无
  Return:         // int ，返回值
  Others:         //
*************************************************/
int add_words_to_file(char *filename, char *add_position, char *add_words)
{
	char s[80];
	int size_temp;
	char *buf;
	int size_all;
	 int rtnval;
	size_all = 0;
	size_temp = 0;
	memset(s, 0, 80);
	buf = NULL;
	FILE *fp = NULL;
	if ((fp = fopen(filename, "r+")) == NULL)
	{
		printf("have   no   such   file \n");
		return -1;
	}

	/*得到文件总长度*/
	fseek(fp, 0, SEEK_END);
	size_all = ftell(fp);

	/*回到文件头*/
	fseek(fp, 0, SEEK_SET);

	/*找到欲添加的位置*/
	while (1)
	{
		memset(s, 0, 80);
	    rtnval = fgetc(fp);
	    if(rtnval == EOF)
	     break;
		fgets(s, 80, fp);

		/*对比位置*/
		if (strcmp(s, add_position) == 0)
		{
			/*位置后的字节数*/
			size_temp = size_all - ftell(fp);

			/*读入后续字节*/
			buf = malloc(size_temp * sizeof(char) + 1);
			if(buf == NULL)
			{
				printf("config_file_ctrl_device:add_words_to_file malloc failed!\n");
				return -1;
			}
			fread(buf, sizeof(char), size_temp, fp);

			/*回到欲写位置*/
			fseek(fp, 0 - size_temp, SEEK_END);

			/*写入欲添加字段*/
			fwrite(add_words, sizeof(char), strlen(add_words), fp);
			fwrite("\n", sizeof(char), strlen("\n"), fp);

			/*写入原始字段*/
			fwrite(buf, sizeof(char), size_temp, fp);

			free(buf);
			break;
		}
	}
	fclose(fp);
	return 0;
}

/*************************************************
  Function:       // UpdataIniKeyString
  Description:    // 读取配置文件中的字符串。
  Calls:          //
  Called By:      // 外部调用
  Input:          //
  Output:         // 无
  Return:         // int ，返回值
  Others:         //
*************************************************/

int UpdataIniKeyString(char *title,char *key,char *value,char *filename)
{
	FILE *fp;
	char szLine[1024];
	char s[1024];
	static char tmpstr[1024];
	int rtnval;
	int i = 0;
	int flag = 0;
	int flag_b = 0;
	int flag_key = 0;
	char *tmp;
	char tmpname[100];			//临时新文件名
	FILE* fpOri = NULL;				//指向原文件
	FILE* fpNew = NULL;
	time_t t = time(NULL);
	int rand_d = 0;
	if ((fp = fopen(filename, "a+")) == NULL)
	{
		printf("have   no   such   file \n");
		return -1;
	}
	while (!feof(fp))
	{
		rtnval = fgetc(fp);
		if (rtnval == EOF)
		{
			if (!flag)
			{
				memset(tmpstr, 0, 1024);
				//strcpy(tmpstr, "\n");
				strcpy(tmpstr, "!");
				strcat(tmpstr, "[");
				strcat(tmpstr, title);
				strcat(tmpstr, "]");
				strcat(tmpstr, "\n");
				fprintf(fp, "%s", tmpstr);
				flag = 1;
			}
			if (flag && !flag_key)
			{
				fclose(fp);
				return 1;
			}
			break;
		}
		else
		{
			szLine[i++] = rtnval;
		}
		if (rtnval == '\n')
		{
#ifndef WIN32
//            i--;
#endif
			szLine[--i] = '\0';
			i = 0;
			tmp = strchr(szLine, '=');

			if ((tmp != NULL) && (flag == 1))
			{
				if (strstr(szLine, key) != NULL)
				{
					//注释行
					if ('#' == szLine[0])
					{

					}
					else
					{
						fclose(fp);
						//找打key对应变量

						//打开原文件
						fpOri = fopen(filename, "r");
						if (fpOri == NULL)
						{
							printf("Error: Cannot open original file!\n");
							return -1;
						}

						//生成新文件名并打开临时新文件
						//tmpname = "rader1_config.cfg";
						rand_d = 1 + (int) (99999.0 * rand() / (RAND_MAX + 1.0)); //表示生成的随机数在0~360范围内
				    	sprintf(tmpname,"%s_%d_%d.cfg",filename,t,rand_d);

						fpNew = fopen(tmpname, "w");
						if (fpNew == NULL)
						{
							fclose(fpOri);
							printf("Error: Cannot open tmp file!\n");
							return -1;
						}
						memset(s, 0, 1024);
						while (1)
						{

							//
							memset(tmpstr, 0, 1024);
							rtnval = fgetc(fpOri);
							if (rtnval == EOF)
							{
								break;
							}
							else
							{
								s[i++] = rtnval;
							}
							if (rtnval == '\n')
							{
								s[--i] = '\0';
								i = 0;
								tmp = strchr(s, '=');
								if (tmp == NULL)
								{
									strcpy(tmpstr, "!");
									strcat(tmpstr, "[");
									strcat(tmpstr, title);
									strcat(tmpstr, "]");
									if (strncmp(tmpstr, s, strlen(tmpstr)) == 0)
									{
										/*找到title*/
										flag_b = 1;
									}
								}
								/*对比位置*/
								if ((strcmp(s, szLine) == 0) && flag_b)
								{
									strcpy(tmpstr, "!");
									strcat(tmpstr, key);
									strcat(tmpstr, "=");
									strcat(tmpstr, value);
									strcat(tmpstr, "\n");
									fputs(tmpstr, fpNew);
								}
								else
								{
									strcpy(tmpstr, s);
									strcat(tmpstr, "\n");
									fputs(tmpstr, fpNew);
								}
							}

						}
						fclose(fpOri);
						fclose(fpNew);

						remove(filename);				//删除原文件
						rename(tmpname, filename);		//重命名新文件
						flag_key = 1;
						return 0;
					}
				}
			}
				else
				{
					strcpy(tmpstr, "!");
					strcat(tmpstr, "[");
					strcat(tmpstr, title);
					strcat(tmpstr, "]");
					if (strncmp(tmpstr, szLine, strlen(tmpstr)) == 0)
					{
						/*找到title*/
						flag = 1;
					}
				}

		}
	}
		fclose(fp);
		return 0;
}
/*************************************************
  Function:       // SetIniKeyString
  Description:    // 读取配置文件中的字符串。
  Calls:          //
  Called By:      // 外部调用
  Input:          //
  Output:         // 无
  Return:         // int ，返回值
  Others:         //
*************************************************/
int SetIniKeyString(char *title,char *key,char *value,char *filename)
{
	char add_position[1024];
	char add_words[1024];
	memset(add_position, 0, 1024);
	memset(add_words, 0, 1024);
	pthread_mutex_lock(&config_mutex);
	int rt_value = UpdataIniKeyString(title, key,value, filename);
	if(rt_value > 0)
	{
		//strcpy(add_position, "!");
		strcpy(add_position, "[");
		strcat(add_position, title);
		strcat(add_position, "]");
		strcat(add_position, "\n");

		strcpy(add_words, "!");
		strcat(add_words, key);
		strcat(add_words, "=");
		strcat(add_words, value);
		rt_value =  add_words_to_file(filename, add_position, add_words);
		//rt_value = 0;
	}
	pthread_mutex_unlock(&config_mutex);
	return rt_value;
}
/*************************************************
  Function:       // SetIniKeyInt_log
  Description:    // 读取配置文件中的字符串。
  Calls:          //
  Called By:      // 外部调用
  Input:          //
  Output:         // 无
  Return:         // int ，返回值
  Others:         //
*************************************************/
int SetIniKeyInt(char *title,char *key,int value,char *filename)
{
	char log_value_str[64];
	memset(log_value_str, 0, sizeof(log_value_str));

	sprintf(log_value_str, "%d", value);

	return SetIniKeyString(title, key, log_value_str, filename);
}
/*************************************************
  Function:       // GetIniKeyInt
  Description:    // 读取配置文件中的整形。
  Calls:          //
  Called By:      // 外部调用
  Input:          //
  Output:         // 无
  Return:         // int ，返回值
  Others:         //
*************************************************/

int GetIniKeyInt_with1(char *title,char *key,char *filename)
{
    return atoi(GetIniKeyString_with1(title,key,filename));
}
float GetIniKeyFloat_with1(char *title,char *key,char *filename)
{
	float f;
	f = atof(GetIniKeyString_with1(title,key,filename));
    return f;
}
//int SetIniKeyString(char *title,char *key,char *value,char *filename)
//{
//    FILE *fp;
//    char szLine[1024];
//    static char tmpstr[1024];
//    int rtnval;
//    int i = 0;
//    int flag = 0;
//    int flag_key = 0;
//    char *tmp;
//
//    if((fp = fopen(filename, "a+")) == NULL)
//    {
//        printf("have   no   such   file \n");
//        return 1;
//    }
//    while(!feof(fp))
//    {
//        rtnval = fgetc(fp);
//        if(rtnval == EOF)
//        {
//            if(!flag)
//            {
//    			memset(tmpstr, 0, 1024);
//    			//strcpy(tmpstr, "\n");
//    			strcpy(tmpstr, "!");
//    			strcat(tmpstr, "[");
//    			strcat(tmpstr, title);
//    			strcat(tmpstr, "]");
//    			strcat(tmpstr, "\n");
//                fprintf(fp,"%s",tmpstr);
//                flag = 1;
//            }
//            if(flag && !flag_key)
//            {
//            	fclose(fp);
//            	return 2;
//            }
//            break;
//        }
//        else
//        {
//            szLine[i++] = rtnval;
//        }
//        if(rtnval == '\n')
//        {
//#ifndef WIN32
////            i--;
//#endif
//            szLine[--i] = '\0';
//            i = 0;
//            tmp = strchr(szLine, '=');
//
//            if(( tmp != NULL )&&(flag == 1))
//            {
//                if(strstr(szLine,key)!=NULL)
//                {
//                    //注释行
//                    if ('#' == szLine[0])
//                    {
//                    }
////                    else if ( '\/' == szLine[0] && '\/' == szLine[1] )
////                    {
////
////                    }
//                    else
//                    {
//                        //找打key对应变量
//                        strcpy(tmpstr,tmp+1);
//                        flag_key = 1;
//                        fclose(fp);
//                        return 0;
//                    }
//                }
//            }
//            else
//            {
//                strcpy(tmpstr,"!");
//                strcat(tmpstr,"[");
//                strcat(tmpstr,title);
//                strcat(tmpstr,"]");
//                if( strncmp(tmpstr,szLine,strlen(tmpstr)) == 0 )
//                {
//                    /*找到title*/
//                    flag = 1;
//                }
//            }
//
//        }
//
//    }
//    fclose(fp);
//    return 0;
//}
/*************************************************
  Function:       // GetIniKeyString
  Description:    // 读取配置文件中的字符串。
  Calls:          //
  Called By:      // 外部调用
  Input:          //
  Output:         // 无
  Return:         // int ，返回值
  Others:         //
*************************************************/
char *GetIniKeyString_m(char *title,char *key,char *filename)
{
    FILE *fp;
    char szLine[1024];
    static char tmpstr[1024];
    int rtnval;
    int i = 0;
    int flag = 0;
    char *tmp;

    pthread_mutex_lock(&config_mutex);
    if((fp = fopen(filename, "r")) == NULL)
    {
        printf("have   no   such   file \n");
        pthread_mutex_unlock(&config_mutex);
        return "";
    }
    while(!feof(fp))
    {
        rtnval = fgetc(fp);
        if(rtnval == EOF)
        {
            break;
        }
        else
        {
            szLine[i++] = rtnval;
        }
        if(rtnval == '\n')
        {
#ifndef WIN32
//            i--;
#endif
            szLine[--i] = '\0';
            i = 0;
            tmp = strchr(szLine, '=');

            if(( tmp != NULL )&&(flag == 1))
            {
                if(strstr(szLine,key)!=NULL)
                {
                    //注释行
                    if ('#' == szLine[0])
                    {
                    }
//                    else if ( '\/' == szLine[0] && '\/' == szLine[1] )
//                    {
//
//                    }
                    else
                    {
                        //找打key对应变量
                        strcpy(tmpstr,tmp+1);
                        fclose(fp);
                        pthread_mutex_unlock(&config_mutex);
                        return tmpstr;
                    }
                }
            }
            else
            {
                strcpy(tmpstr,"[");
                strcat(tmpstr,title);
                strcat(tmpstr,"]");
                if( strncmp(tmpstr,szLine,strlen(tmpstr)) == 0 )
                {
                    /*找到title*/
                    flag = 1;
                }
            }
        }
    }
    pthread_mutex_unlock(&config_mutex);
    fclose(fp);
    return "";
}

/*************************************************
  Function:       // GetIniKeyInt
  Description:    // 读取配置文件中的整形。
  Calls:          //
  Called By:      // 外部调用
  Input:          //
  Output:         // 无
  Return:         // int ，返回值
  Others:         //
*************************************************/

int GetIniKeyInt_m(char *title,char *key,char *filename)
{
    return atoi(GetIniKeyString_m(title,key,filename));
}
float GetIniKeyfloat_m(char *title,char *key,char *filename)
{
	float a = 0;
	a = atof(GetIniKeyString_m(title,key,filename));
    return a;
}

/*************************************************
  Function:       // change_conf_value
  Description:    // 修改配置文件中的值
  Calls:          //
  Called By:      // 外部调用
  Input:          //
  Output:         // 无
  Return:         // int ，返回值
  Others:         //
*************************************************/
int change_conf_value(float value, char* key, char* filename)
{
	FILE *fp;
	char read_char[256];
	int p_len = 0;
	int char_len;
	char* p = NULL;
	char temp_value_char[16];
	char temp_char[256];
	int temp_len;

	memset(read_char, 0, 256);
	memset(temp_char, 0, 256);
	memset(temp_value_char, 0, 16);

	sprintf(temp_char, "%s%s", key, "=");
	sprintf(temp_value_char, "%.4f", value);
	temp_len = strlen(temp_value_char);
//	printf("value len = %d\n", temp_len);
//	printf("temp_value_char = %s\n", temp_value_char);
//	printf("temp_char = %s\n", temp_char);

	fp=fopen(filename, "rb+"); //使用rb+模式,可以往半中间插入数据,而且是覆盖插入,若使用"ab+"每次都插入到最后面,调用fseek也没用

	while(1)
	{
		memset(read_char,0,256);
		if(fgets(read_char, 256, fp)==NULL)
		{
//			printf("Mission Compele!\n");
			break;
		}
		/*查找需要的字段*/
		p = strstr(read_char, temp_char);
		if (p == NULL)
		{
			p_len += strlen(read_char);
		}
		else
		{
			char_len = strlen(temp_char);
			p_len += char_len;
//			printf("len = %d\n", p_len);
			break;
		}
	}

	if(p != NULL)
	{
		if(NULL != fp)
		{
			if(-1 == (fseek(fp, p_len, SEEK_SET)))
			{
				printf("seek error\n");
			}
			fwrite(temp_value_char, 1, temp_len, fp);
			fclose(fp);
		}
		else
		{
			printf("fopen error\n");
			return 1;
		}
	}
	else
	{
		fclose(fp);
	}

	return 0;
}
int config_run()
{
    if(config_flag)
    {
    	int ini = 0;
		ini = pthread_mutex_init(&(config_mutex), NULL);
		if(ini != 0)
		{
			return -1;
		}
		config_flag = ini;
    }
    return 0;
}
