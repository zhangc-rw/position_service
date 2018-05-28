// DisToPos.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "DisToPos.h"
#include "dis_to_pos_matlab.h"
#include <iostream>


int _tmain(int argc, _TCHAR* argv[])
{
	ANCHOR_INFO info;
	CDisToPos test;
	POSITION_3D pos_t;
	int my_temp = 0;
	pos_t.x = 2;
	pos_t.y = 3;
	pos_t.z = 4;
	double dis_list[4] = {4.14,5.13,5.0,4.9};
	int i = 0;

	my_temp = test.Init();

	my_temp = test.GetAnchorInfo(&info);

//	my_temp = test.SetAnchorPos(1, pos_t);

	my_temp = test.DoDisToPos(4, dis_list, &pos_t);

	my_temp = test.UpdateAnchorPos();

	my_temp = test.SetAnchorCount(4);

	while (1)
	{
		my_temp = dis_to_pos_matlabInitialize();
		if (my_temp)    //必须的要初始化，格式为  名字Initialize()
		{
			printf("success!\n");
		}
		else
		{
			printf("failed!\n");
			//		return 0;
		}

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

		double nu1[] = {0};
		double nu2[] = {0};
		double nu3[] = {0};
		double nu4[] = {0};
		double nu5[] = {8};
		double nu6[] = {0};
		double nu7[] = {6};
		double nu8[] = {0};
		double nu9[] = {0};
		double nu10[] = {0};
		double nu11[] = {0};
		double nu12[] = {3};
		double nuda[] = {4.137239920271500};
		double nudb[] = {5.143225995875269};
		double nudc[] = {5.077910355884999};
		double nudd[] = {4.803843739516471};

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

		double x_temp;
		x_temp = xyz.Get(1,1);
		x_temp = xyz.Get(1,2);
		x_temp = xyz.Get(1,3);

		i++;
		printf("%d\n", i);
	}

	return 0;
}


