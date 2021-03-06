#include "StdAfx.h"
#include "DisToPos.h"
#include <windows.h>
#include "dis_to_pos_matlab.h"
#include <math.h>





CDisToPos::CDisToPos(void)
{
	m_IfInit = 0;
	m_AnchorCount = 0;
	memset(m_AnchorPosList, 0, sizeof(POSITION_3D) * MAX_ANCHOR);
}


CDisToPos::~CDisToPos(void)
{
	//判断是否初始化
	if (m_IfInit != 0)
	{
		dis_to_pos_matlabTerminate();
		m_IfInit = 0;
	}
}

// 初始化配置
int CDisToPos::Init()
{
	int my_temp = 0;

	//判断是否初始化
	if (m_IfInit == 1)
	{
		return 0;
	}

	my_temp = UpdateAnchorPos();
	if (my_temp != 0)
	{
		return my_temp;
	}

	my_temp = dis_to_pos_matlabInitialize();
	if (my_temp == 0)
	{
		return 1;
	}

	m_IfInit = 1;
	return 0;
}




// 设置基站位置
int CDisToPos::SetAnchorPos(int index, POSITION_3D pos)
{
	int my_temp = 0;
	char temp_anchor_name[128] = {0};
	char temp_anchor_pos[128] = {0};
	TCHAR temp_anchor_name_T[128] = {0};
	TCHAR temp_anchor_pos_T[128] = {0};

	//判断是否初始化
	if (m_IfInit == 0)
	{
		return ERROR_NOT_INIT;
	}
	//更新基站信息
	my_temp = UpdateAnchorPos();
	if (my_temp != 0)
	{
		return my_temp;
	}

	//如果index不在count范围，返回错误
	if (index < 0 || index > m_AnchorCount)
	{
		return ERROR_INDEX_NOT_RANGE;
	}

	//更改配置文件相关配置
	sprintf_s(temp_anchor_name, "A_%d_X", index);
	CharToTchar(temp_anchor_name, temp_anchor_name_T);
	sprintf_s(temp_anchor_pos, "%f", pos.x);
	CharToTchar(temp_anchor_pos, temp_anchor_pos_T);
	WritePrivateProfileString(TEXT("Anchor_Pos"), temp_anchor_name_T, temp_anchor_pos_T, _TEXT(TRANS_CONF_FILE_PATH)); 

	sprintf_s(temp_anchor_name, "A_%d_Y", index);
	CharToTchar(temp_anchor_name, temp_anchor_name_T);
	sprintf_s(temp_anchor_pos, "%f", pos.y);
	CharToTchar(temp_anchor_pos, temp_anchor_pos_T);
	WritePrivateProfileString(TEXT("Anchor_Pos"), temp_anchor_name_T, temp_anchor_pos_T, _TEXT(TRANS_CONF_FILE_PATH)); 

	sprintf_s(temp_anchor_name, "A_%d_Z", index);
	CharToTchar(temp_anchor_name, temp_anchor_name_T);
	sprintf_s(temp_anchor_pos, "%f", pos.z);
	CharToTchar(temp_anchor_pos, temp_anchor_pos_T);
	WritePrivateProfileString(TEXT("Anchor_Pos"), temp_anchor_name_T, temp_anchor_pos_T, _TEXT(TRANS_CONF_FILE_PATH));  

	//存入内存
	m_AnchorPosList[index].x = pos.x;
	m_AnchorPosList[index].y = pos.y;
	m_AnchorPosList[index].z = pos.z;

	return 0;
}


//执行根据距离计算坐标
int CDisToPos::DoDisToPos(int dis_count, double *dis_list, POSITION_3D *pos)
{
	//定义mwArray类型变量，用于存放矩阵
	mwArray x1(1,1,mxDOUBLE_CLASS);
	mwArray x2(1,1,mxDOUBLE_CLASS);
	mwArray x3(1,1,mxDOUBLE_CLASS);
	mwArray x4(1,1,mxDOUBLE_CLASS);
	mwArray x5(1,1,mxDOUBLE_CLASS);
	mwArray x6(1,1,mxDOUBLE_CLASS);
	mwArray x7(1,1,mxDOUBLE_CLASS);
	mwArray x8(1,1,mxDOUBLE_CLASS);
	mwArray x9(1,1,mxDOUBLE_CLASS);
	mwArray x10(1,1,mxDOUBLE_CLASS);
	mwArray x11(1,1,mxDOUBLE_CLASS);
	mwArray x12(1,1,mxDOUBLE_CLASS);
	mwArray da(1,1,mxDOUBLE_CLASS);
	mwArray db(1,1,mxDOUBLE_CLASS);
	mwArray dc(1,1,mxDOUBLE_CLASS);
	mwArray dd(1,1,mxDOUBLE_CLASS);
	mwArray xyz(3,1,mxDOUBLE_CLASS);

	double nu1[] = {m_AnchorPosList[0].x};
	double nu2[] = {m_AnchorPosList[0].y};
	double nu3[] = {m_AnchorPosList[0].z};
	double nu4[] = {m_AnchorPosList[1].x};
	double nu5[] = {m_AnchorPosList[1].y};
	double nu6[] = {m_AnchorPosList[1].z};
	double nu7[] = {m_AnchorPosList[2].x};
	double nu8[] = {m_AnchorPosList[2].y};
	double nu9[] = {m_AnchorPosList[2].z};
	double nu10[] = {m_AnchorPosList[3].x};
	double nu11[] = {m_AnchorPosList[3].y};
	double nu12[] = {m_AnchorPosList[3].z};
	double nuda[] = {dis_list[0]};
	double nudb[] = {dis_list[1]};
	double nudc[] = {dis_list[2]};
	double nudd[] = {dis_list[3]};

	//判断是否初始化
	if (m_IfInit == 0)
	{
		return ERROR_NOT_INIT;
	}

	//判断是不是4个，不是暂时不支持
	if (dis_count != 4 || m_AnchorCount != 4)
	{
		return ERROR_ANCHOR_COUNT;
	}

	//给输入 mxArray 对象赋值
	x1.SetData(nu1,1);
	x2.SetData(nu2,1);
	x3.SetData(nu3,1);
	x4.SetData(nu4,1);
	x5.SetData(nu5,1);
	x6.SetData(nu6,1);
	x7.SetData(nu7,1);
	x8.SetData(nu8,1);
	x9.SetData(nu9,1);
	x10.SetData(nu10,1);
	x11.SetData(nu11,1);
	x12.SetData(nu12,1);
	da.SetData(nuda,1);
	db.SetData(nudb,1);
	dc.SetData(nudc,1);
	dd.SetData(nudd,1);

	//调用DLL函数
	dis_to_pos_matlab(1,xyz,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,da,db,dc,dd);
	
	//判断执行是否出错（输出是否为非数NAN）
	if (!(_finite(xyz.Get(1,1))))
	{
		return ERROR_TRANS_WRONG;
	}

	pos->x = xyz.Get(1,1);
	pos->y = xyz.Get(1,2);
	pos->z = xyz.Get(1,3);

	return 0;
}



// 更新基站信息
int CDisToPos::UpdateAnchorPos()
{
	int count = 0;
	int i = 0;
	char temp_anchor_name[128] = {0};
	char temp_anchor_pos[128] = {0};
	TCHAR temp_anchor_name_T[128] = {0};
	TCHAR temp_anchor_pos_T[128] = {0};

	//重新读取配置文件信息
	count = GetPrivateProfileInt(_TEXT("Anchor_Pos"), _TEXT("Count") ,0, _TEXT(TRANS_CONF_FILE_PATH));

	if (count == 0)
	{
		//如果没有配置则输入默认个数和坐标
		WritePrivateProfileString(TEXT("Anchor_Pos"), TEXT("Count"), TEXT(DEFULT_ANCHOR_COUNT), _TEXT(TRANS_CONF_FILE_PATH));  

		WritePrivateProfileString(TEXT("Anchor_Pos"), TEXT("A_0_X"), TEXT(DEFULT_ANCHOR_POSITION_X), _TEXT(TRANS_CONF_FILE_PATH));  
		WritePrivateProfileString(TEXT("Anchor_Pos"), TEXT("A_0_Y"), TEXT(DEFULT_ANCHOR_POSITION_Y), _TEXT(TRANS_CONF_FILE_PATH));  
		WritePrivateProfileString(TEXT("Anchor_Pos"), TEXT("A_0_Z"), TEXT(DEFULT_ANCHOR_POSITION_Z), _TEXT(TRANS_CONF_FILE_PATH));

		WritePrivateProfileString(TEXT("Anchor_Pos"), TEXT("A_1_X"), TEXT(DEFULT_ANCHOR_POSITION_X), _TEXT(TRANS_CONF_FILE_PATH));
		WritePrivateProfileString(TEXT("Anchor_Pos"), TEXT("A_1_Y"), TEXT(DEFULT_ANCHOR_POSITION_Y), _TEXT(TRANS_CONF_FILE_PATH));  
		WritePrivateProfileString(TEXT("Anchor_Pos"), TEXT("A_1_Z"), TEXT(DEFULT_ANCHOR_POSITION_Z), _TEXT(TRANS_CONF_FILE_PATH)); 

		WritePrivateProfileString(TEXT("Anchor_Pos"), TEXT("A_2_X"), TEXT(DEFULT_ANCHOR_POSITION_X), _TEXT(TRANS_CONF_FILE_PATH));  
		WritePrivateProfileString(TEXT("Anchor_Pos"), TEXT("A_2_Y"), TEXT(DEFULT_ANCHOR_POSITION_Y), _TEXT(TRANS_CONF_FILE_PATH));  
		WritePrivateProfileString(TEXT("Anchor_Pos"), TEXT("A_2_Z"), TEXT(DEFULT_ANCHOR_POSITION_Z), _TEXT(TRANS_CONF_FILE_PATH)); 

		WritePrivateProfileString(TEXT("Anchor_Pos"), TEXT("A_3_X"), TEXT(DEFULT_ANCHOR_POSITION_X), _TEXT(TRANS_CONF_FILE_PATH));
		WritePrivateProfileString(TEXT("Anchor_Pos"), TEXT("A_3_Y"), TEXT(DEFULT_ANCHOR_POSITION_Y), _TEXT(TRANS_CONF_FILE_PATH));  
		WritePrivateProfileString(TEXT("Anchor_Pos"), TEXT("A_3_Z"), TEXT(DEFULT_ANCHOR_POSITION_Z), _TEXT(TRANS_CONF_FILE_PATH)); 

		m_AnchorCount = atoi(DEFULT_ANCHOR_COUNT);
		for (i = 0; i < m_AnchorCount; i++)
		{
			//分别获取XYZ的坐标
			sprintf_s(temp_anchor_name, "A_%d_X", i);
			CharToTchar(temp_anchor_name, temp_anchor_name_T);
			GetPrivateProfileString(TEXT("Anchor_Pos"), temp_anchor_name_T, _TEXT("NA"), temp_anchor_pos_T, 128, _TEXT(TRANS_CONF_FILE_PATH));
			if (_tcscmp(temp_anchor_pos_T, _TEXT("NA")) == 0)
			{
				//未配置相应数据
				return ERROR_ANCHOR_POS_NOT_FOUND;
			}
			TcharToChar(temp_anchor_pos_T, temp_anchor_pos);
			m_AnchorPosList[i].x = atof(temp_anchor_pos);

			sprintf_s(temp_anchor_name, "A_%d_Y", i);
			CharToTchar(temp_anchor_name, temp_anchor_name_T);
			GetPrivateProfileString(TEXT("Anchor_Pos"), temp_anchor_name_T, _TEXT("NA"), temp_anchor_pos_T, 128, _TEXT(TRANS_CONF_FILE_PATH));
			if (_tcscmp(temp_anchor_pos_T, _TEXT("NA")) == 0)
			{
				//未配置相应数据
				return ERROR_ANCHOR_POS_NOT_FOUND;
			}
			TcharToChar(temp_anchor_pos_T, temp_anchor_pos);
			m_AnchorPosList[i].y = atof(temp_anchor_pos);

			sprintf_s(temp_anchor_name, "A_%d_Z", i);
			CharToTchar(temp_anchor_name, temp_anchor_name_T);
			GetPrivateProfileString(TEXT("Anchor_Pos"), temp_anchor_name_T, _TEXT("NA"), temp_anchor_pos_T, 128, _TEXT(TRANS_CONF_FILE_PATH));
			if (_tcscmp(temp_anchor_pos_T, _TEXT("NA")) == 0)
			{
				//未配置相应数据
				return ERROR_ANCHOR_POS_NOT_FOUND;
			}
			TcharToChar(temp_anchor_pos_T, temp_anchor_pos);
			m_AnchorPosList[i].z = atof(temp_anchor_pos);
		}
	}
	else
	{
		//将读取的基站位置放入内存
		m_AnchorCount = count;
		for (i = 0; i < m_AnchorCount; i++)
		{
			//分别获取XYZ的坐标
			sprintf_s(temp_anchor_name, "A_%d_X", i);
			CharToTchar(temp_anchor_name, temp_anchor_name_T);
			GetPrivateProfileString(TEXT("Anchor_Pos"), temp_anchor_name_T, _TEXT("NA"), temp_anchor_pos_T, 128, _TEXT(TRANS_CONF_FILE_PATH));
			if (_tcscmp(temp_anchor_pos_T, _TEXT("NA")) == 0)
			{
				//未配置相应数据
				return ERROR_ANCHOR_POS_NOT_FOUND;
			}
			TcharToChar(temp_anchor_pos_T, temp_anchor_pos);
			m_AnchorPosList[i].x = atof(temp_anchor_pos);

			sprintf_s(temp_anchor_name, "A_%d_Y", i);
			CharToTchar(temp_anchor_name, temp_anchor_name_T);
			GetPrivateProfileString(TEXT("Anchor_Pos"), temp_anchor_name_T, _TEXT("NA"), temp_anchor_pos_T, 128, _TEXT(TRANS_CONF_FILE_PATH));
			if (_tcscmp(temp_anchor_pos_T, _TEXT("NA")) == 0)
			{
				//未配置相应数据
				return ERROR_ANCHOR_POS_NOT_FOUND;
			}
			TcharToChar(temp_anchor_pos_T, temp_anchor_pos);
			m_AnchorPosList[i].y = atof(temp_anchor_pos);

			sprintf_s(temp_anchor_name, "A_%d_Z", i);
			CharToTchar(temp_anchor_name, temp_anchor_name_T);
			GetPrivateProfileString(TEXT("Anchor_Pos"), temp_anchor_name_T, _TEXT("NA"), temp_anchor_pos_T, 128, _TEXT(TRANS_CONF_FILE_PATH));
			if (_tcscmp(temp_anchor_pos_T, _TEXT("NA")) == 0)
			{
				//未配置相应数据
				return ERROR_ANCHOR_POS_NOT_FOUND;
			}
			TcharToChar(temp_anchor_pos_T, temp_anchor_pos);
			m_AnchorPosList[i].z = atof(temp_anchor_pos);
		}
	}
	return 0;
}

// 更改基站数量
int CDisToPos::SetAnchorCount(int count)
{
	int my_temp = 0;
	char temp_anchor_count[128] = {0};
	TCHAR temp_anchor_count_T[128] = {0};

	//判断是否初始化
	if (m_IfInit == 0)
	{
		return ERROR_NOT_INIT;
	}

	//更新基站信息
	my_temp = UpdateAnchorPos();
	if (my_temp != 0)
	{
		return my_temp;
	}

	//更改配置和内存变量
	sprintf_s(temp_anchor_count, "%d", count);
	CharToTchar(temp_anchor_count, temp_anchor_count_T);
	WritePrivateProfileString(TEXT("Anchor_Pos"), _TEXT("Count"), temp_anchor_count_T, _TEXT(TRANS_CONF_FILE_PATH)); 

	return 0;
}

// 查看基站信息
int CDisToPos::GetAnchorInfo(ANCHOR_INFO *info)
{
	int my_temp = 0;
	int i = 0;

	//判断是否初始化
	if (m_IfInit == 0)
	{
		return ERROR_NOT_INIT;
	}

	//更新基站信息
	
	my_temp = UpdateAnchorPos();
	if (my_temp != 0)
	{
		return my_temp;
	}

	//赋值返回
	info->count = m_AnchorCount;
	for (i = 0; i < m_AnchorCount; i++)
	{
		info->pos_list[i].x = m_AnchorPosList[i].x;
		info->pos_list[i].y = m_AnchorPosList[i].y;
		info->pos_list[i].z = m_AnchorPosList[i].z;
	}

	return 0;
}


void CDisToPos::CharToTchar(const char * _char, TCHAR * tchar)
{
	int iLength;
	iLength = MultiByteToWideChar(CP_ACP, 0, _char, (int)strlen(_char) + 1, NULL, 0);
	MultiByteToWideChar(CP_ACP, 0, _char, (int)strlen(_char) + 1, tchar, iLength);
}

void CDisToPos::TcharToChar(const TCHAR * tchar, char * _char)
{
	int iLength;
	//获取字节长度   
	iLength = WideCharToMultiByte(CP_ACP, 0, tchar, -1, NULL, 0, NULL, NULL);
	//将tchar值赋给_char    
	WideCharToMultiByte(CP_ACP, 0, tchar, -1, _char, iLength, NULL, NULL);
}

