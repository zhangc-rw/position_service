#include "StdAfx.h"
#include "DisToPos.h"
#include <windows.h>
#include <cstring>
#include <string.h>





CDisToPos::CDisToPos(void)
{
	m_IfInit = 0;
	m_AnchorCount = 0;
	memset(m_AnchorPosList, 0, sizeof(POSITION_3D) * MAX_ANCHOR);
}


CDisToPos::~CDisToPos(void)
{

}

// ��ʼ������
int CDisToPos::Init()
{
	int my_temp = 0;
	my_temp = UpdateAnchorPos();
	if (my_temp != 0)
	{
		return my_temp;
	}
	m_IfInit = 1;
	return 0;
}



// ���û�վλ��
int CDisToPos::SetAnchorPos(int index, POSITION_3D pos)
{
	int my_temp = 0;
	char temp_anchor_name[128] = {0};
	char temp_anchor_pos[128] = {0};
	TCHAR temp_anchor_name_T[128] = {0};
	TCHAR temp_anchor_pos_T[128] = {0};

	//�ж��Ƿ��ʼ��
	if (m_IfInit == 0)
	{
		return ERROR_NOT_INIT;
	}
	//���»�վ��Ϣ
	my_temp = UpdateAnchorPos();
	if (my_temp != 0)
	{
		return my_temp;
	}

	//���index����count��Χ�����ش���
	if (index < 0 || index > m_AnchorCount)
	{
		return ERROR_INDEX_NOT_RANGE;
	}

	//���������ļ��������
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

	//�����ڴ�
	m_AnchorPosList[index].x = pos.x;
	m_AnchorPosList[index].y = pos.y;
	m_AnchorPosList[index].z = pos.z;

	return 0;
}


//ִ�и��ݾ����������
int CDisToPos::DoDisToPos(int dis_count, double *dis_list, POSITION_3D *pos)
{
	//�ж��Ƿ��ʼ��
	if (m_IfInit == 0)
	{
		return ERROR_NOT_INIT;
	}

	//�ж��ǲ���4����������ʱ��֧��
	if (dis_count != 4 || m_AnchorCount != 4)
	{
		return ERROR_ANCHOR_COUNT;
	}

	//����matlab��������


	return 0;
}



// ���»�վ��Ϣ
int CDisToPos::UpdateAnchorPos()
{
	int count = 0;
	int i = 0;
	char temp_anchor_name[128] = {0};
	char temp_anchor_pos[128] = {0};
	TCHAR temp_anchor_name_T[128] = {0};
	TCHAR temp_anchor_pos_T[128] = {0};

	//���¶�ȡ�����ļ���Ϣ
	count = GetPrivateProfileInt(_TEXT("Anchor_Pos"), _TEXT("Count") ,0, _TEXT(TRANS_CONF_FILE_PATH));

	if (count == 0)
	{
		//���û������������Ĭ�ϸ���������
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
			//�ֱ��ȡXYZ������
			sprintf_s(temp_anchor_name, "A_%d_X", i);
			CharToTchar(temp_anchor_name, temp_anchor_name_T);
			GetPrivateProfileString(TEXT("Anchor_Pos"), temp_anchor_name_T, _TEXT("NA"), temp_anchor_pos_T, 128, _TEXT(TRANS_CONF_FILE_PATH));
			if (_tcscmp(temp_anchor_pos_T, _TEXT("NA")) == 0)
			{
				//δ������Ӧ����
				return ERROR_ANCHOR_POS_NOT_FOUND;
			}
			TcharToChar(temp_anchor_pos_T, temp_anchor_pos);
			m_AnchorPosList[i].x = atof(temp_anchor_pos);

			sprintf_s(temp_anchor_name, "A_%d_X", i);
			CharToTchar(temp_anchor_name, temp_anchor_name_T);
			GetPrivateProfileString(TEXT("Anchor_Pos"), temp_anchor_name_T, _TEXT("NA"), temp_anchor_pos_T, 128, _TEXT(TRANS_CONF_FILE_PATH));
			if (_tcscmp(temp_anchor_pos_T, _TEXT("NA")) == 0)
			{
				//δ������Ӧ����
				return ERROR_ANCHOR_POS_NOT_FOUND;
			}
			TcharToChar(temp_anchor_pos_T, temp_anchor_pos);
			m_AnchorPosList[i].y = atof(temp_anchor_pos);

			sprintf_s(temp_anchor_name, "A_%d_Z", i);
			CharToTchar(temp_anchor_name, temp_anchor_name_T);
			GetPrivateProfileString(TEXT("Anchor_Pos"), temp_anchor_name_T, _TEXT("NA"), temp_anchor_pos_T, 128, _TEXT(TRANS_CONF_FILE_PATH));
			if (_tcscmp(temp_anchor_pos_T, _TEXT("NA")) == 0)
			{
				//δ������Ӧ����
				return ERROR_ANCHOR_POS_NOT_FOUND;
			}
			TcharToChar(temp_anchor_pos_T, temp_anchor_pos);
			m_AnchorPosList[i].z = atof(temp_anchor_pos);
		}
	}
	else
	{
		//����ȡ�Ļ�վλ�÷����ڴ�
		m_AnchorCount = count;
		for (i = 0; i < m_AnchorCount; i++)
		{
			//�ֱ��ȡXYZ������
			sprintf_s(temp_anchor_name, "A_%d_X", i);
			CharToTchar(temp_anchor_name, temp_anchor_name_T);
			GetPrivateProfileString(TEXT("Anchor_Pos"), temp_anchor_name_T, _TEXT("NA"), temp_anchor_pos_T, 128, _TEXT(TRANS_CONF_FILE_PATH));
			if (_tcscmp(temp_anchor_pos_T, _TEXT("NA")) == 0)
			{
				//δ������Ӧ����
				return ERROR_ANCHOR_POS_NOT_FOUND;
			}
			TcharToChar(temp_anchor_pos_T, temp_anchor_pos);
			m_AnchorPosList[i].x = atof(temp_anchor_pos);

			sprintf_s(temp_anchor_name, "A_%d_X", i);
			CharToTchar(temp_anchor_name, temp_anchor_name_T);
			GetPrivateProfileString(TEXT("Anchor_Pos"), temp_anchor_name_T, _TEXT("NA"), temp_anchor_pos_T, 128, _TEXT(TRANS_CONF_FILE_PATH));
			if (_tcscmp(temp_anchor_pos_T, _TEXT("NA")) == 0)
			{
				//δ������Ӧ����
				return ERROR_ANCHOR_POS_NOT_FOUND;
			}
			TcharToChar(temp_anchor_pos_T, temp_anchor_pos);
			m_AnchorPosList[i].y = atof(temp_anchor_pos);

			sprintf_s(temp_anchor_name, "A_%d_Z", i);
			CharToTchar(temp_anchor_name, temp_anchor_name_T);
			GetPrivateProfileString(TEXT("Anchor_Pos"), temp_anchor_name_T, _TEXT("NA"), temp_anchor_pos_T, 128, _TEXT(TRANS_CONF_FILE_PATH));
			if (_tcscmp(temp_anchor_pos_T, _TEXT("NA")) == 0)
			{
				//δ������Ӧ����
				return ERROR_ANCHOR_POS_NOT_FOUND;
			}
			TcharToChar(temp_anchor_pos_T, temp_anchor_pos);
			m_AnchorPosList[i].z = atof(temp_anchor_pos);
		}
	}
	return 0;
}

// ���Ļ�վ����
int CDisToPos::SetAnchorCount(int count)
{
	int my_temp = 0;
	char temp_anchor_count[128] = {0};
	TCHAR temp_anchor_count_T[128] = {0};

	//�ж��Ƿ��ʼ��
	if (m_IfInit == 0)
	{
		return ERROR_NOT_INIT;
	}

	//���»�վ��Ϣ
	my_temp = UpdateAnchorPos();
	if (my_temp != 0)
	{
		return my_temp;
	}

	//�������ú��ڴ����
	sprintf_s(temp_anchor_count, "%d", count);
	CharToTchar(temp_anchor_count, temp_anchor_count_T);
	WritePrivateProfileString(TEXT("Anchor_Pos"), _TEXT("Count"), temp_anchor_count_T, _TEXT(TRANS_CONF_FILE_PATH)); 

	return 0;
}

// �鿴��վ��Ϣ
int CDisToPos::GetAnchorInfo(ANCHOR_INFO *info)
{
	int my_temp = 0;
	int i = 0;

	//�ж��Ƿ��ʼ��
	if (m_IfInit == 0)
	{
		return ERROR_NOT_INIT;
	}

	//���»�վ��Ϣ
	
	my_temp = UpdateAnchorPos();
	if (my_temp != 0)
	{
		return my_temp;
	}

	//��ֵ����
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
	iLength = MultiByteToWideChar(CP_ACP, 0, _char, strlen(_char) + 1, NULL, 0);
	MultiByteToWideChar(CP_ACP, 0, _char, strlen(_char) + 1, tchar, iLength);
}

void CDisToPos::TcharToChar(const TCHAR * tchar, char * _char)
{
	int iLength;
	//��ȡ�ֽڳ���   
	iLength = WideCharToMultiByte(CP_ACP, 0, tchar, -1, NULL, 0, NULL, NULL);
	//��tcharֵ����_char    
	WideCharToMultiByte(CP_ACP, 0, tchar, -1, _char, iLength, NULL, NULL);
}

