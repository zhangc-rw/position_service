#pragma once

#include <stdarg.h>  

#define TRANS_CONF_FILE_PATH ".//Anchor_Pos.ini"

#define ERROR_ANCHOR_COUNT 0x00000001	//��վ��������
#define ERROR_ANCHOR_POS_NOT_FOUND 0x00000002	//��վλ��δ�ҵ�
#define ERROR_NOT_INIT 0x00000003	//δ��ʼ��
#define ERROR_INDEX_NOT_RANGE 0x00000004	//�����������ڷ�Χ
#define ERROR_TRANS_WRONG 0x00000005	//���ڻ�վ����;�������Ĳ���ת��

#define MAX_ANCHOR 20

#define DEFULT_ANCHOR_COUNT "4"
#define DEFULT_ANCHOR_POSITION_X "0"
#define DEFULT_ANCHOR_POSITION_Y "0"
#define DEFULT_ANCHOR_POSITION_Z "0"

typedef struct _POSITION_3D
{
	//��ά�����ꡣ
	double x;
	double y;
	double z;
}POSITION_3D;

typedef struct _ANCHOR_INFO
{
	int count;
	POSITION_3D pos_list[MAX_ANCHOR];
}ANCHOR_INFO;

class CDisToPos
{
public:
	CDisToPos(void);
	~CDisToPos(void);

	// ��ʼ������
	int Init();
	// ���û�վλ�ã���0��ʼ
	int SetAnchorPos(int index, POSITION_3D pos);
	// ִ�и��ݾ����������
	int DoDisToPos(int dis_count, double *dis_list, POSITION_3D *pos);
	// ���»�վ��Ϣ
	int UpdateAnchorPos();
	// ���Ļ�վ����
	int SetAnchorCount(int count);
	// �鿴��վ��Ϣ
	int GetAnchorInfo(ANCHOR_INFO *info);
private:
	//�ڲ�����

	int m_IfInit;	//�Ƿ��ʼ��
	int m_AnchorCount;	//��վ����
	POSITION_3D m_AnchorPosList[MAX_ANCHOR];	//����վ����

private:
	//�ڲ�����

	//CharתTchar
	void CharToTchar(const char * _char, TCHAR * tchar);
	//TcharתChar
	void TcharToChar(const TCHAR * tchar, char * _char);
};

