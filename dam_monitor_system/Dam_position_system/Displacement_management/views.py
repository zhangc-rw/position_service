from django.shortcuts import render
# Create your views here.
from Displacement_management.models import DReal
from Displacement_management.models import DPast
from Displacement_management.models import Dping
from Displacement_management.models import Average_data
from Displacement_management.models import Average_data_his
from Displacement_management.models import Raw_data
from Displacement_management.models import Processing_data

from Displacement_management.models import Smooth_data
from Displacement_management.models import Smooth_data_his
from Displacement_management.models import Convergence_data
from Displacement_management.models import Convergence_data_his
from Dam_Device_management.models import Device
from Dam_Device_management.models import Dam


import datetime
import json
import re
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse

	#return HttpResponseRedirect('/Dam_Device_management/DandL_management')
	#return HttpResponse(json.dumps({'d_list':d_list,'time_list':time_list}))
	#return render(request,'label_detail_history.html')'''
def Raw_data_history(request):
	if request.session.get('userName'):
		dam_num = request.POST.get('dam_num')
		device_num = request.POST.get('device_num')
		station_num = request.POST.get('station_num')
		time = request.POST.get('reservationtime')
		temperature = request.POST.get('temperature_num')
		raw = request.POST.get('raw_num')
		#print(dam_num)


		Data_list_temperature = []
		Data_list_raw  = [] 
		Time_list = []

		start =time[0:16]
		end = time[-16:]
		print(start)

		Convergence_time = ('2018-08-06 23:59:59')
		Convergence_his_start_time = ('2018-08-22 23:59:59')
		Convergence_his_end_time = ('2018-09-08 21:27:00')



		dam_list = Dam.objects.get(dam_num = dam_num)
		device_list = Device.objects.filter(device_num = device_num,at_tip =  1,dam = dam_list )
		#S0E0
		if end <= Convergence_time:
			print('S0E0')

			#平均
			Average_list = Average_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,stationID = station_num[index])		
			
			#温度
			if temperature[index] == "是":
				temperature_list = []
				for t in Average_list:
					temperature_list.append(t.temperature)
					Data_list.append(t.temperature)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
				#print(temperature_list)
				num = len(temperature_list)
				Num_list.append(num)
				Name1_list.append(dam_num)
				Name1_list.append(station_num[index])
				Name1_list.append(device_num[index])
				Name1_list.append('1')
				Name1_list=','.join(Name1_list)
				Name_list.append(Name1_list)
			
		#S1E1&S3E3
		elif (Convergence_time <= start<=end<= Convergence_his_start_time) or (Convergence_his_end_time<=start):
			print('S1E1&S3E3')

			#时间
			D_list = Processing_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,station_num = station_num).values("temperature","dreal_update_time","d")	
			for t in D_list:
				Time_list.append(t["dreal_update_time"].strftime("%Y-%m-%d %H:%M:%S"))

			#温度
			if temperature =="是":
				print('执行判断中1')
				for t in D_list:
					Data_list_temperature.append(t["temperature"])
					#Time_list.append(t["dreal_update_time"].strftime("%Y-%m-%d %H:%M:%S"))
				print('温度FOR查询完成')

			#原始
			if raw =="是":
				print('执行判断中2')
				for t in D_list:
					Data_list_raw.append(t["d"])
					#Time_list.append(t["dreal_update_time"].strftime("%Y-%m-%d %H:%M:%S"))
				print('原始数据FOR查询完成')



		#S1E2
		elif Convergence_time<= start<= Convergence_his_start_time<=end<=Convergence_his_end_time:
			print('S1E2')

			#平均
			Average_list = Average_data.objects.filter(dreal_update_time__range=(start, Convergence_his_start_time)).filter(device = device_list,stationID = station_num[index])		
			

			#平均
			Average_list_his = Average_data_his.objects.filter(dreal_update_time__range=(Convergence_his_start_time, end)).filter(device = device_list,stationID = station_num[index])		
			
			#温度
			if temperature[index] == "是":
				temperature_list = []
				for t in Average_list:
					temperature_list.append(t.temperature)
					Data_list.append(t.temperature)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
				for t in Average_list_his:
					temperature_list.append(t.temperature)
					Data_list.append(t.temperature)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
				#print(temperature_list)
				num = len(temperature_list)
				Num_list.append(num)
				Name1_list.append(dam_num)
				Name1_list.append(station_num[index])
				Name1_list.append(device_num[index])
				Name1_list.append('1')
				Name1_list=','.join(Name1_list)
				Name_list.append(Name1_list)
			
		#S1E3
		elif Convergence_time<= start<= Convergence_his_start_time<=Convergence_his_end_time<=end:
			print('S1E3')

			#平均
			Average_list= Average_data.objects.filter(dreal_update_time__range=(start, Convergence_his_start_time)).filter(device = device_list,stationID = station_num[index])		
			

			#平均
			Average_list_his = Average_data_his.objects.filter(dreal_update_time__range=(Convergence_his_start_time, Convergence_his_end_time)).filter(device = device_list,stationID = station_num[index])		
			

			#平均
			Average_list_2 = Average_data.objects.filter(dreal_update_time__range=(Convergence_his_end_time, end)).filter(device = device_list,stationID = station_num[index])		
			
			#温度
			if temperature[index] == "是":
				temperature_list = []
				for t in Average_list:
					temperature_list.append(t.temperature)
					Data_list.append(t.temperature)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
				for t in Average_list_his:
					temperature_list.append(t.temperature)
					Data_list.append(t.temperature)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
				for t in Average_list_2:
					temperature_list.append(t.temperature)
					Data_list.append(t.temperature)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
				#print(temperature_list)
				num = len(temperature_list)
				Num_list.append(num)
				Name1_list.append(dam_num)
				Name1_list.append(station_num[index])
				Name1_list.append(device_num[index])
				Name1_list.append('1')
				Name1_list=','.join(Name1_list)
				Name_list.append(Name1_list)

		#S2E2
		elif Convergence_his_start_time<= start<=end<=Convergence_his_end_time:
			print('S2E2')

			#平均
			Average_list_his = Average_data_his.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,stationID = station_num[index])		
			
			#温度
			if temperature[index] == "是":
				temperature_list = []
				for t in Average_list_his:
					temperature_list.append(t.temperature)
					Data_list.append(t.temperature)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
				#print(temperature_list)
				num = len(temperature_list)
				Num_list.append(num)
				Name1_list.append(dam_num)
				Name1_list.append(station_num[index])
				Name1_list.append(device_num[index])
				Name1_list.append('1')
				Name1_list=','.join(Name1_list)
				Name_list.append(Name1_list)

		#S2E3
		elif Convergence_his_start_time<= start<=Convergence_his_end_time<=end:
			print('S2E3')
			#原始

			#平均
			Average_list_his = Average_data_his.objects.filter(dreal_update_time__range=(start, Convergence_his_end_time)).filter(device = device_list,stationID = station_num[index])		

			#平均
			Average_list= Average_data.objects.filter(dreal_update_time__range=(Convergence_his_end_time, end)).filter(device = device_list,stationID = station_num[index])		
			
			#温度
			if temperature[index] == "是":
				temperature_list = []
				for t in Average_list_his:
					temperature_list.append(t.temperature)
					Data_list.append(t.temperature)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
				for t in Average_list:
					temperature_list.append(t.temperature)
					Data_list.append(t.temperature)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
				
				#print(temperature_list)
				num = len(temperature_list)
				Num_list.append(num)
				Name1_list.append(dam_num)
				Name1_list.append(station_num[index])
				Name1_list.append(device_num[index])
				Name1_list.append('1')
				Name1_list=','.join(Name1_list)
				Name_list.append(Name1_list)

			
			
		#print(Data_list_temperature)
		#print(Data_list_raw)
		print(Time_list)	
		return HttpResponse(json.dumps({'Data_list_temperature':Data_list_temperature,'Data_list_raw':Data_list_raw,'Time_list':Time_list}))
		#return render(request, 'list_show_history.html')#, {'Data_list': json.dumps(Data_list),'Time_list': json.dumps(Time_list),'Name_list': json.dumps(Name_list),'Num_list': json.dumps(Num_list)})
	else:
		return render(request, 'login.html')	
#实时位移查看
def Raw_data_real(request):
	if request.session.get('userName'):
		dam_num = request.POST.get('dam_num')
		dam_num = re.findall(r"\d+\.?\d*",dam_num)
		device_num = request.POST.get('device_num')
		device_num = re.findall(r"\d+\.?\d*",device_num)
		station_num = request.POST.get('station_num')
		station_num = re.findall(r"\d+\.?\d*",station_num)
		#print (dam_num)
		#print (device_num)
		print (station_num)
		num = len(station_num)
		Data_list = []
		X_list = []
		Y_list = []
		Z_list = []
		Time_list = []
		for index in range(num):
			print (station_num[index])
			
				
		#判断锚点编号
			dam_list = Dam.objects.get(dam_num = dam_num[index])
			device_list = Device.objects.get(device_num = device_num[index],at_tip = 1,dam = dam_list)
			#D_list = Raw_data.objects.filter(device = device_list).order_by('-id')[:1]
			D_list = Processing_data.objects.filter(device = device_list,station_num = station_num[index]).order_by('-id')[:1]
			DPast_list = DPast.objects.filter(device = device_list).order_by('-id')[:1]
			d2_list = []

			if station_num[index] == '15':
				Data_list.append("无数据")
				X_list.append("无数据")
				Y_list.append("无数据")
				Z_list.append("无数据")
				Time_list.append('NULL')
			elif station_num[index] == '16':
				Data_list.append("无数据")
				X_list.append("无数据")
				Y_list.append("无数据")
				Z_list.append("无数据")
				Time_list.append('NULL')
			elif station_num[index] == '17':
				Data_list.append("无数据")
				X_list.append("无数据")
				Y_list.append("无数据")
				Z_list.append("无数据")
				Time_list.append('NULL')
			elif station_num[index] == '18':
				Data_list.append("无数据")
				X_list.append("无数据")
				Y_list.append("无数据")
				Z_list.append("无数据")
				Time_list.append('NULL')

			else:
				for d in D_list :
					Data_list.append(d.d)
					d2_list.append(d.d)
					Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S:%S"))
				for d in DPast_list :
					X_list.append(d.x)
					Y_list.append(d.y)
					Z_list.append(d.z)
				'''if station_num[index] == "0":
					Data_list.append(d.d1)
					d2_list.append(d.d1)
				elif station_num[index] == "1":
					Data_list.append(d.d2)
					d2_list.append(d.d2)
				elif station_num[index] == "2":
					Data_list.append(d.d3)
					d2_list.append(d.d3)
				elif station_num[index] == "3":
					Data_list.append(d.d4)
					d2_list.append(d.d4)'''
		print (Time_list)	
		print (Data_list)
		print (X_list)
		print (Y_list)
		print (Z_list)
		return HttpResponse(json.dumps({'Data_list':Data_list,'Time_list':Time_list,'X_list':X_list,'Y_list':Y_list,'Z_list':Z_list}))#,'Num_list':Num_list}))
	else:
		return render(request, 'login.html')
def DReal_management(request,aid,bid,cid):
	if request.session.get('userName'):
		Data_list = []
		Name_list = [] 
		Num_list = [] 
		Time_list = []
		dam_list = Dam.objects.get(dam_num = aid)
		device_list = Device.objects.get(device_num = cid,at_tip = 1,dam = dam_list)
		#通过最大的ID查询
		DPast_list = DPast.objects.filter(device = device_list).order_by('-id')[:4]
		Dping_list = Dping.objects.filter(device = device_list).order_by('-id')[:4]
		#收敛
		Convergence_list = Convergence_data.objects.filter(device = device_list,station_num = bid).order_by('-id')[:4]
		#平滑
		Smooth_list = Smooth_data.objects.filter(device = device_list,station_num = bid).order_by('-id')[:4]
		#平均
		Average_list = Average_data.objects.filter(device = device_list,station_num = bid).order_by('-id')[:4]

		#D_list = Raw_data.objects.filter(device = device_list).order_by('-id')[:120]
		D_list = Processing_data.objects.filter(device = device_list,station_num = bid).exclude(d = 0).order_by('-id')[:120]
		
		Convergence_list = Convergence_list[::-1]
		Smooth_list = Smooth_list[::-1]
		Average_list = Average_list[::-1]
		D_list = D_list[::-1]
		DPast_list = DPast_list[::-1]

		#D_list = D_list.reverse()[:1]
		#Name1_list = [] 
		Name2_list = [] 
		Name3_list = []
		Name4_list = []
		Name5_list = []
		Name6_list = []
		Name7_list = []
		Name8_list = []

		#原始
		d2_list = []
		for d in D_list :
			Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S:%S"))
			Data_list.append(d.d)
			d2_list.append(d.d)
		'''if bid== "0":
			D_list_2 = Raw_data.objects.filter(device = device_list, d1 = 0).order_by('-id')[:120]
			for i in D_list_2:
				if i in D_list:
					D_list.remove(i)
			for d in D_list :
				Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S:%S"))
				Data_list.append(d.d1)
				d2_list.append(d.d1)
		elif bid == "1":
			D_list_2 = Raw_data.objects.filter(device = device_list, d2 = 0).order_by('-id')[:120]
			for i in D_list_2:
				if i in D_list:
					D_list.remove(i)
			for d in D_list :
				Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S:%S"))
				Data_list.append(d.d2)
				d2_list.append(d.d2)
		elif bid == "2":
			D_list_2 = Raw_data.objects.filter(device = device_list, d3 = 0).order_by('-id')[:120]
			for i in D_list_2:
				if i in D_list:
					D_list.remove(i)
			for d in D_list :
				Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S:%S"))
				Data_list.append(d.d3)
				d2_list.append(d.d3)
		elif bid == "3":
			D_list_2 = Raw_data.objects.filter(device = device_list, d4 = 0).order_by('-id')[:120]
			for i in D_list_2:
				if i in D_list:
					D_list.remove(i)
			for d in D_list :
				Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S:%S"))
				Data_list.append(d.d4)
				d2_list.append(d.d4)'''
		num = len(d2_list)
		Num_list.append(num)
		Name2_list.append(aid)
		Name2_list.append(bid)
		Name2_list.append(cid)
		Name2_list.append('2')
		Name2_list=','.join(Name2_list)
		Name_list.append(Name2_list)				
		#平均
		d3_list = []
		for d in Average_list:
			d3_list.append(d.d)
			Data_list.append(d.d)
			Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
		num = len(d3_list)#计算list元素个数
		Num_list.append(num)
		Name3_list.append(aid)
		Name3_list.append(bid)
		Name3_list.append(cid)
		Name3_list.append('3')
		Name3_list=','.join(Name3_list)#合并字符串	
		Name_list.append(Name3_list)
				

		#收敛
		d4_list = []
		for d in Convergence_list:
			Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
			d4_list.append(d.d)
			Data_list.append(d.d)
		num = len(d4_list)
		Num_list.append(num)
		Name4_list.append(aid)
		Name4_list.append(bid)
		Name4_list.append(cid)	
		Name4_list.append('4')
		Name4_list=','.join(Name4_list)
		Name_list.append(Name4_list)
			

		#平滑
		d5_list = []
		for d in Smooth_list:
			Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
			d5_list.append(d.d)
			Data_list.append(d.d)
		num = len(d5_list)
		Num_list.append(num)
		Name5_list.append(aid)
		Name5_list.append(bid)
		Name5_list.append(cid)
		Name5_list.append('5')
		Name5_list=','.join(Name5_list)
		Name_list.append(Name5_list)

		#坐标
				
		d6_list = []
		d7_list = []
		d8_list = []
		for t in DPast_list:
			Data_list.append(t.x)
			d6_list.append(t.x)
			Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
		for t in DPast_list:
			Data_list.append(t.y)
			d7_list.append(t.y)
			Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
		for t in DPast_list:
			Data_list.append(t.z)
			d8_list.append(t.z)
			Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
		
		num = len(d6_list)
		Num_list.append(num)
		Name6_list.append(aid)
		Name6_list.append(bid)
		Name6_list.append(cid)
		Name6_list.append('6')
		Name6_list=','.join(Name6_list)
		Name_list.append(Name6_list)

		num = len(d7_list)
		Num_list.append(num)
		Name7_list.append(aid)
		Name7_list.append(bid)
		Name7_list.append(cid)
		Name7_list.append('7')
		Name7_list=','.join(Name7_list)
		Name_list.append(Name7_list)

		num = len(d8_list)
		Num_list.append(num)
		Name8_list.append(aid)
		Name8_list.append(bid)
		Name8_list.append(cid)
		Name8_list.append('8')
		Name8_list=','.join(Name8_list)
		Name_list.append(Name8_list)

		Name1_list = [] 
		
		temperature_list = []
		for t in D_list:
			temperature_list.append(t.temperature)
			Data_list.append(t.temperature)
			Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
		#print(temperature_list)
		num = len(temperature_list)
		Num_list.append(num)
		Name1_list.append(aid)
		Name1_list.append(bid)
		Name1_list.append(cid)
		Name1_list.append('1')
		Name1_list=','.join(Name1_list)
		Name_list.append(Name1_list)
		
		print(Data_list)
		#print(Time_list)
		print(Name_list)
		print(Num_list)		
		return  render(request, 'label_detail_realTime.html',{'Num_list': json.dumps(Num_list),'Data_list': json.dumps(Data_list),'Time_list': json.dumps(Time_list),'Name_list': json.dumps(Name_list)})
	else:
		return render(request, 'login.html')

#历史位移查看
def DPast_management_sametime_2(request):
	if request.session.get('userName'):
		if request.method == "POST":
			time_ymd = request.POST.get('reservationtime')
			time_hms_start = request.POST.get('start_time')
			time_hms_end = request.POST.get('end_time')
			dam_num = request.POST.get('dam_num')
			device_num = request.POST.get('device_num')
			station_num = request.POST.get('station_num')
			average = request.POST.get('d1_num')
			convergence = request.POST.get('d2_num')
			smooth = request.POST.get('d3_num')
			XYZ = request.POST.get('coor_num')
			temperature = request.POST.get('temperature_num')
			print(time_ymd)
			print(len(station_num))
			num = len(station_num)
			Data_list = []
			Name_list = [] 
			Num_list = [] 
			Time_list = []
			#遍历基站列表取出时间段个数
			#取出时间的每天
			date_list = []
			begin_date = datetime.datetime.strptime(time_ymd[0:10], "%Y-%m-%d")
			end_date = datetime.datetime.strptime(time_ymd[-10:], "%Y-%m-%d")
			while begin_date <= end_date:
				date_str = begin_date.strftime("%Y-%m-%d")
				date_list.append(date_str)
				begin_date += datetime.timedelta(days=1)
			print (date_list)
			#整合时间代码
			for t in date_list:
				time_list_start =[]
				time_list_start.append(t)
				time_list_start.append(time_hms_start)
				start_1 =' '.join(time_list_start)
				print(start_1)
				time_list_start =[]
				time_list_start.append(t)
				time_list_start.append(time_hms_end)
				end_1=' '.join(time_list_start)
				print(end_1)

				Convergence_time = ('2018-08-06 23:59:59')
				Convergence_his_start_time = ('2018-08-22 23:59:59')
				Convergence_his_end_time = ('2018-09-08 21:27:00')
				Name1_list = [] 
				Name3_list = []
				Name4_list = []
				Name5_list = []
				Name6_list = []
				Name7_list = []
				Name8_list = []


				dam_list = Dam.objects.get(dam_num = dam_num)
				device_list = Device.objects.filter(device_num = device_num,at_tip =  1,dam = dam_list)
				#S0_E0
				if end_1 < Convergence_time:
					DPast_list = DPast.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list)
					Dping_list = Dping.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list)
					#收敛
					if convergence =="是":
						d4_list = []
						for d in DPast_list:
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							if station_num == "0":
								d4_list.append(d.d1)
								Data_list.append(d.d1)
							elif station_num == "1":
								d4_list.append(d.d2)
								Data_list.append(d.d2)
							elif station_num == "2":
								d4_list.append(d.d3)
								Data_list.append(d.d3)
							elif station_num == "3":
								d4_list.append(d.d4)
								Data_list.append(d.d4)
						num = len(d4_list)
						Num_list.append(num)
						Name4_list.append(dam_num)
						Name4_list.append(station_num)
						Name4_list.append(device_num)
						Name4_list.append('4')
						Name4_list=','.join(Name4_list)
						Name_list.append(Name4_list)
					#平滑
					if smooth =="是":
						d5_list = []
						for d in Dping_list:
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							if station_num == "0":
								d5_list.append(d.d1)
								Data_list.append(d.d1)
							elif station_num == "1":
								d5_list.append(d.d2)
								Data_list.append(d.d2)
							elif station_num == "2":
								d5_list.append(d.d3)
								Data_list.append(d.d3)
							elif station_num == "3":
								d5_list.append(d.d4)
								Data_list.append(d.d4)
						num = len(d5_list)
						Num_list.append(num)
						Name5_list.append(dam_num)
						Name5_list.append(station_num)
						Name5_list.append(device_num)
						Name5_list.append('5')
						Name5_list=','.join(Name5_list)
						Name_list.append(Name5_list)

				#S1E1&S3E3
				elif (Convergence_time <= start_1  <= Convergence_his_start_time) or (Convergence_his_end_time<=start_1):
					#收敛
					Convergence_list = Convergence_data.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list,stationID = station_num)
					#平滑
					Smooth_list = Smooth_data.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list,stationID = station_num)
					#平均
					Average_list = Average_data.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list,stationID= station_num)
					#温度
					if temperature =="是":
						temperature_list = []
						for t in Average_list:
							temperature_list.append(t.temperature)
							Data_list.append(t.temperature)
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						#print(temperature_list)
						num = len(temperature_list)
						Num_list.append(num)
						Name1_list.append(dam_num)
						Name1_list.append(station_num)#基站编号
						Name1_list.append(device_num)#标签编号
						Name1_list.append('1')
						Name1_list=','.join(Name1_list)	
						Name_list.append(Name1_list)
						#Name1_list.clear()
					#平均
					if average =="是":
						d3_list = []
						for d in Average_list:
							d3_list.append(d.d)
							Data_list.append(d.d)
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						num = len(d3_list)#计算list元素个数
						Num_list.append(num)
						Name3_list.append(dam_num)
						Name3_list.append(station_num)
						Name3_list.append(device_num)
						Name3_list.append('3')
						Name3_list=','.join(Name3_list)#合并字符串	
						Name_list.append(Name3_list)

					#收敛
					if convergence =="是":
						d4_list = []
						for d in Convergence_list:
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d4_list.append(d.d)
							Data_list.append(d.d)
						num = len(d4_list)
						Num_list.append(num)
						Name4_list.append(dam_num)	
						Name4_list.append(station_num)
						Name4_list.append(device_num)
						Name4_list.append('4')
						Name4_list=','.join(Name4_list)
						Name_list.append(Name4_list)				
					#平滑
					if smooth =="是":
						d5_list = []
						for d in Smooth_list:
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d5_list.append(d.d)
							Data_list.append(d.d)
						num = len(d5_list)
						Num_list.append(num)
						Name5_list.append(dam_num)
						Name5_list.append(station_num)
						Name5_list.append(device_num)
						Name5_list.append('5')
						Name5_list=','.join(Name5_list)
						Name_list.append(Name5_list)
				#S2E2
				elif Convergence_his_start_time<=start_1<=Convergence_his_end_time:
					print('S2E2')
					#收敛_his
					Convergence_list_his = Convergence_data_his.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list,stationID = station_num)
					#平滑_his
					Smooth_list_his = Smooth_data_his.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list,stationID = station_num)
					#平均
					Average_list_his = Average_data_his.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list,stationID= station_num)
					#温度
					if temperature == "是":
						temperature_list = []
						for t in Average_list_his:
							temperature_list.append(t.temperature)
							Data_list.append(t.temperature)
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						print(temperature_list)
						num = len(temperature_list)
						Num_list.append(num)
						Name1_list.append(dam_num)
						Name1_list.append(station_num)
						Name1_list.append(device_num)
						Name1_list.append('1')
						Name1_list=','.join(Name1_list)
						Name_list.append(Name1_list)		
					#平均
					if average =="是":
						d3_list = []
						for d in Average_list_his:
							d3_list.append(d.d)
							Data_list.append(d.d)
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						num = len(d3_list)#计算list元素个数
						Num_list.append(num)
						Name3_list.append(dam_num)
						Name3_list.append(station_num)
						Name3_list.append(device_num)
						Name3_list.append('3')
						Name3_list=','.join(Name3_list)#合并字符串	
						Name_list.append(Name3_list)
					#收敛
					if convergence =="是":
						d4_list = []
						for d_his in Convergence_list_his:
							Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d4_list.append(d_his.d)
							Data_list.append(d_his.d)
						num = len(d4_list)
						Num_list.append(num)
						Name4_list.append(dam_num)	
						Name4_list.append(station_num)
						Name4_list.append(device_num)	
						Name4_list.append('4')
						Name4_list=','.join(Name4_list)
						Name_list.append(Name4_list)				
					#平滑
					if smooth =="是":
						d5_list = []
						for d_his in Smooth_list_his:
							Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d5_list.append(d_his.d)
							Data_list.append(d_his.d)
						num = len(d5_list)
						Num_list.append(num)
						Name5_list.append(dam_num)
						Name5_list.append(station_num)
						Name5_list.append(device_num)
						Name5_list.append('5')
						Name5_list=','.join(Name5_list)
						Name_list.append(Name5_list)

				#坐标
				
				if XYZ == "是":				
					d6_list = []
					d7_list = []
					d8_list = []
					DPast_list = DPast.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list)
					for t in DPast_list:
						Data_list.append(t.x)
						d6_list.append(t.x)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					for t in DPast_list:
						Data_list.append(t.y)
						d7_list.append(t.y)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					for t in DPast_list:
						Data_list.append(t.z)
						d8_list.append(t.z)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					
					num = len(d6_list)
					Num_list.append(num)
					Name6_list.append(dam_num)
					Name6_list.append(station_num)
					Name6_list.append(device_num)
					Name6_list.append('6')
					Name6_list=','.join(Name6_list)
					Name_list.append(Name6_list)

					num = len(d7_list)
					Num_list.append(num)
					Name7_list.append(dam_num)
					Name7_list.append(station_num)
					Name7_list.append(device_num)
					Name7_list.append('7')
					Name7_list=','.join(Name7_list)
					Name_list.append(Name7_list)

					num = len(d8_list)
					Num_list.append(num)
					Name8_list.append(dam_num)
					Name8_list.append(station_num)
					Name8_list.append(device_num)
					Name8_list.append('8')
					Name8_list=','.join(Name8_list)
					Name_list.append(Name8_list)
						
			print(Data_list)
			print(Time_list)
			print(Name_list)
			print(Num_list)
			return render(request, 'label_detail_history_sametime.html', {'Data_list': json.dumps(Data_list),'Time_list': json.dumps(Time_list),'Name_list': json.dumps(Name_list),'Num_list': json.dumps(Num_list)})
		else:
			return render(request, 'list_show_realTime.html')
	else:
		return render(request, 'login.html')
#历史位移查看
def DPast_management_2(request):
	if request.session.get('userName'):
		if request.method == "POST":
			time = request.POST.get('reservationtime')
			dam_num = request.POST.get('dam_num')
			device_num = request.POST.get('device_num')
			station_num = request.POST.get('station_num')
			average = request.POST.get('d1_num')
			convergence = request.POST.get('d2_num')
			smooth = request.POST.get('d3_num')
			XYZ = request.POST.get('coor_num')
			temperature = request.POST.get('temperature_num')
			print(time)
			print(device_num)
			print(station_num)
			print(temperature)
			num = len(station_num)
			Data_list = []
			Name_list = [] 
			Num_list = [] 
			Time_list = []
			start =time[0:16]
			end = time[-16:]
			print(start)

			Convergence_time = ('2018-08-06 23:59:59')
			Convergence_his_start_time = ('2018-08-22 23:59:59')
			Convergence_his_end_time = ('2018-09-08 21:27:00')

			Name1_list = [] 
			Name2_list = [] 
			Name3_list = []
			Name4_list = []
			Name5_list = []
			Name6_list = []
			Name7_list = []
			Name8_list = []

			dam_list = Dam.objects.get(dam_num = dam_num)
			device_list = Device.objects.filter(device_num = device_num,at_tip =  1,dam = dam_list )
			#S0E0
			if end <= Convergence_time:
				print('S0E0')

				#收敛
				DPast_list = DPast.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
				#平滑
				Dping_list = Dping.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
				#平均
				Average_list = Average_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,stationID = station_num)		
				
				#温度
				if temperature == "是":
					temperature_list = []
					for t in Average_list:
						temperature_list.append(t.temperature)
						Data_list.append(t.temperature)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					#print(temperature_list)
					num = len(temperature_list)
					Num_list.append(num)
					Name1_list.append(dam_num)
					Name1_list.append(station_num)
					Name1_list.append(device_num)
					Name1_list.append('1')
					Name1_list=','.join(Name1_list)
					Name_list.append(Name1_list)
				#平均
				if average =="是":
					d3_list = []
					for d in Average_list:
						d3_list.append(d.d)
						Data_list.append(d.d)
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					num = len(d3_list)#计算list元素个数
					Num_list.append(num)
					Name3_list.append(dam_num)
					Name3_list.append(station_num)
					Name3_list.append(device_num)
					Name3_list.append('3')
					Name3_list=','.join(Name3_list)#合并字符串	
					Name_list.append(Name3_list)
				#收敛
				if convergence =="是":
					d4_list = []
					for d in DPast_list:
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						if station_num == "0":
							d4_list.append(d.d1)
							Data_list.append(d.d1)
						elif station_num == "1":
							d4_list.append(d.d2)
							Data_list.append(d.d2)
						elif station_num == "2":
							d4_list.append(d.d3)
							Data_list.append(d.d3)
						elif station_num == "3":
							d4_list.append(d.d4)
							Data_list.append(d.d4)
					num = len(d4_list)
					Num_list.append(num)
					Name4_list.append(dam_num)
					Name4_list.append(station_num)
					Name4_list.append(device_num)
					Name4_list.append('4')
					Name4_list=','.join(Name4_list)
					Name_list.append(Name4_list)
				#平滑
				if smooth =="是":
					d5_list = []
					for d in Dping_list:
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						if station_num == "0":
							d5_list.append(d.d1)
							Data_list.append(d.d1)
						elif station_num == "1":
							d5_list.append(d.d2)
							Data_list.append(d.d2)
						elif station_num == "2":
							d5_list.append(d.d3)
							Data_list.append(d.d3)
						elif station_num == "3":
							d5_list.append(d.d4)
							Data_list.append(d.d4)
					num = len(d5_list)
					Num_list.append(num)
					Name5_list.append(dam_num)
					Name5_list.append(station_num)
					Name5_list.append(device_num)
					Name5_list.append('5')
					Name5_list=','.join(Name5_list)
					Name_list.append(Name5_list)
			#S1E1&S3E3
			elif (Convergence_time <= start<=end<= Convergence_his_start_time) or (Convergence_his_end_time<=start):
				print('S1E1&S3E3')

				#收敛
				Convergence_list = Convergence_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,stationID = station_num)
				#平滑
				Smooth_list = Smooth_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,stationID = station_num)
				#平均
				Average_list = Average_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,stationID = station_num)		
				
				#温度
				if temperature == "是":
					temperature_list = []
					for t in Average_list:
						temperature_list.append(t.temperature)
						Data_list.append(t.temperature)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					#print(temperature_list)
					num = len(temperature_list)
					Num_list.append(num)
					Name1_list.append(dam_num)
					Name1_list.append(station_num)
					Name1_list.append(device_num)
					Name1_list.append('1')
					Name1_list=','.join(Name1_list)
					Name_list.append(Name1_list)
				#平均
				if average =="是":
					d3_list = []
					for d in Average_list:
						d3_list.append(d.d)
						Data_list.append(d.d)
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					num = len(d3_list)#计算list元素个数
					Num_list.append(num)
					Name3_list.append(dam_num)
					Name3_list.append(station_num)
					Name3_list.append(device_num)
					Name3_list.append('3')
					Name3_list=','.join(Name3_list)#合并字符串	
					Name_list.append(Name3_list)
				#收敛
				if convergence =="是":
					d4_list = []
					for d_his in Convergence_list:
						Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d4_list.append(d_his.d)
						Data_list.append(d_his.d)
					num = len(d4_list)
					Num_list.append(num)
					Name4_list.append(dam_num)	
					Name4_list.append(station_num)
					Name4_list.append(device_num)
					Name4_list.append('4')
					Name4_list=','.join(Name4_list)
					Name_list.append(Name4_list)				
				#平滑
				if smooth =="是":
					d5_list = []
					for d_his in Smooth_list:
						Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d5_list.append(d_his.d)
						Data_list.append(d_his.d)
					num = len(d5_list)
					Num_list.append(num)
					Name5_list.append(dam_num)
					Name5_list.append(station_num)
					Name5_list.append(device_num)
					Name5_list.append('5')
					Name5_list=','.join(Name5_list)
					Name_list.append(Name5_list)
			#S1E2
			elif Convergence_time<= start<= Convergence_his_start_time<=end<=Convergence_his_end_time:
				print('S1E2')
				#收敛
				Convergence_list = Convergence_data.objects.filter(dreal_update_time__range=(start, Convergence_his_start_time)).filter(device = device_list,stationID = station_num)
				#平滑
				Smooth_list = Smooth_data.objects.filter(dreal_update_time__range=(start, Convergence_his_start_time)).filter(device = device_list,stationID = station_num)
				#平均
				Average_list = Average_data.objects.filter(dreal_update_time__range=(start, Convergence_his_start_time)).filter(device = device_list,stationID = station_num)		
				
				#收敛
				Convergence_list_his = Convergence_data_his.objects.filter(dreal_update_time__range=(Convergence_his_start_time, end)).filter(device = device_list,stationID = station_num)
				#平滑
				Smooth_list_his = Smooth_data_his.objects.filter(dreal_update_time__range=(Convergence_his_start_time, end)).filter(device = device_list,stationID = station_num)
				#平均
				Average_list_his = Average_data_his.objects.filter(dreal_update_time__range=(Convergence_his_start_time, end)).filter(device = device_list,stationID = station_num)		
				
				#温度
				if temperature == "是":
					temperature_list = []
					for t in Average_list:
						temperature_list.append(t.temperature)
						Data_list.append(t.temperature)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					for t in Average_list_his:
						temperature_list.append(t.temperature)
						Data_list.append(t.temperature)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					#print(temperature_list)
					num = len(temperature_list)
					Num_list.append(num)
					Name1_list.append(dam_num)
					Name1_list.append(station_num)
					Name1_list.append(device_num)
					Name1_list.append('1')
					Name1_list=','.join(Name1_list)
					Name_list.append(Name1_list)
				#平均
				if average =="是":
					d3_list = []
					for d in Average_list:
						d3_list.append(d.d)
						Data_list.append(d.d)
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					for d in Average_list_his:
						d3_list.append(d.d)
						Data_list.append(d.d)
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					num = len(d3_list)#计算list元素个数
					Num_list.append(num)
					Name3_list.append(dam_num)
					Name3_list.append(station_num)
					Name3_list.append(device_num)
					Name3_list.append('3')
					Name3_list=','.join(Name3_list)#合并字符串	
					Name_list.append(Name3_list)
				#收敛
				if convergence =="是":
					d4_list = []
					for d in Convergence_list:
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d4_list.append(d.d)
						Data_list.append(d.d)
					for d_his in Convergence_list_his:
						Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d4_list.append(d_his.d)
						Data_list.append(d_his.d)
					num = len(d4_list)
					Num_list.append(num)
					Name4_list.append(dam_num)	
					Name4_list.append(station_num)
					Name4_list.append(device_num)
					Name4_list.append('4')
					Name4_list=','.join(Name4_list)
					Name_list.append(Name4_list)	

				#平滑
				if smooth =="是":
					d5_list = []
					for d in Smooth_list:
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d5_list.append(d.d)
						Data_list.append(d.d)
					for d_his in Smooth_list_his:
						Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d5_list.append(d_his.d)
						Data_list.append(d_his.d)
					num = len(d5_list)
					Num_list.append(num)
					Name5_list.append(dam_num)
					Name5_list.append(station_num)
					Name5_list.append(device_num)
					Name5_list.append('5')
					Name5_list=','.join(Name5_list)
					Name_list.append(Name5_list)
			#S1E3
			elif Convergence_time<= start<= Convergence_his_start_time<=Convergence_his_end_time<=end:
				print('S1E3')
				#收敛
				Convergence_list = Convergence_data.objects.filter(dreal_update_time__range=(start, Convergence_his_start_time)).filter(device = device_list,stationID = station_num)
				#平滑
				Smooth_list = Smooth_data.objects.filter(dreal_update_time__range=(start, Convergence_his_start_time)).filter(device = device_list,stationID = station_num)
				#平均
				Average_list= Average_data.objects.filter(dreal_update_time__range=(start, Convergence_his_start_time)).filter(device = device_list,stationID = station_num)		
				
				#收敛
				Convergence_list_his = Convergence_data_his.objects.filter(dreal_update_time__range=(Convergence_his_start_time, Convergence_his_end_time)).filter(device = device_list,stationID = station_num)
				#平滑
				Smooth_list_his = Smooth_data_his.objects.filter(dreal_update_time__range=(Convergence_his_start_time, Convergence_his_end_time)).filter(device = device_list,stationID = station_num)
				#平均
				Average_list_his = Average_data_his.objects.filter(dreal_update_time__range=(Convergence_his_start_time, Convergence_his_end_time)).filter(device = device_list,stationID = station_num)		
				
				#收敛
				Convergence_list_2 = Convergence_data.objects.filter(dreal_update_time__range=(Convergence_his_end_time, end)).filter(device = device_list,stationID = station_num)
				#平滑
				Smooth_list_2 = Smooth_data.objects.filter(dreal_update_time__range=(Convergence_his_end_time, end)).filter(device = device_list,stationID = station_num)
				#平均
				Average_list_2 = Average_data.objects.filter(dreal_update_time__range=(Convergence_his_end_time, end)).filter(device = device_list,stationID = station_num)		
				
				#温度
				if temperature == "是":
					temperature_list = []
					for t in Average_list:
						temperature_list.append(t.temperature)
						Data_list.append(t.temperature)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					for t in Average_list_his:
						temperature_list.append(t.temperature)
						Data_list.append(t.temperature)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					for t in Average_list_2:
						temperature_list.append(t.temperature)
						Data_list.append(t.temperature)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					#print(temperature_list)
					num = len(temperature_list)
					Num_list.append(num)
					Name1_list.append(dam_num)
					Name1_list.append(station_num)
					Name1_list.append(device_num)
					Name1_list.append('1')
					Name1_list=','.join(Name1_list)
					Name_list.append(Name1_list)
				#平均
				if average =="是":
					d3_list = []
					for d in Average_list:
						d3_list.append(d.d)
						Data_list.append(d.d)
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					for d in Average_list_his:
						d3_list.append(d.d)
						Data_list.append(d.d)
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					for d in Average_list_2:
						d3_list.append(d.d)
						Data_list.append(d.d)
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					num = len(d3_list)#计算list元素个数
					Num_list.append(num)
					Name3_list.append(dam_num)
					Name3_list.append(station_num)
					Name3_list.append(device_num)
					Name3_list.append('3')
					Name3_list=','.join(Name3_list)#合并字符串	
					Name_list.append(Name3_list)
				#收敛
				if convergence =="是":
					d4_list = []
					for d in Convergence_list:
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d4_list.append(d.d)
						Data_list.append(d.d)
					for d_his in Convergence_list_his:
						Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d4_list.append(d_his.d)
						Data_list.append(d_his.d)
					for d_2 in Convergence_list_2:
						Time_list.append(d_2.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d4_list.append(d_2.d)
						Data_list.append(d_2.d)
					num = len(d4_list)
					Num_list.append(num)
					Name4_list.append(dam_num)	
					Name4_list.append(station_num)
					Name4_list.append(device_num)
					Name4_list.append('4')
					Name4_list=','.join(Name4_list)
					Name_list.append(Name4_list)				
				#平滑
				if smooth =="是":
					d5_list = []
					for d in Smooth_list:
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d5_list.append(d.d)
						Data_list.append(d.d)
					for d_his in Smooth_list_his:
						Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d5_list.append(d_his.d)
						Data_list.append(d_his.d)
					for d_2 in Smooth_list_2:
						Time_list.append(d_2.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d5_list.append(d_2.d)
						Data_list.append(d_2.d)
					num = len(d5_list)
					Num_list.append(num)
					Name5_list.append(dam_num)
					Name5_list.append(station_num)
					Name5_list.append(device_num)
					Name5_list.append('5')
					Name5_list=','.join(Name5_list)
					Name_list.append(Name5_list)
			#S2E2
			elif Convergence_his_start_time<= start<=end<=Convergence_his_end_time:
				print('S2E2')

				#收敛
				Convergence_list_his = Convergence_data_his.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,stationID = station_num)
				#平滑
				Smooth_list_his = Smooth_data_his.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,stationID = station_num)
				#平均
				Average_list_his = Average_data_his.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,stationID = station_num)		
				
				#温度
				if temperature == "是":
					temperature_list = []
					for t in Average_list_his:
						temperature_list.append(t.temperature)
						Data_list.append(t.temperature)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					#print(temperature_list)
					num = len(temperature_list)
					Num_list.append(num)
					Name1_list.append(dam_num)
					Name1_list.append(station_num)
					Name1_list.append(device_num)
					Name1_list.append('1')
					Name1_list=','.join(Name1_list)
					Name_list.append(Name1_list)
				#平均
				if average =="是":
					d3_list = []
					for d in Average_list_his:
						d3_list.append(d.d)
						Data_list.append(d.d)
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					num = len(d3_list)#计算list元素个数
					Num_list.append(num)
					Name3_list.append(dam_num)
					Name3_list.append(station_num)
					Name3_list.append(device_num)
					Name3_list.append('3')
					Name3_list=','.join(Name3_list)#合并字符串	
					Name_list.append(Name3_list)
				#收敛
				if convergence =="是":
					d4_list = []
					for d_his in Convergence_list_his:
						Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d4_list.append(d_his.d)
						Data_list.append(d_his.d)	
					num = len(d4_list)
					Num_list.append(num)
					Name4_list.append(dam_num)	
					Name4_list.append(station_num)
					Name4_list.append(device_num)
					Name4_list.append('4')
					Name4_list=','.join(Name4_list)
					Name_list.append(Name4_list)				
				#平滑
				if smooth =="是":
					d5_list = []
					for d_his in Smooth_list_his:
						Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d5_list.append(d_his.d)
						Data_list.append(d_his.d)
					num = len(d5_list)
					Num_list.append(num)
					Name5_list.append(dam_num)
					Name5_list.append(station_num)
					Name5_list.append(device_num)
					Name5_list.append('5')
					Name5_list=','.join(Name5_list)
					Name_list.append(Name5_list)
			#S2E3
			elif Convergence_his_start_time<= start<=Convergence_his_end_time<=end:
				print('S2E3')
				print(start)
				print(end)
				#收敛
				Convergence_list_his = Convergence_data_his.objects.filter(dreal_update_time__range=(start, Convergence_his_end_time)).filter(device = device_list,stationID = station_num)
				#平滑
				Smooth_list_his = Smooth_data_his.objects.filter(dreal_update_time__range=(start, Convergence_his_end_time)).filter(device = device_list,stationID = station_num)
				#平均
				Average_list_his = Average_data_his.objects.filter(dreal_update_time__range=(start, Convergence_his_end_time)).filter(device = device_list,stationID = station_num)		
				
				#收敛
				Convergence_list = Convergence_data.objects.filter(dreal_update_time__range=(Convergence_his_end_time, end)).filter(device = device_list,stationID = station_num)
				#平滑
				Smooth_list = Smooth_data.objects.filter(dreal_update_time__range=(Convergence_his_end_time, end)).filter(device = device_list,stationID = station_num)
				#平均
				Average_list= Average_data.objects.filter(dreal_update_time__range=(Convergence_his_end_time, end)).filter(device = device_list,stationID = station_num)		
				
				#温度
				if temperature == "是":
					temperature_list = []
					for t in Average_list_his:
						temperature_list.append(t.temperature)
						Data_list.append(t.temperature)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					for t in Average_list:
						temperature_list.append(t.temperature)
						Data_list.append(t.temperature)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					
					#print(temperature_list)
					num = len(temperature_list)
					Num_list.append(num)
					Name1_list.append(dam_num)
					Name1_list.append(station_num)
					Name1_list.append(device_num)
					Name1_list.append('1')
					Name1_list=','.join(Name1_list)
					Name_list.append(Name1_list)
				#平均
				if average =="是":
					d3_list = []
					for d in Average_list_his:
						d3_list.append(d.d)
						Data_list.append(d.d)
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					for d in Average_list:
						d3_list.append(d.d)
						Data_list.append(d.d)
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					num = len(d3_list)#计算list元素个数
					Num_list.append(num)
					Name3_list.append(dam_num)
					Name3_list.append(station_num)
					Name3_list.append(device_num)
					Name3_list.append('3')
					Name3_list=','.join(Name3_list)#合并字符串	
					Name_list.append(Name3_list)
				#收敛
				if convergence =="是":
					d4_list = []
					for d_his in Convergence_list_his:
						Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d4_list.append(d_his.d)
						Data_list.append(d_his.d)
					for d in Convergence_list:
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d4_list.append(d.d)
						Data_list.append(d.d)
					
					num = len(d4_list)
					Num_list.append(num)
					Name4_list.append(dam_num)	
					Name4_list.append(station_num)
					Name4_list.append(device_num)
					Name4_list.append('4')
					Name4_list=','.join(Name4_list)
					Name_list.append(Name4_list)				
				#平滑
				if smooth =="是":
					d5_list = []
					for d_his in Smooth_list_his:
						Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d5_list.append(d_his.d)
						Data_list.append(d_his.d)
					for d in Smooth_list:
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d5_list.append(d.d)
						Data_list.append(d.d)
					
					num = len(d5_list)
					Num_list.append(num)
					Name5_list.append(dam_num)
					Name5_list.append(station_num)
					Name5_list.append(device_num)
					Name5_list.append('5')
					Name5_list=','.join(Name5_list)
					Name_list.append(Name5_list)
					


			#坐标
			if XYZ== "是":				
				d6_list = []
				d7_list = []
				d8_list = []
				DPast_list = DPast.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
				for t in DPast_list:
					Data_list.append(t.x)
					d6_list.append(t.x)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
				for t in DPast_list:
					Data_list.append(t.y)
					d7_list.append(t.y)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
				for t in DPast_list:
					Data_list.append(t.z)
					d8_list.append(t.z)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
				
				num = len(d6_list)
				Num_list.append(num)
				Name6_list.append(dam_num)
				Name6_list.append(station_num)
				Name6_list.append(device_num)
				Name6_list.append('6')
				Name6_list=','.join(Name6_list)
				Name_list.append(Name6_list)

				num = len(d7_list)
				Num_list.append(num)
				Name7_list.append(dam_num)
				Name7_list.append(station_num)
				Name7_list.append(device_num)
				Name7_list.append('7')
				Name7_list=','.join(Name7_list)
				Name_list.append(Name7_list)

				num = len(d8_list)
				Num_list.append(num)
				Name8_list.append(dam_num)
				Name8_list.append(station_num)
				Name8_list.append(device_num)
				Name8_list.append('8')
				Name8_list=','.join(Name8_list)
				Name_list.append(Name8_list)

			
			#print(Data_list)
			#print(Time_list)
			print(Name_list)
			#print(Num_list)	

			return render(request, 'label_detail_history.html', {'Data_list': json.dumps(Data_list),'Time_list': json.dumps(Time_list),'Name_list': json.dumps(Name_list),'Num_list': json.dumps(Num_list)})
		else:
			return render(request, 'list_show_realTime.html')	
	else:
		return render(request, 'login.html')		


#历史位移查看
def DPast_management_sametime(request):
	if request.session.get('userName'):
		if request.method == "POST":
			time_ymd = request.POST.getlist('reservationtime[]')
			time_hms_start = request.POST.get('start_time')
			time_hms_end = request.POST.get('end_time')
			dam_num = request.POST.get('dam_num_2')
			device_num = request.POST.getlist('device_num[]')
			station_num = request.POST.getlist('station_num[]')
			average = request.POST.getlist('d1_num[]')
			convergence = request.POST.getlist('d2_num[]')
			smooth = request.POST.getlist('d3_num[]')
			XYZ = request.POST.getlist('coor_num[]')
			#dam_num = "123"
			temperature = request.POST.getlist('temperature_num[]')

			#print(dam_num)
			#print(len(temperature)) 
			#print(time_hms_start)
			#print(time_hms_end)
			num = len(station_num)
			Data_list = []
			Name_list = [] 
			Num_list = [] 
			Time_list = []
			#遍历基站列表取出时间段个数
			for index in range(num):
				#取出时间的每天
				date_list = []
				begin_date = datetime.datetime.strptime(time_ymd[index][0:10], "%Y-%m-%d")
				end_date = datetime.datetime.strptime(time_ymd[index][-10:], "%Y-%m-%d")
				while begin_date <= end_date:
					date_str = begin_date.strftime("%Y-%m-%d")
					date_list.append(date_str)
					begin_date += datetime.timedelta(days=1)
				#print (date_list)
				#整合时间代码

				time_list_start =[]
				time_ymd_1=time_ymd[index][0:10]
				time_ymd_2=time_ymd[index][-10:]
				time_list_start.append(time_ymd_1)
				time_list_start.append(time_hms_start)
				start_1 =' '.join(time_list_start)
				#print(start_1)
				time_list_start =[]
				time_list_start.append(time_ymd_2)
				time_list_start.append(time_hms_end)
				end_1=' '.join(time_list_start)
				#print(start_1)



				Convergence_time = ('2018-08-06 23:59:59')
				Convergence_his_start_time = ('2018-08-22 23:59:59')
				Convergence_his_end_time = ('2018-09-08 21:27:00')

				Name1_list = [] 
				Name3_list = []
				Name4_list = []
				Name5_list = []
				Name6_list = []
				Name7_list = []
				Name8_list = []

				dam_list = Dam.objects.get(dam_num = dam_num)
				device_list = Device.objects.filter(device_num = device_num[index],at_tip =  1,dam = dam_list)
				#S0_E0
				if end_1 < Convergence_time:
					DPast_list = DPast.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list)
					Dping_list = Dping.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list)
					#收敛
					if convergence[index] =="是":
						d4_list = []
						for d in DPast_list:
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							if station_num[index] == "0":
								d4_list.append(d.d1)
								Data_list.append(d.d1)
							elif station_num[index] == "1":
								d4_list.append(d.d2)
								Data_list.append(d.d2)
							elif station_num[index] == "2":
								d4_list.append(d.d3)
								Data_list.append(d.d3)
							elif station_num[index] == "3":
								d4_list.append(d.d4)
								Data_list.append(d.d4)
						num = len(d4_list)
						Num_list.append(num)
						Name4_list.append(dam_num)
						Name4_list.append(station_num[index])
						Name4_list.append(device_num[index])
						Name4_list.append('4')
						Name4_list=','.join(Name4_list)
						Name_list.append(Name4_list)
					#平滑
					if smooth[index] =="是":
						d5_list = []
						for d in Dping_list:
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							if station_num[index] == "0":
								d5_list.append(d.d1)
								Data_list.append(d.d1)
							elif station_num[index] == "1":
								d5_list.append(d.d2)
								Data_list.append(d.d2)
							elif station_num[index] == "2":
								d5_list.append(d.d3)
								Data_list.append(d.d3)
							elif station_num[index] == "3":
								d5_list.append(d.d4)
								Data_list.append(d.d4)
						num = len(d5_list)
						Num_list.append(num)
						Name5_list.append(dam_num)
						Name5_list.append(station_num[index])
						Name5_list.append(device_num[index])
						Name5_list.append('5')
						Name5_list=','.join(Name5_list)
						Name_list.append(Name5_list)

				#S1E1&S3E3
				elif (Convergence_time <= start_1  <= Convergence_his_start_time) or (Convergence_his_end_time<=start_1):
					print('S3E3')
					#收敛
					Convergence_list = Convergence_data.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list,stationID = station_num[index]).values("dreal_update_time","d")
					#平滑
					Smooth_list = Smooth_data.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list,stationID = station_num[index]).values("dreal_update_time","d")
					#平均
					Average_list = Average_data.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list,stationID= station_num[index]).values("temperature","dreal_update_time","d")
					#温度
					
					if temperature[index] =="是":
						print('执行判断中1')
						Data_list_all = []
						Time_list_all = []
						for t in Average_list:
							Data_list_all.append(t["temperature"])
							Time_list_all.append(t["dreal_update_time"].strftime("%Y-%m-%d %H:%M:%S"))
						print('温度FOR查询完成')
						Name1_list.append(dam_num)
						Name1_list.append(station_num[index])#基站编号
						Name1_list.append(device_num[index])#标签编号
						Name1_list.append('1')
						Name1_list=','.join(Name1_list)	
						for t in date_list:
							time_list_start =[]
							time_list_start.append(t)
							time_list_start.append(time_hms_start)
							start_1_1 =' '.join(time_list_start)
							#print(start_1_1)
							time_list_start =[]
							time_list_start.append(t)
							time_list_start.append(time_hms_end)
							end_1_1=' '.join(time_list_start)
						#	print(end_1_1)
						
							Time_list_1 = []
							for i in Time_list_all:
								if start_1_1<=i<=end_1_1:
									Time_list_1.append(i)

							if len(Time_list_1) <2:
								Data_list=Data_list
								Time_list = Time_list
							else:
								c = Time_list_all.index(Time_list_1[0])
								d = Time_list_all.index(Time_list_1[-1])
								Data_list_1=Data_list_all[c:d+1]
								Data_list=Data_list+Data_list_1
								Time_list = Time_list+Time_list_1


							Num_list.append(len(Time_list_1))	

							Name_list.append(Name1_list)

						print('温度查询完成')
						#Name1_list.clear()
					#平均
					if average[index] =="是":
						print('执行判断中2')
						Data_list_all = []
						Time_list_all = []
						for d in Average_list:
							Data_list_all.append(d["d"])
							Time_list_all.append(d["dreal_update_time"].strftime("%Y-%m-%d %H:%M:%S"))
						print('平均FOR查询完成')

						Name3_list.append(dam_num)
						Name3_list.append(station_num[index])
						Name3_list.append(device_num[index])
						Name3_list.append('3')
						Name3_list=','.join(Name3_list)#合并字符串	

						for t in date_list:
							time_list_start =[]
							time_list_start.append(t)
							time_list_start.append(time_hms_start)
							start_1_1 =' '.join(time_list_start)
							#print(start_1_1)
							time_list_start =[]
							time_list_start.append(t)
							time_list_start.append(time_hms_end)
							end_1_1=' '.join(time_list_start)
							#print(end_1_1)
						
							Time_list_1 = []
							for i in Time_list_all:
								if start_1_1<=i<=end_1_1:
									Time_list_1.append(i)
							if len(Time_list_1) <2:
								Data_list=Data_list
								Time_list = Time_list
							else:
								c = Time_list_all.index(Time_list_1[0])
								d = Time_list_all.index(Time_list_1[-1])
								Data_list_1=Data_list_all[c:d+1]
								Data_list=Data_list+Data_list_1
								Time_list = Time_list+Time_list_1

							Num_list.append(len(Time_list_1))	


							Name_list.append(Name3_list)
						print('平均查询完成')

					#收敛
					if convergence[index] =="是":
						print('执行判断中3')
						Data_list_all = []
						Time_list_all = []
						for d in Convergence_list:
							Data_list_all.append(d["d"])
							Time_list_all.append(d["dreal_update_time"].strftime("%Y-%m-%d %H:%M:%S"))
						print('收敛fOR查询完成')	
						Name4_list.append(dam_num)	
						Name4_list.append(station_num[index])
						Name4_list.append(device_num[index])
						Name4_list.append('4')
						Name4_list=','.join(Name4_list)
						for t in date_list:
							time_list_start =[]
							time_list_start.append(t)
							time_list_start.append(time_hms_start)
							start_1_1 =' '.join(time_list_start)
							#print(start_1_1)
							time_list_start =[]
							time_list_start.append(t)
							time_list_start.append(time_hms_end)
							end_1_1=' '.join(time_list_start)
							#print(end_1_1)
						
							Time_list_1 = []
							for i in Time_list_all:
								if start_1_1<=i<=end_1_1:
									Time_list_1.append(i)
							if len(Time_list_1) <2:
								Data_list=Data_list
								Time_list = Time_list
							else:
								c = Time_list_all.index(Time_list_1[0])
								d = Time_list_all.index(Time_list_1[-1])
								Data_list_1=Data_list_all[c:d+1]
								Data_list=Data_list+Data_list_1
								Time_list = Time_list+Time_list_1

							Num_list.append(len(Time_list_1))	

							Name_list.append(Name4_list)	
						print('收敛查询完成')			
					#平滑
					if smooth[index] =="是":
						print('执行判断中4')
						Data_list_all = []
						Time_list_all = []
						for d in Smooth_list:
							#d5_list.append(d["d"])
							Data_list_all.append(d["d"])
							Time_list_all.append(d["dreal_update_time"].strftime("%Y-%m-%d %H:%M:%S"))
						print('平滑FOR查询完成')
						Name5_list.append(dam_num)
						Name5_list.append(station_num[index])
						Name5_list.append(device_num[index])
						Name5_list.append('5')
						Name5_list=','.join(Name5_list)
						for t in date_list:
							time_list_start =[]
							time_list_start.append(t)
							time_list_start.append(time_hms_start)
							start_1_1 =' '.join(time_list_start)
						#	print(start_1_1)
							time_list_start =[]
							time_list_start.append(t)
							time_list_start.append(time_hms_end)
							end_1_1=' '.join(time_list_start)
						#	print(end_1_1)
						
							Time_list_1 = []
							for i in Time_list_all:
								if start_1_1<=i<=end_1_1:
									Time_list_1.append(i)
							if len(Time_list_1) <2:
								Data_list=Data_list
								Time_list = Time_list
							else:
								c = Time_list_all.index(Time_list_1[0])
								d = Time_list_all.index(Time_list_1[-1])
								Data_list_1=Data_list_all[c:d+1]
								Data_list=Data_list+Data_list_1
								Time_list = Time_list+Time_list_1

							Num_list.append(len(Time_list_1))	
						
							Name_list.append(Name5_list)
						print('平滑查询完成')
				#S2E2
				elif Convergence_his_start_time<=start_1<=Convergence_his_end_time:
					print('S2E2')
					#收敛_his
					Convergence_list_his = Convergence_data_his.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list,stationID = station_num[index])
					#平滑_his
					Smooth_list_his = Smooth_data_his.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list,stationID = station_num[index])
					#平均
					Average_list_his = Average_data_his.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list,stationID= station_num[index])
					#温度
					if temperature[index] == "是":
						temperature_list = []
						for t in Average_list_his:
							temperature_list.append(t.temperature)
							Data_list.append(t.temperature)
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						print(temperature_list)
						num = len(temperature_list)
						Num_list.append(num)
						Name1_list.append(dam_num)
						Name1_list.append(station_num[index])
						Name1_list.append(device_num[index])
						Name1_list.append('1')
						Name1_list=','.join(Name1_list)
						Name_list.append(Name1_list)		
					#平均
					if average[index] =="是":
						d3_list = []
						for d in Average_list_his:
							d3_list.append(d.d)
							Data_list.append(d.d)
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						num = len(d3_list)#计算list元素个数
						Num_list.append(num)
						Name3_list.append(dam_num)
						Name3_list.append(station_num[index])
						Name3_list.append(device_num[index])
						Name3_list.append('3')
						Name3_list=','.join(Name3_list)#合并字符串	
						Name_list.append(Name3_list)
					#收敛
					if convergence[index] =="是":
						d4_list = []
						for d_his in Convergence_list_his:
							Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d4_list.append(d_his.d)
							Data_list.append(d_his.d)
						num = len(d4_list)
						Num_list.append(num)
						Name4_list.append(dam_num)	
						Name4_list.append(station_num[index])
						Name4_list.append(device_num[index])	
						Name4_list.append('4')
						Name4_list=','.join(Name4_list)
						Name_list.append(Name4_list)				
					#平滑
					if smooth[index] =="是":
						d5_list = []
						for d_his in Smooth_list_his:
							Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d5_list.append(d_his.d)
							Data_list.append(d_his.d)
						num = len(d5_list)
						Num_list.append(num)
						Name5_list.append(dam_num)
						Name5_list.append(station_num[index])
						Name5_list.append(device_num[index])
						Name5_list.append('5')
						Name5_list=','.join(Name5_list)
						Name_list.append(Name5_list)

				#坐标
				if XYZ[index] == "是":				
					Data_list_all = []
					Time_list_all = []
					Data_list_all_1 = []
					Time_list_all_1 = []
					Data_list_all_2 = []
					Time_list_all_2 = []
					DPast_list = DPast.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list).values("x","y","z","dreal_update_time")
					for t in DPast_list:
						Data_list_all.append(t["x"])
						Time_list_all.append(t["dreal_update_time"].strftime("%Y-%m-%d %H:%M:%S"))
					for t in DPast_list:
						Data_list_all_1.append(t["y"])
						Time_list_all_1.append(t["dreal_update_time"].strftime("%Y-%m-%d %H:%M:%S"))
					for t in DPast_list:
						Data_list_all_2.append(t["z"])
						Time_list_all_2.append(t["dreal_update_time"].strftime("%Y-%m-%d %H:%M:%S"))

						'''for i in range(len(XYZ_list)):
							XYZ_list[i] = str(XYZ_list[i])
						XYZ_list=','.join(XYZ_list)
						d6_list.append(XYZ_list)	
						Data_list = Data_list + d6_list'''
					Name6_list.append(dam_num)
					Name6_list.append(station_num[index])
					Name6_list.append(device_num[index])
					Name6_list.append('6')
					Name6_list=','.join(Name6_list)	
					for t in date_list:
						time_list_start =[]
						time_list_start.append(t)
						time_list_start.append(time_hms_start)
						start_1_1 =' '.join(time_list_start)
						print(start_1_1)
						time_list_start =[]
						time_list_start.append(t)
						time_list_start.append(time_hms_end)
						end_1_1=' '.join(time_list_start)
						print(end_1_1)
					
						Time_list_1 = []
						for i in Time_list_all:
							if start_1_1<=i<=end_1_1:
								Time_list_1.append(i)
						if len(Time_list_1) <2:
							Data_list=Data_list
							Time_list = Time_list
						else:
							c = Time_list_all.index(Time_list_1[0])
							d = Time_list_all.index(Time_list_1[-1])
							Data_list_1=Data_list_all[c:d+1]
							Data_list=Data_list+Data_list_1
							Time_list = Time_list+Time_list_1

						Num_list.append(len(Time_list_1))

					
						Name_list.append(Name6_list)

					Name7_list.append(dam_num)
					Name7_list.append(station_num[index])
					Name7_list.append(device_num[index])
					Name7_list.append('7')
					Name7_list=','.join(Name7_list)
					for t in date_list:
						time_list_start =[]
						time_list_start.append(t)
						time_list_start.append(time_hms_start)
						start_1_1 =' '.join(time_list_start)
						print(start_1_1)
						time_list_start =[]
						time_list_start.append(t)
						time_list_start.append(time_hms_end)
						end_1_1=' '.join(time_list_start)
						print(end_1_1)
					
						Time_list_1 = []
						for i in Time_list_all_1:
							if start_1_1<=i<=end_1_1:
								Time_list_1.append(i)
						if len(Time_list_1) <2:
							Data_list=Data_list
							Time_list = Time_list
						else:
							c = Time_list_all_1.index(Time_list_1[0])
							d = Time_list_all_1.index(Time_list_1[-1])
							Data_list_1=Data_list_all_1[c:d+1]
							Data_list=Data_list+Data_list_1
							Time_list = Time_list+Time_list_1


						Num_list.append(len(Time_list_1))
						Name_list.append(Name7_list)

					Name8_list.append(dam_num)
					Name8_list.append(station_num[index])
					Name8_list.append(device_num[index])
					Name8_list.append('8')
					Name8_list=','.join(Name8_list)
					for t in date_list:
						time_list_start =[]
						time_list_start.append(t)
						time_list_start.append(time_hms_start)
						start_1_1 =' '.join(time_list_start)
						#print(start_1_1)
						time_list_start =[]
						time_list_start.append(t)
						time_list_start.append(time_hms_end)
						end_1_1=' '.join(time_list_start)
						#print(end_1_1)
					
						Time_list_1 = []
						for i in Time_list_all_2:
							if start_1_1<=i<=end_1_1:
								Time_list_1.append(i)
						if len(Time_list_1) <2:
							Data_list=Data_list
							Time_list = Time_list
						else:
							c = Time_list_all_2.index(Time_list_1[0])
							d = Time_list_all_2.index(Time_list_1[-1])
							Data_list_1=Data_list_all_2[c:d+1]
							Data_list=Data_list+Data_list_1
							Time_list = Time_list+Time_list_1


						Num_list.append(len(Time_list_1))
						Name_list.append(Name8_list)
						
			#print(Data_list)
			#print(Time_list)
			#print(Name_list)
			#print(Num_list)

				

			return render(request, 'label_detail_history_sametime.html', {'Data_list': json.dumps(Data_list),'Time_list': json.dumps(Time_list),'Name_list': json.dumps(Name_list),'Num_list': json.dumps(Num_list)})
		else:
			return render(request, 'history_search.html')
	else:
		return render(request, 'login.html')
#历史位移查看
def DPast_management(request):
	if request.session.get('userName'):
		if request.method == "POST":
			time = request.POST.getlist('reservationtime[]')
			dam_num = request.POST.get('dam_num_1')
			device_num = request.POST.getlist('device_num[]')
			station_num = request.POST.getlist('station_num[]')
			average = request.POST.getlist('d1_num[]')
			convergence = request.POST.getlist('d2_num[]')
			smooth = request.POST.getlist('d3_num[]')
			XYZ = request.POST.getlist('coor_num[]')
			temperature = request.POST.getlist('temperature_num[]')
			num = len(station_num)
			Data_list = []
			Name_list = [] 
			Num_list = [] 
			Time_list = []
			for index in range(num):
				start =time[index][0:16]
				end = time[index][-16:]

				Convergence_time = ('2018-08-06 23:59:59')
				Convergence_his_start_time = ('2018-08-22 23:59:59')
				Convergence_his_end_time = ('2018-09-08 21:27:00')

				Name1_list = [] 
				Name2_list = [] 
				Name3_list = []
				Name4_list = []
				Name5_list = []
				Name6_list = []
				Name7_list = []
				Name8_list = []

				dam_list = Dam.objects.get(dam_num = dam_num)
				device_list = Device.objects.filter(device_num = device_num[index],at_tip =  1,dam = dam_list )
				#S0E0
				if end <= Convergence_time:
					print('S0E0')

					#收敛
					DPast_list = DPast.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
					#平滑
					Dping_list = Dping.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
					#平均
					Average_list = Average_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,stationID = station_num[index])		
					
					#温度
					if temperature[index] == "是":
						temperature_list = []
						for t in Average_list:
							temperature_list.append(t.temperature)
							Data_list.append(t.temperature)
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						#print(temperature_list)
						num = len(temperature_list)
						Num_list.append(num)
						Name1_list.append(dam_num)
						Name1_list.append(station_num[index])
						Name1_list.append(device_num[index])
						Name1_list.append('1')
						Name1_list=','.join(Name1_list)
						Name_list.append(Name1_list)
					#平均
					if average[index] =="是":
						d3_list = []
						for d in Average_list:
							d3_list.append(d.d)
							Data_list.append(d.d)
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						num = len(d3_list)#计算list元素个数
						Num_list.append(num)
						Name3_list.append(dam_num)
						Name3_list.append(station_num[index])
						Name3_list.append(device_num[index])
						Name3_list.append('3')
						Name3_list=','.join(Name3_list)#合并字符串	
						Name_list.append(Name3_list)
					#收敛
					if convergence[index] =="是":
						d4_list = []
						for d in DPast_list:
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							if station_num[index] == "0":
								d4_list.append(d.d1)
								Data_list.append(d.d1)
							elif station_num[index] == "1":
								d4_list.append(d.d2)
								Data_list.append(d.d2)
							elif station_num[index] == "2":
								d4_list.append(d.d3)
								Data_list.append(d.d3)
							elif station_num[index] == "3":
								d4_list.append(d.d4)
								Data_list.append(d.d4)
						num = len(d4_list)
						Num_list.append(num)
						Name4_list.append(dam_num)
						Name4_list.append(station_num[index])
						Name4_list.append(device_num[index])
						Name4_list.append('4')
						Name4_list=','.join(Name4_list)
						Name_list.append(Name4_list)
					#平滑
					if smooth[index] =="是":
						d5_list = []
						for d in Dping_list:
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							if station_num[index] == "0":
								d5_list.append(d.d1)
								Data_list.append(d.d1)
							elif station_num[index] == "1":
								d5_list.append(d.d2)
								Data_list.append(d.d2)
							elif station_num[index] == "2":
								d5_list.append(d.d3)
								Data_list.append(d.d3)
							elif station_num[index] == "3":
								d5_list.append(d.d4)
								Data_list.append(d.d4)
						num = len(d5_list)
						Num_list.append(num)
						Name5_list.append(dam_num)
						Name5_list.append(station_num[index])
						Name5_list.append(device_num[index])
						Name5_list.append('5')
						Name5_list=','.join(Name5_list)
						Name_list.append(Name5_list)
				#S1E1&S3E3
				elif (Convergence_time <= start<=end<= Convergence_his_start_time) or (Convergence_his_end_time<=start):
					print('S1E1&S3E3')

					#收敛
					Convergence_list = Convergence_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,stationID = station_num[index]).values("dreal_update_time","d")
					#平滑
					Smooth_list = Smooth_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,stationID = station_num[index]).values("dreal_update_time","d")
					#平均
					Average_list = Average_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,stationID= station_num[index]).values("temperature","dreal_update_time","d")		
					
					#温度
					if temperature[index] =="是":
						print('执行判断中1')
						temperature_list = []
						for t in Average_list:
							temperature_list.append(t["temperature"])
							Data_list.append(t["temperature"])
							Time_list.append(t["dreal_update_time"].strftime("%Y-%m-%d %H:%M:%S"))
						print('温度FOR查询完成')
						#print(temperature_list)
						num = len(temperature_list)
						Num_list.append(num)
						Name1_list.append(dam_num)
						Name1_list.append(station_num[index])#基站编号
						Name1_list.append(device_num[index])#标签编号
						Name1_list.append('1')
						Name1_list=','.join(Name1_list)	
						Name_list.append(Name1_list)
						print('温度查询完成')
						#Name1_list.clear()
					#平均
					if average[index] =="是":
						print('执行判断中2')
						d3_list = []
						for d in Average_list:
							d3_list.append(d["d"])
							Data_list.append(d["d"])
							Time_list.append(d["dreal_update_time"].strftime("%Y-%m-%d %H:%M:%S"))
						print('平均FOR查询完成')
						num = len(d3_list)#计算list元素个数
						Num_list.append(num)
						Name3_list.append(dam_num)
						Name3_list.append(station_num[index])
						Name3_list.append(device_num[index])
						Name3_list.append('3')
						Name3_list=','.join(Name3_list)#合并字符串	
						Name_list.append(Name3_list)
						print('平均查询完成')

					#收敛
					if convergence[index] =="是":
						print('执行判断中3')
						d4_list = []
						for d in Convergence_list:
							d4_list.append(d["d"])
							Data_list.append(d["d"])
							Time_list.append(d["dreal_update_time"].strftime("%Y-%m-%d %H:%M:%S"))
						print('收敛fOR查询完成')	
						num = len(d4_list)
						Num_list.append(num)
						Name4_list.append(dam_num)	
						Name4_list.append(station_num[index])
						Name4_list.append(device_num[index])
						Name4_list.append('4')
						Name4_list=','.join(Name4_list)
						Name_list.append(Name4_list)	
						print('收敛查询完成')			
					#平滑
					if smooth[index] =="是":
						print('执行判断中4')
						d5_list = []
						for d in Smooth_list:
							
							d5_list.append(d["d"])
							Data_list.append(d["d"])
							Time_list.append(d["dreal_update_time"].strftime("%Y-%m-%d %H:%M:%S"))
						print('平滑FOR查询完成')
						num = len(d5_list)
						Num_list.append(num)
						Name5_list.append(dam_num)
						Name5_list.append(station_num[index])
						Name5_list.append(device_num[index])
						Name5_list.append('5')
						Name5_list=','.join(Name5_list)
						Name_list.append(Name5_list)
						print('平滑查询完成')
				#S1E2
				elif Convergence_time<= start<= Convergence_his_start_time<=end<=Convergence_his_end_time:
					print('S1E2')
					#收敛
					Convergence_list = Convergence_data.objects.filter(dreal_update_time__range=(start, Convergence_his_start_time)).filter(device = device_list,stationID = station_num[index])
					#平滑
					Smooth_list = Smooth_data.objects.filter(dreal_update_time__range=(start, Convergence_his_start_time)).filter(device = device_list,stationID = station_num[index])
					#平均
					Average_list = Average_data.objects.filter(dreal_update_time__range=(start, Convergence_his_start_time)).filter(device = device_list,stationID = station_num[index])		
					
					#收敛
					Convergence_list_his = Convergence_data_his.objects.filter(dreal_update_time__range=(Convergence_his_start_time, end)).filter(device = device_list,stationID = station_num[index])
					#平滑
					Smooth_list_his = Smooth_data_his.objects.filter(dreal_update_time__range=(Convergence_his_start_time, end)).filter(device = device_list,stationID = station_num[index])
					#平均
					Average_list_his = Average_data_his.objects.filter(dreal_update_time__range=(Convergence_his_start_time, end)).filter(device = device_list,stationID = station_num[index])		
					
					#温度
					if temperature[index] == "是":
						temperature_list = []
						for t in Average_list:
							temperature_list.append(t.temperature)
							Data_list.append(t.temperature)
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						for t in Average_list_his:
							temperature_list.append(t.temperature)
							Data_list.append(t.temperature)
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						#print(temperature_list)
						num = len(temperature_list)
						Num_list.append(num)
						Name1_list.append(dam_num)
						Name1_list.append(station_num[index])
						Name1_list.append(device_num[index])
						Name1_list.append('1')
						Name1_list=','.join(Name1_list)
						Name_list.append(Name1_list)
					#平均
					if average[index] =="是":
						d3_list = []
						for d in Average_list:
							d3_list.append(d.d)
							Data_list.append(d.d)
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						for d in Average_list_his:
							d3_list.append(d.d)
							Data_list.append(d.d)
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						num = len(d3_list)#计算list元素个数
						Num_list.append(num)
						Name3_list.append(dam_num)
						Name3_list.append(station_num[index])
						Name3_list.append(device_num[index])
						Name3_list.append('3')
						Name3_list=','.join(Name3_list)#合并字符串	
						Name_list.append(Name3_list)
					#收敛
					if convergence[index] =="是":
						d4_list = []
						for d in Convergence_list:
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d4_list.append(d.d)
							Data_list.append(d.d)
						for d_his in Convergence_list_his:
							Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d4_list.append(d_his.d)
							Data_list.append(d_his.d)
						num = len(d4_list)
						Num_list.append(num)
						Name4_list.append(dam_num)	
						Name4_list.append(station_num[index])
						Name4_list.append(device_num[index])
						Name4_list.append('4')
						Name4_list=','.join(Name4_list)
						Name_list.append(Name4_list)	

					#平滑
					if smooth[index] =="是":
						d5_list = []
						for d in Smooth_list:
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d5_list.append(d.d)
							Data_list.append(d.d)
						for d_his in Smooth_list_his:
							Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d5_list.append(d_his.d)
							Data_list.append(d_his.d)
						num = len(d5_list)
						Num_list.append(num)
						Name5_list.append(dam_num)
						Name5_list.append(station_num[index])
						Name5_list.append(device_num[index])
						Name5_list.append('5')
						Name5_list=','.join(Name5_list)
						Name_list.append(Name5_list)
				#S1E3
				elif Convergence_time<= start<= Convergence_his_start_time<=Convergence_his_end_time<=end:
					print('S1E3')
					#收敛
					Convergence_list = Convergence_data.objects.filter(dreal_update_time__range=(start, Convergence_his_start_time)).filter(device = device_list,stationID = station_num[index])
					#平滑
					Smooth_list = Smooth_data.objects.filter(dreal_update_time__range=(start, Convergence_his_start_time)).filter(device = device_list,stationID = station_num[index])
					#平均
					Average_list= Average_data.objects.filter(dreal_update_time__range=(start, Convergence_his_start_time)).filter(device = device_list,stationID = station_num[index])		
					
					#收敛
					Convergence_list_his = Convergence_data_his.objects.filter(dreal_update_time__range=(Convergence_his_start_time, Convergence_his_end_time)).filter(device = device_list,stationID = station_num[index])
					#平滑
					Smooth_list_his = Smooth_data_his.objects.filter(dreal_update_time__range=(Convergence_his_start_time, Convergence_his_end_time)).filter(device = device_list,stationID = station_num[index])
					#平均
					Average_list_his = Average_data_his.objects.filter(dreal_update_time__range=(Convergence_his_start_time, Convergence_his_end_time)).filter(device = device_list,stationID = station_num[index])		
					
					#收敛
					Convergence_list_2 = Convergence_data.objects.filter(dreal_update_time__range=(Convergence_his_end_time, end)).filter(device = device_list,stationID = station_num[index])
					#平滑
					Smooth_list_2 = Smooth_data.objects.filter(dreal_update_time__range=(Convergence_his_end_time, end)).filter(device = device_list,stationID = station_num[index])
					#平均
					Average_list_2 = Average_data.objects.filter(dreal_update_time__range=(Convergence_his_end_time, end)).filter(device = device_list,stationID = station_num[index])		
					
					#温度
					if temperature[index] == "是":
						temperature_list = []
						for t in Average_list:
							temperature_list.append(t.temperature)
							Data_list.append(t.temperature)
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						for t in Average_list_his:
							temperature_list.append(t.temperature)
							Data_list.append(t.temperature)
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						for t in Average_list_2:
							temperature_list.append(t.temperature)
							Data_list.append(t.temperature)
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						#print(temperature_list)
						num = len(temperature_list)
						Num_list.append(num)
						Name1_list.append(dam_num)
						Name1_list.append(station_num[index])
						Name1_list.append(device_num[index])
						Name1_list.append('1')
						Name1_list=','.join(Name1_list)
						Name_list.append(Name1_list)
					#平均
					if average[index] =="是":
						d3_list = []
						for d in Average_list:
							d3_list.append(d.d)
							Data_list.append(d.d)
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						for d in Average_list_his:
							d3_list.append(d.d)
							Data_list.append(d.d)
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						for d in Average_list_2:
							d3_list.append(d.d)
							Data_list.append(d.d)
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						num = len(d3_list)#计算list元素个数
						Num_list.append(num)
						Name3_list.append(dam_num)
						Name3_list.append(station_num[index])
						Name3_list.append(device_num[index])
						Name3_list.append('3')
						Name3_list=','.join(Name3_list)#合并字符串	
						Name_list.append(Name3_list)
					#收敛
					if convergence[index] =="是":
						d4_list = []
						for d in Convergence_list:
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d4_list.append(d.d)
							Data_list.append(d.d)
						for d_his in Convergence_list_his:
							Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d4_list.append(d_his.d)
							Data_list.append(d_his.d)
						for d_2 in Convergence_list_2:
							Time_list.append(d_2.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d4_list.append(d_2.d)
							Data_list.append(d_2.d)
						num = len(d4_list)
						Num_list.append(num)
						Name4_list.append(dam_num)	
						Name4_list.append(station_num[index])
						Name4_list.append(device_num[index])
						Name4_list.append('4')
						Name4_list=','.join(Name4_list)
						Name_list.append(Name4_list)				
					#平滑
					if smooth[index] =="是":
						d5_list = []
						for d in Smooth_list:
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d5_list.append(d.d)
							Data_list.append(d.d)
						for d_his in Smooth_list_his:
							Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d5_list.append(d_his.d)
							Data_list.append(d_his.d)
						for d_2 in Smooth_list_2:
							Time_list.append(d_2.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d5_list.append(d_2.d)
							Data_list.append(d_2.d)
						num = len(d5_list)
						Num_list.append(num)
						Name5_list.append(dam_num)
						Name5_list.append(station_num[index])
						Name5_list.append(device_num[index])
						Name5_list.append('5')
						Name5_list=','.join(Name5_list)
						Name_list.append(Name5_list)
				#S2E2
				elif Convergence_his_start_time<= start<=end<=Convergence_his_end_time:
					print('S2E2')

					#收敛
					Convergence_list_his = Convergence_data_his.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,stationID = station_num[index])
					#平滑
					Smooth_list_his = Smooth_data_his.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,stationID = station_num[index])
					#平均
					Average_list_his = Average_data_his.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,stationID = station_num[index])		
					
					#温度
					if temperature[index] == "是":
						temperature_list = []
						for t in Average_list_his:
							temperature_list.append(t.temperature)
							Data_list.append(t.temperature)
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						#print(temperature_list)
						num = len(temperature_list)
						Num_list.append(num)
						Name1_list.append(dam_num)
						Name1_list.append(station_num[index])
						Name1_list.append(device_num[index])
						Name1_list.append('1')
						Name1_list=','.join(Name1_list)
						Name_list.append(Name1_list)
					#平均
					if average[index] =="是":
						d3_list = []
						for d in Average_list_his:
							d3_list.append(d.d)
							Data_list.append(d.d)
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						num = len(d3_list)#计算list元素个数
						Num_list.append(num)
						Name3_list.append(dam_num)
						Name3_list.append(station_num[index])
						Name3_list.append(device_num[index])
						Name3_list.append('3')
						Name3_list=','.join(Name3_list)#合并字符串	
						Name_list.append(Name3_list)
					#收敛
					if convergence[index] =="是":
						d4_list = []
						for d_his in Convergence_list_his:
							Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d4_list.append(d_his.d)
							Data_list.append(d_his.d)	
						num = len(d4_list)
						Num_list.append(num)
						Name4_list.append(dam_num)	
						Name4_list.append(station_num[index])
						Name4_list.append(device_num[index])
						Name4_list.append('4')
						Name4_list=','.join(Name4_list)
						Name_list.append(Name4_list)				
					#平滑
					if smooth[index] =="是":
						d5_list = []
						for d_his in Smooth_list_his:
							Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d5_list.append(d_his.d)
							Data_list.append(d_his.d)
						num = len(d5_list)
						Num_list.append(num)
						Name5_list.append(dam_num)
						Name5_list.append(station_num[index])
						Name5_list.append(device_num[index])
						Name5_list.append('5')
						Name5_list=','.join(Name5_list)
						Name_list.append(Name5_list)
				#S2E3
				elif Convergence_his_start_time<= start<=Convergence_his_end_time<=end:
					print('S2E3')
					print(start)
					print(end)
					#收敛
					Convergence_list_his = Convergence_data_his.objects.filter(dreal_update_time__range=(start, Convergence_his_end_time)).filter(device = device_list,stationID = station_num[index])
					#平滑
					Smooth_list_his = Smooth_data_his.objects.filter(dreal_update_time__range=(start, Convergence_his_end_time)).filter(device = device_list,stationID = station_num[index])
					#平均
					Average_list_his = Average_data_his.objects.filter(dreal_update_time__range=(start, Convergence_his_end_time)).filter(device = device_list,stationID = station_num[index])		
					
					#收敛
					Convergence_list = Convergence_data.objects.filter(dreal_update_time__range=(Convergence_his_end_time, end)).filter(device = device_list,stationID = station_num[index])
					#平滑
					Smooth_list = Smooth_data.objects.filter(dreal_update_time__range=(Convergence_his_end_time, end)).filter(device = device_list,stationID = station_num[index])
					#平均
					Average_list= Average_data.objects.filter(dreal_update_time__range=(Convergence_his_end_time, end)).filter(device = device_list,stationID = station_num[index])		
					
					#温度
					if temperature[index] == "是":
						temperature_list = []
						for t in Average_list_his:
							temperature_list.append(t.temperature)
							Data_list.append(t.temperature)
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						for t in Average_list:
							temperature_list.append(t.temperature)
							Data_list.append(t.temperature)
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						
						#print(temperature_list)
						num = len(temperature_list)
						Num_list.append(num)
						Name1_list.append(dam_num)
						Name1_list.append(station_num[index])
						Name1_list.append(device_num[index])
						Name1_list.append('1')
						Name1_list=','.join(Name1_list)
						Name_list.append(Name1_list)
					#平均
					if average[index] =="是":
						d3_list = []
						for d in Average_list_his:
							d3_list.append(d.d)
							Data_list.append(d.d)
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						for d in Average_list:
							d3_list.append(d.d)
							Data_list.append(d.d)
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						num = len(d3_list)#计算list元素个数
						Num_list.append(num)
						Name3_list.append(dam_num)
						Name3_list.append(station_num[index])
						Name3_list.append(device_num[index])
						Name3_list.append('3')
						Name3_list=','.join(Name3_list)#合并字符串	
						Name_list.append(Name3_list)
					#收敛
					if convergence[index] =="是":
						d4_list = []
						for d_his in Convergence_list_his:
							Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d4_list.append(d_his.d)
							Data_list.append(d_his.d)
						for d in Convergence_list:
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d4_list.append(d.d)
							Data_list.append(d.d)
						
						num = len(d4_list)
						Num_list.append(num)
						Name4_list.append(dam_num)	
						Name4_list.append(station_num[index])
						Name4_list.append(device_num[index])
						Name4_list.append('4')
						Name4_list=','.join(Name4_list)
						Name_list.append(Name4_list)				
					#平滑
					if smooth[index] =="是":
						d5_list = []
						for d_his in Smooth_list_his:
							Time_list.append(d_his.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d5_list.append(d_his.d)
							Data_list.append(d_his.d)
						for d in Smooth_list:
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
							d5_list.append(d.d)
							Data_list.append(d.d)
						
						num = len(d5_list)
						Num_list.append(num)
						Name5_list.append(dam_num)
						Name5_list.append(station_num[index])
						Name5_list.append(device_num[index])
						Name5_list.append('5')
						Name5_list=','.join(Name5_list)
						Name_list.append(Name5_list)
						


				#坐标
				if XYZ[index] == "是":				
					d6_list = []
					d7_list = []
					d8_list = []
					DPast_list = DPast.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
					for t in DPast_list:
						Data_list.append(t.x)
						d6_list.append(t.x)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					for t in DPast_list:
						Data_list.append(t.y)
						d7_list.append(t.y)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					for t in DPast_list:
						Data_list.append(t.z)
						d8_list.append(t.z)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					
					num = len(d6_list)
					Num_list.append(num)
					Name6_list.append(dam_num)
					Name6_list.append(station_num[index])
					Name6_list.append(device_num[index])
					Name6_list.append('6')
					Name6_list=','.join(Name6_list)
					Name_list.append(Name6_list)

					num = len(d7_list)
					Num_list.append(num)
					Name7_list.append(dam_num)
					Name7_list.append(station_num[index])
					Name7_list.append(device_num[index])
					Name7_list.append('7')
					Name7_list=','.join(Name7_list)
					Name_list.append(Name7_list)

					num = len(d8_list)
					Num_list.append(num)
					Name8_list.append(dam_num)
					Name8_list.append(station_num[index])
					Name8_list.append(device_num[index])
					Name8_list.append('8')
					Name8_list=','.join(Name8_list)
					Name_list.append(Name8_list)

				
			#print(Data_list)
			#print(Time_list)
			#print(Name_list)
			#print(Num_list)	

			return render(request, 'label_detail_history.html', {'Data_list': json.dumps(Data_list),'Time_list': json.dumps(Time_list),'Name_list': json.dumps(Name_list),'Num_list': json.dumps(Num_list)})
		else:
			return render(request, 'history_search.html')
	else:
		return render(request, 'login.html')

		

#实时数据查询120
def Raw_data_management(request):
	if request.session.get('userName'):
		if request.method == "POST":
			dam_num = request.POST.get('dam_num')
			device_num = request.POST.getlist('device_num[]')
			station_num = request.POST.getlist('station_num[]')
			
			temperature = request.POST.get('device_num_tem')

			average = request.POST.getlist('d1_num[]')
			convergence = request.POST.getlist('d2_num[]')
			smooth = request.POST.getlist('d3_num[]')
			XYZ = request.POST.getlist('coor_num[]')	
			raw = request.POST.getlist('raw_num[]')
			#由于只显示一个标签的温度对标签编号去重处理
			device_num_2 = list(set(device_num))

			print (temperature)
			print (device_num)
			print (device_num_2)

			num = len(station_num)
			Data_list = []
			Name_list = [] 
			Num_list = [] 
			Time_list = []
			

			for index in range(num):
			#判断锚点编号
				dam_list = Dam.objects.get(dam_num = dam_num)
				device_list = Device.objects.get(device_num = device_num[index],at_tip = 1,dam = dam_list)
				#通过最大的ID查询
				DPast_list = DPast.objects.filter(device = device_list).order_by('-id')[:4]
				Dping_list = Dping.objects.filter(device = device_list).order_by('-id')[:4]
				#收敛
				Convergence_list = Convergence_data.objects.filter(device = device_list,station_num = station_num[index]).order_by('-id')[:4]
				#平滑
				Smooth_list = Smooth_data.objects.filter(device = device_list,station_num = station_num[index]).order_by('-id')[:4]
				#平均
				Average_list = Average_data.objects.filter(device = device_list,station_num = station_num[index]).order_by('-id')[:4]
			
				#D_list = Raw_data.objects.filter(device = device_list).order_by('-id')[:120]
				D_list = Processing_data.objects.filter(device = device_list,station_num = station_num[index]).exclude(d = 0).order_by('-id')[:120]			

				Convergence_list = Convergence_list[::-1]
				Smooth_list = Smooth_list[::-1]
				Average_list = Average_list [::-1]
				D_list = D_list[::-1]

				#D_list = D_list.reverse()[:1]
				Name2_list = [] 
				Name3_list = []
				Name4_list = []
				Name5_list = []
				Name6_list = []
				Name7_list = []
				Name8_list = []

				#原始
				if raw[index] =="是":
					d2_list = []
					Time_list_2= []
					for d in D_list :
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S:%S"))
						Data_list.append(d.d)
						d2_list.append(d.d)

					'''if station_num[index]== "0":
						D_list_2 = Raw_data.objects.filter(device = device_list, d1 = 0).order_by('-id')[:120]
						for i in D_list_2:
							if i in D_list:
								D_list.remove(i)
						for d in D_list :
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S:%S"))
							Data_list.append(d.d1)
							d2_list.append(d.d1)
					elif station_num[index] == "1":
						D_list_2 = Raw_data.objects.filter(device = device_list, d2 = 0).order_by('-id')[:120]
						for i in D_list_2:
							if i in D_list:
								D_list.remove(i)
						for d in D_list :
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S:%S"))
							Data_list.append(d.d2)
							d2_list.append(d.d2)
					elif station_num[index] == "2":
						D_list_2 = Raw_data.objects.filter(device = device_list, d3 = 0).order_by('-id')[:120]
						for i in D_list_2:
							if i in D_list:
								D_list.remove(i)
						for d in D_list :
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S:%S"))
							Data_list.append(d.d3)
							d2_list.append(d.d3)
					elif station_num[index] == "3":
						D_list_2 = Raw_data.objects.filter(device = device_list, d4 = 0).order_by('-id')[:120]
						for i in D_list_2:
							if i in D_list:
								D_list.remove(i)
						for d in D_list :
							Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S:%S"))
							Data_list.append(d.d4)
							d2_list.append(d.d4)'''
					num = len(d2_list)
					Num_list.append(num)
					Name2_list.append(dam_num)
					Name2_list.append(station_num[index])
					Name2_list.append(device_num[index])
					Name2_list.append('2')
					Name2_list=','.join(Name2_list)
					Name_list.append(Name2_list)				
				#平均
				if average[index] =="是":
					d3_list = []
					for d in Average_list:
						d3_list.append(d.d)
						Data_list.append(d.d)
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					num = len(d3_list)#计算list元素个数
					Num_list.append(num)
					Name3_list.append(dam_num)
					Name3_list.append(station_num[index])
					Name3_list.append(device_num[index])
					Name3_list.append('3')
					Name3_list=','.join(Name3_list)#合并字符串	
					Name_list.append(Name3_list)
						

				#收敛
				if convergence[index] =="是":
					d4_list = []
					for d in Convergence_list:
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d4_list.append(d.d)
						Data_list.append(d.d)

						'''if station_num[index] == "0":
							d4_list.append(d.d1)
							Data_list.append(d.d1)
						elif station_num[index] == "1":
							d4_list.append(d.d2)
							Data_list.append(d.d2)
						elif station_num[index] == "2":
							d4_list.append(d.d3)
							Data_list.append(d.d3)
						elif station_num[index] == "3":
							d4_list.append(d.d4)
							Data_list.append(d.d4)'''
					num = len(d4_list)
					Num_list.append(num)
					Name4_list.append(dam_num)
					Name4_list.append(station_num[index])
					Name4_list.append(device_num[index])	
					Name4_list.append('4')
					Name4_list=','.join(Name4_list)
					Name_list.append(Name4_list)
						

				#平滑
				if smooth[index] =="是":
					d5_list = []
					for d in Smooth_list:
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						d5_list.append(d.d)
						Data_list.append(d.d)
					num = len(d5_list)
					Num_list.append(num)
					Name5_list.append(dam_num)
					Name5_list.append(station_num[index])
					Name5_list.append(device_num[index])
					Name5_list.append('5')
					Name5_list=','.join(Name5_list)
					Name_list.append(Name5_list)

				#坐标
				if XYZ[index] == "是":				
					d6_list = []
					d7_list = []
					d8_list = []
					DPast_list = DPast.objects.filter(device = device_list).order_by('-id')[:4]
					DPast_list = DPast_list[::-1]
					for t in DPast_list:
						Data_list.append(t.x)
						d6_list.append(t.x)
						if d6_list == [None]:
							Time_list.append (' ')
						else:
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					for t in DPast_list:
						Data_list.append(t.y)
						d7_list.append(t.y)
						if d7_list == [None]:
							Time_list.append (' ')
						else:
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					for t in DPast_list:
						Data_list.append(t.z)
						d8_list.append(t.z)
						if d8_list == [None]:
							Time_list.append (' ')
						else:
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					num = len(d6_list)
					Num_list.append(num)
					Name6_list.append(dam_num)
					Name6_list.append(station_num[index])
					Name6_list.append(device_num[index])
					Name6_list.append('6')
					Name6_list=','.join(Name6_list)
					Name_list.append(Name6_list)
					num = len(d7_list)
					Num_list.append(num)
					Name7_list.append(dam_num)
					Name7_list.append(station_num[index])
					Name7_list.append(device_num[index])
					Name7_list.append('7')
					Name7_list=','.join(Name7_list)
					Name_list.append(Name7_list)
					num = len(d8_list)
					Num_list.append(num)
					Name8_list.append(dam_num)
					Name8_list.append(station_num[index])
					Name8_list.append(device_num[index])
					Name8_list.append('8')
					Name8_list=','.join(Name8_list)
					Name_list.append(Name8_list)

			if temperature == "是":
				for i in device_num_2 :
					dam_list = Dam.objects.get(dam_num = dam_num)
					device_list = Device.objects.get(device_num = i,at_tip = 1,dam = dam_list)
					#D_list = Raw_data.objects.filter(device = device_list).order_by('-id')[:120]
					D_list = Processing_data.objects.filter(device = device_list,station_num = station_num[index]).order_by('-id')[:120]	
					D_list=D_list[::-1]
					Name1_list = [] 
					
					temperature_list = []
					for t in D_list:
						temperature_list.append(t.temperature)
						Data_list.append(t.temperature)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					#print(temperature_list)
					num = len(temperature_list)
					Num_list.append(num)
					Name1_list.append(dam_num)
					Name1_list.append(station_num[index])
					Name1_list.append(i)
					Name1_list.append('1')
					Name1_list=','.join(Name1_list)
					Name_list.append(Name1_list)
				
			print(Data_list)
			print(Time_list)
			print(Name_list)
			print(Num_list)		
			return  render(request, 'label_detail_realTime.html',{'Data_list': json.dumps(Data_list),'Num_list': json.dumps(Num_list),'Time_list': json.dumps(Time_list),'Name_list': json.dumps(Name_list)})
		else:
			return  render(request, 'realTime_search.html')
	else:
		return render(request, 'login.html')

#实时数据查询1		
def Raw_data_management_real(request):
	if request.session.get('userName'):
		if request.method == "POST":
			dam_num = request.POST.get('dam_num')
			dam_num = re.findall(r"\d+\.?\d*",dam_num)
			device_num = request.POST.get('device_num')
			device_num = re.findall(r"\d+\.?\d*",device_num)
			station_num = request.POST.get('station_num')
			station_num = re.findall(r"\d+\.?\d*",station_num)
			type_num_list = request.POST.get('type_num')
			type_num_list = re.findall(r"\d+\.?\d*",type_num_list)
			
			#print (device_num)
			#print (station_num)
			#print (type_num_list)
			device_num_2 = list(set(device_num))
			num = len(station_num)
			Data_list = []
			Name_list = [] 
			Num_list = [] 
			Time_list = []
			Num_list = [] 	
			for index in range(num):
			#判断锚点编号
				dam_list = Dam.objects.get(dam_num = dam_num[index])
				device_list = Device.objects.filter(device_num = device_num[index],at_tip = 1,dam = dam_list)
				#通过最大的ID查询
				DPast_list = DPast.objects.filter(device = device_list).order_by('-id')[:1]
				Dping_list = Dping.objects.filter(device = device_list).order_by('-id')[:1]
				#收敛
				Convergence_list = Convergence_data.objects.filter(device = device_list,station_num = station_num[index]).order_by('-id')[:1]
				#平滑
				Smooth_list = Smooth_data.objects.filter(device = device_list,station_num = station_num[index]).order_by('-id')[:1]
				#平均
				Average_list = Average_data.objects.filter(device = device_list,station_num = station_num[index]).order_by('-id')[:1]
				#原始
				#D_list = Raw_data.objects.filter(device = device_list).order_by('-id')[:1]
				D_list = Processing_data.objects.filter(device = device_list,station_num = station_num[index]).order_by('-id')[:1]			



				

				#原始
				if type_num_list[index] == '2':
					d2_list = []
					for d in D_list :
						Data_list.append(d.d)
						d2_list.append(d.d)
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S:%S"))
						'''if station_num[index] == "0":
							Data_list.append(d.d1)
							d2_list.append(d.d1)
						elif station_num[index] == "1":
							Data_list.append(d.d2)
							d2_list.append(d.d2)
						elif station_num[index] == "2":
							Data_list.append(d.d3)
							d2_list.append(d.d3)
						elif station_num[index] == "3":
							Data_list.append(d.d4)	
							d2_list.append(d.d4)'''
					num = len(d2_list)
					Num_list.append(num)
				#平均
				if type_num_list[index] == '3':
					d3_list = []
					for d in Average_list:
						d3_list.append(d.d)
						Data_list.append(d.d)
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					num = len(d3_list)
					Num_list.append(num)
				#收敛
				if type_num_list[index] =='4':
					d4_list = []
					for d in Convergence_list:
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						Data_list.append(d.d)
						d4_list.append(d.d)
					num = len(d4_list)
					Num_list.append(num)
					'''if station_num[index] == "0":
						Data_list.append(d.d1)
					elif station_num[index] == "1":
						Data_list.append(d.d2)
					elif station_num[index] == "2":
						Data_list.append(d.d3)
					elif station_num[index] == "3":
						Data_list.append(d.d4)'''
				#平滑
				if type_num_list[index] == '5':
					d5_list = []
					for d in Smooth_list:
						d5_list.append(d.d)
						Data_list.append(d.d)
						Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
						'''if station_num[index] == "0":
							Data_list.append(d.d1)
						elif station_num[index] == "1":
							Data_list.append(d.d2)
						elif station_num[index] == "2":
							Data_list.append(d.d3)
						elif station_num[index] == "3":
							Data_list.append(d.d4)'''
					num = len(d5_list)
					Num_list.append(num)
				#坐标
				if type_num_list[index] == '6':	
					x_list = []	
					y_list = []	
					z_list = []		
					DPast_list = DPast.objects.filter(device = device_list).order_by('-id')[:1]		
					for t in DPast_list:
						Data_list.append(t.x)
						x_list.append(t.x)
						if x_list == [None]:
							Time_list.append (' ')
						else:
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					for t in DPast_list:
						Data_list.append(t.y)
						y_list.append(t.y)
						if y_list == [None]:
							Time_list.append (' ')
						else:
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					for t in DPast_list:
						Data_list.append(t.z)
						z_list.append(t.z)
						if z_list == [None]:
							Time_list.append (' ')
						else:
							Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))	
				#温度
				if type_num_list[index] == '1':
					temperature_list=[]
					for t in D_list:
						temperature_list.append(t.temperature)
						Data_list.append(t.temperature)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					num = len(temperature_list)
					Num_list.append(num)

			#print(Data_list)
			#print(Time_list)
			#print(Num_list)
			#print(x_list)
			'''判断锚点编号
				device_list = Device.objects.filter(device_num = device_num_list[index],at_tip = 1 )
				#通过最大的ID查询
				D_list = Raw_data.objects.filter(device = device_list).order_by('-id')[:1]
				d = D_list[0]
				#for d in D_list :'''
			return HttpResponse(json.dumps({'Data_list':Data_list,'Time_list':Time_list,'Num_list':Num_list}))
		else:
			return  render(request, 'realTime_search.html')
	else:
		return render(request, 'login.html')

def label_detail_realtime(request):
	if request.session.get('userName'):
		return render(request,'label_detail_realtime.html') 
	else:
		return render(request, 'login.html')

def Label_history_select(request,aid,bid,cid):
	if request.session.get('userName'):
		dam_list =[]
		station_list =[]
		device_list =[]

		dam_list.append(aid)
		station_list.append(bid)
		device_list.append(cid)
		print (dam_list)

		return render(request,'label_history_select.html',{'dam_list':json.dumps(dam_list),'station_list':json.dumps(station_list),'device_list':json.dumps(device_list)})

	else:
		return render(request, 'login.html')
	
def history_search(request):
	if request.session.get('userName'):
		dam_list = Dam.objects.all()
		dam_num_list=[]
		for d in dam_list:
			dam_num_list.append(d.dam_num)	
		print (dam_num_list)
		device_list_123 = Device.objects.filter(at_tip =  1,dam_id = 1)
		device_list_456 = Device.objects.filter(at_tip =  1,dam_id = 2)
		device_num_list =[]
		device_num_list_1 = []
		device_num_list_2 = []
		device_num_total_list = []
		for d in device_list_123:
			device_num_list_1.append(d.device_num)
			device_num_list.append(d.device_num)
		device_num_total_list.append(len(device_num_list_1))
		for d in device_list_456:
			device_num_list_2.append(d.device_num)
			device_num_list.append(d.device_num)
		device_num_total_list.append(len(device_num_list_2))
		#print (device_num_list)
		station_list_123 = Device.objects.filter(at_tip =  0,dam_id = 1)
		station_list_456 = Device.objects.filter(at_tip =  0,dam_id = 2)
		station_num_list= []
		station_num_list_1 = []
		station_num_list_2 = []
		station_num_total_list = []
		for d in station_list_123:
			station_num_list_1.append(d.device_num)
			station_num_list.append(d.device_num)
		station_num_total_list.append(len(station_num_list_1))
		for d in station_list_456:
			station_num_list_2.append(d.device_num)
			station_num_list.append(d.device_num)
		station_num_total_list.append(len(station_num_list_2))
		print(device_num_total_list)
		print(station_num_total_list)
		#print (station_num_list)
		#station_num_list = station_num_list.distinct()
		return render(request,'history_search.html',{'device_num_total_list':json.dumps(device_num_total_list),'station_num_total_list':json.dumps(station_num_total_list),'dam_num_list':json.dumps(dam_num_list),'device_num_list':json.dumps(device_num_list),'station_num_list':json.dumps(station_num_list)})
	else:
		return render(request, 'login.html')

def realTime_search(request):
	if request.session.get('userName'):
		dam_list = Dam.objects.all()
		dam_num_list =[]
		for d in dam_list:
			dam_num_list.append(d.dam_num)	
		#print (dam_num_list)
		device_list_123 = Device.objects.filter(at_tip =  1,dam_id = 1)
		device_list_456 = Device.objects.filter(at_tip =  1,dam_id = 2)
		device_num_list =[]
		device_num_list_1 = []
		device_num_list_2 = []
		device_num_total_list = []
		for d in device_list_123:
			device_num_list_1.append(d.device_num)
			device_num_list.append(d.device_num)
		device_num_total_list.append(len(device_num_list_1))
		for d in device_list_456:
			device_num_list_2.append(d.device_num)
			device_num_list.append(d.device_num)
		device_num_total_list.append(len(device_num_list_2))
		#print (device_num_list)
		station_list_123 = Device.objects.filter(at_tip =  0,dam_id = 1)
		station_list_456 = Device.objects.filter(at_tip =  0,dam_id = 2)
		station_num_list= []
		station_num_list_1 = []
		station_num_list_2 = []
		station_num_total_list = []
		for d in station_list_123:
			station_num_list_1.append(d.device_num)
			station_num_list.append(d.device_num)
		station_num_total_list.append(len(station_num_list_1))
		for d in station_list_456:
			station_num_list_2.append(d.device_num)
			station_num_list.append(d.device_num)
		station_num_total_list.append(len(station_num_list_2))
		print(device_num_total_list)
		print(station_num_total_list)
		return render(request,'realTime_search.html',{'device_num_total_list':json.dumps(device_num_total_list),'station_num_total_list':json.dumps(station_num_total_list),'dam_num_list':json.dumps(dam_num_list),'device_num_list':json.dumps(device_num_list),'station_num_list':json.dumps(station_num_list)})
	else:
		return render(request, 'login.html')