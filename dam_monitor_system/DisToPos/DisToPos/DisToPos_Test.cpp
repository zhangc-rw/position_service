// DisToPos.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "DisToPos.h"


int _tmain(int argc, _TCHAR* argv[])
{
	ANCHOR_INFO info;
	CDisToPos test;
	POSITION_3D pos;
	int my_temp = 0;
	pos.x = 2;
	pos.y = 3;
	pos.z = 4;
	double dis_list[4] = {1.0,2.2,4.5,6.6};

	my_temp = test.Init();

	my_temp = test.GetAnchorInfo(&info);

	my_temp = test.SetAnchorPos(1, pos);

	my_temp = test.DoDisToPos(4, dis_list, &pos);

	my_temp = test.UpdateAnchorPos();

	my_temp = test.SetAnchorCount(3);

	return 0;
}


