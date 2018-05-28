#pragma once

#include <stdarg.h>  

#define TRANS_CONF_FILE_PATH ".//Anchor_Pos.ini"

#define ERROR_ANCHOR_COUNT 0x00000001	//基站个数错误
#define ERROR_ANCHOR_POS_NOT_FOUND 0x00000002	//基站位置未找到
#define ERROR_NOT_INIT 0x00000003	//未初始化
#define ERROR_INDEX_NOT_RANGE 0x00000004	//输入索引不在范围
#define ERROR_TRANS_WRONG 0x00000005	//由于基站坐标和距离引起的不能转换

#define MAX_ANCHOR 20

#define DEFULT_ANCHOR_COUNT "4"
#define DEFULT_ANCHOR_POSITION_X "0"
#define DEFULT_ANCHOR_POSITION_Y "0"
#define DEFULT_ANCHOR_POSITION_Z "0"

typedef struct _POSITION_3D
{
	//三维点坐标。
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

	// 初始化配置
	int Init();
	// 设置基站位置，从0开始
	int SetAnchorPos(int index, POSITION_3D pos);
	// 执行根据距离计算坐标
	int DoDisToPos(int dis_count, double *dis_list, POSITION_3D *pos);
	// 更新基站信息
	int UpdateAnchorPos();
	// 更改基站数量
	int SetAnchorCount(int count);
	// 查看基站信息
	int GetAnchorInfo(ANCHOR_INFO *info);
private:
	//内部数据

	int m_IfInit;	//是否初始化
	int m_AnchorCount;	//基站个数
	POSITION_3D m_AnchorPosList[MAX_ANCHOR];	//各基站坐标

private:
	//内部方法

	//Char转Tchar
	void CharToTchar(const char * _char, TCHAR * tchar);
	//Tchar转Char
	void TcharToChar(const TCHAR * tchar, char * _char);
};

