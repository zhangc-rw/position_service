from django.shortcuts import render
# Create your views here.
from Displacement_management.models import DReal
from Displacement_management.models import DPast
from Displacement_management.models import Dping
from Displacement_management.models import Average_data
from Displacement_management.models import Raw_data
from Dam_Device_management.models import Device
from Dam_Device_management.models import Dam


import datetime
import json
import re
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse
#实时位移查看
def DReal_management(request,aid,bid):
	dam_list = Dam.objects.get(dam_num = aid)
	device_list = Device.objects.filter(device_num = bid,dam = dam_list)
	D_list = DReal.objects.filter(device = device_list)
	DReal_list = []
	for i in D_list:
		DReal_list.append(i.device)
		DReal_list.append(i.stationID)
		DReal_list.append(i.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
		DReal_list.append(i.temperature)
		DReal_list.append(i.voltage)
		DReal_list.append(i.d1)
		DReal_list.append(i.d2)
		DReal_list.append(i.d3)
		DReal_list.append(i.d4)
		DReal_list.append(i.d5)
		DReal_list.append(i.d6)
		DReal_list.append(i.d7)
		DReal_list.append(i.d8)
		DReal_list.append(i.x)
		DReal_list.append(i.y)
		DReal_list.append(i.z)
		DReal_list.append(i.d)
		DReal_list.append(i.dx)
		DReal_list.append(i.dy)
		DReal_list.append(i.dz)
	print(DReal_list)
	return render(request,'label_detail_realtime.html',{'DReal_list':DReal_list})


#历史位移查看
def DPast_management_sametime(request):
	if request.method == "POST":
		time_ymd = request.POST.getlist('reservationtime[]')
		time_hms_start = request.POST.get('start_time')
		time_hms_end = request.POST.get('end_time')
		
		dam_num = request.POST.get('dam_num')
		device_num = request.POST.getlist('device_num[]')
		station_num = request.POST.getlist('station_num[]')
		average = request.POST.getlist('d1_num[]')
		convergence = request.POST.getlist('d2_num[]')
		smooth = request.POST.getlist('d3_num[]')
		XYZ = request.POST.getlist('coor_num[]')
		temperature = request.POST.getlist('temperature_num[]')
		#print(dam_num)
		print(time_hms_start)
		print(time_hms_end)
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

				dam_list = Dam.objects.get(dam_num = dam_num)
				device_list = Device.objects.filter(device_num = device_num[index],at_tip =  1,dam = dam_list)
				DPast_list = DPast.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list)
				Dping_list = Dping.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list)
				Average_list = Average_data.objects.filter(dreal_update_time__range=(start_1, end_1)).filter(device = device_list,station_num = station_num[index])
				
				Name1_list = [] 
				Name3_list = []
				Name4_list = []
				Name5_list = []
				Name6_list = []
				Name7_list = []
				Name8_list = []

				if temperature[index] == "是":
					temperature_list = []
					for t in DPast_list:
						temperature_list.append(t.temperature)
						Data_list.append(t.temperature)
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					print(temperature_list)
					num = len(temperature_list)
					Num_list.append(num)
					Name1_list.append(dam_num)
					Name1_list.append(device_num[index])
					Name1_list.append(station_num[index])
					Name1_list.append('1')
					Name1_list=','.join(Name1_list)
					Name_list.append(Name1_list)
					time1_list = []
						

				#平均
				if average[index] =="是":
					d3_list = []
					for d in Average_list:
						d3_list.append(d.d)
						Data_list.append(d.d)
					num = len(d3_list)#计算list元素个数
					Num_list.append(num)
					Name3_list.append(dam_num)
					Name3_list.append(device_num[index])
					Name3_list.append(station_num[index])
					Name3_list.append('3')
					Name3_list=','.join(Name3_list)#合并字符串	
					Name_list.append(Name3_list)
					time1_list = []
					for t in DPast_list:
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
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
					Name4_list.append(device_num[index])
					Name4_list.append(station_num[index])
					Name4_list.append('4')
					Name4_list=','.join(Name4_list)
					Name_list.append(Name4_list)

						
				#平滑
				if smooth[index] =="是":
					d5_list = []
					for d in Dping_list:
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
					Name5_list.append(device_num[index])
					Name5_list.append(station_num[index])
					Name5_list.append('5')
					Name5_list=','.join(Name5_list)
					Name_list.append(Name5_list)
					for t in DPast_list:
						Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))

				#坐标
				if XYZ[index] == "是":				
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
						'''for i in range(len(XYZ_list)):
							XYZ_list[i] = str(XYZ_list[i])
						XYZ_list=','.join(XYZ_list)
						d6_list.append(XYZ_list)	
					Data_list = Data_list + d6_list'''
					num = len(d6_list)
					Num_list.append(num)
					Name6_list.append(dam_num)
					Name6_list.append(device_num[index])
					Name6_list.append(station_num[index])
					Name6_list.append('6')
					Name6_list=','.join(Name6_list)
					Name_list.append(Name6_list)
					num = len(d7_list)
					Num_list.append(num)
					Name7_list.append(dam_num)
					Name7_list.append(device_num[index])
					Name7_list.append(station_num[index])
					Name7_list.append('7')
					Name7_list=','.join(Name7_list)
					Name_list.append(Name7_list)
					num = len(d8_list)
					Num_list.append(num)
					Name8_list.append(dam_num)
					Name8_list.append(device_num[index])
					Name8_list.append(station_num[index])
					Name8_list.append('8')
					Name8_list=','.join(Name8_list)
					Name_list.append(Name8_list)
						
			print(Data_list)
			print(Time_list)
			print(Name_list)
			print(Num_list)

			

	return render(request, 'label_detail_history_sametime.html', {'Data_list': json.dumps(Data_list),'Time_list': json.dumps(Time_list),'Name_list': json.dumps(Name_list),'Num_list': json.dumps(Num_list)})

#历史位移查看
def DPast_management(request):
	if request.method == "POST":
		time = request.POST.getlist('reservationtime[]')
		dam_num = request.POST.get('dam_num')
		device_num = request.POST.getlist('device_num[]')
		station_num = request.POST.getlist('station_num[]')
		average = request.POST.getlist('d1_num[]')
		convergence = request.POST.getlist('d2_num[]')
		smooth = request.POST.getlist('d3_num[]')
		XYZ = request.POST.getlist('coor_num[]')
		temperature = request.POST.getlist('temperature_num[]')
		print(dam_num)
		num = len(station_num)
		Data_list = []
		Name_list = [] 
		Num_list = [] 
		Time_list = []
		for index in range(num):
			start =time[index][0:16]
			end = time[index][-16:]
			#判断锚点编号
			dam_list = Dam.objects.get(dam_num = dam_num)
			device_list = Device.objects.filter(device_num = device_num[index],at_tip =  1,dam = dam_list )
			DPast_list = DPast.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
			Dping_list = Dping.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
			Average_list = Average_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,station_num = station_num[index])
			Name1_list = [] 
			Name2_list = [] 
			Name3_list = []
			Name4_list = []
			Name5_list = []
			Name6_list = []
			Name7_list = []
			Name8_list = []

			if temperature[index] == "是":
				temperature_list = []
				for t in DPast_list:
					temperature_list.append(t.temperature)
					Data_list.append(t.temperature)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
				#print(temperature_list)
				num = len(temperature_list)
				Num_list.append(num)
				Name1_list.append(dam_num)
				Name1_list.append(device_num[index])
				Name1_list.append(station_num[index])
				Name1_list.append('1')
				Name1_list=','.join(Name1_list)
				Name_list.append(Name1_list)

			#平均
			if average[index] =="是":
				d3_list = []
				for d in Average_list:
					d3_list.append(d.d)
					Data_list.append(d.d)
				num = len(d3_list)#计算list元素个数
				Num_list.append(num)
				Name3_list.append(dam_num)
				Name3_list.append(device_num[index])
				Name3_list.append(station_num[index])
				Name3_list.append('3')
				Name3_list=','.join(Name3_list)#合并字符串	
				Name_list.append(Name3_list)
				for t in DPast_list:
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))

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
				Name4_list.append(device_num[index])
				Name4_list.append(station_num[index])
				Name4_list.append('4')
				Name4_list=','.join(Name4_list)
				Name_list.append(Name4_list)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))

			#平滑
			if smooth[index] =="是":
				d5_list = []
				for d in Dping_list:
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
				Name5_list.append(device_num[index])
				Name5_list.append(station_num[index])
				Name5_list.append('5')
				Name5_list=','.join(Name5_list)
				Name_list.append(Name5_list)
				time1_list = []
				for t in DPast_list:
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))

			#坐标
			if XYZ[index] == "是":				
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
				Name6_list.append(dam_num)
				Name6_list.append(device_num[index])
				Name6_list.append(station_num[index])
				Name6_list.append('6')
				Name6_list=','.join(Name6_list)
				Name_list.append(Name6_list)
				num = len(d7_list)
				Num_list.append(num)
				Name7_list.append(dam_num)
				Name7_list.append(device_num[index])
				Name7_list.append(station_num[index])
				Name7_list.append('7')
				Name7_list=','.join(Name7_list)
				Name_list.append(Name7_list)
				num = len(d8_list)
				Num_list.append(num)
				Name8_list.append(dam_num)
				Name8_list.append(device_num[index])
				Name8_list.append(station_num[index])
				Name8_list.append('8')
				Name8_list=','.join(Name8_list)
				Name_list.append(Name8_list)

			
		print(Data_list)
		print(Time_list)
		print(Name_list)
		print(Num_list)	

	return render(request, 'label_detail_history.html', {'Data_list': json.dumps(Data_list),'Time_list': json.dumps(Time_list),'Name_list': json.dumps(Name_list),'Num_list': json.dumps(Num_list)})
			
		
	#return HttpResponseRedirect('/Dam_Device_management/DandL_management')
	#return HttpResponse(json.dumps({'d_list':d_list,'time_list':time_list}))
	#return render(request,'label_detail_history.html')'''


def Raw_data_management(request):
	if request.method == "POST":
		dam_num = request.POST.get('dam_num')
		device_num = request.POST.getlist('device_num[]')
		station_num = request.POST.getlist('station_num[]')
		temperature = request.POST.getlist('temperature_num[]')
		average = request.POST.getlist('d1_num[]')
		convergence = request.POST.getlist('d2_num[]')
		smooth = request.POST.getlist('d3_num[]')
		XYZ = request.POST.getlist('coor_num[]')	
		raw = request.POST.getlist('raw_num[]')
		print (raw)
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
			DPast_list = DPast.objects.filter(device = device_list).order_by('-id')[:1]
			Dping_list = Dping.objects.filter(device = device_list).order_by('-id')[:1]
			Average_list = Average_data.objects.filter(device = device_list,station_num = station_num[index]).order_by('-id')[:1]
			D_list = Raw_data.objects.filter(device = device_list).order_by('-id')[:1]
			#D_list = D_list.reverse()[:1]
			Name1_list = [] 
			Name2_list = [] 
			Name3_list = []
			Name4_list = []
			Name5_list = []
			Name6_list = []
			Name7_list = []
			Name8_list = []

			#温度
			if temperature[index] == "是":
				temperature_list = []
				for t in DPast_list:
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
					
			#原始
			if raw[index] =="是":
				d2_list = []
				for d in D_list :
					Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S:%S"))
					if station_num[index] == "0":
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
						d2_list.append(d.d4)
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

			#坐标
			if XYZ[index] == "是":				
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

			
		print(Data_list)
		print(Time_list)
		print(Name_list)
		print(Num_list)		
	return  render(request, 'label_detail_realTime_Raw.html',{'Data_list': json.dumps(Data_list),'Time_list': json.dumps(Time_list),'Name_list': json.dumps(Name_list)})
		
def Raw_data_management_real(request):
	if request.method == "POST":
		dam_num = request.POST.get('dam_num')
		dam_num = re.findall(r"\d+\.?\d*",dam_num)
		device_num = request.POST.get('device_num')
		device_num = re.findall(r"\d+\.?\d*",device_num)
		station_num = request.POST.get('station_num')
		station_num = re.findall(r"\d+\.?\d*",station_num)
		type_num_list = request.POST.get('type_num')
		type_num_list = re.findall(r"\d+\.?\d*",type_num_list)
		print (type_num_list)
		#print (dam_num)
		#print (device_num)
		num = len(station_num)
		Data_list = []
		Name_list = [] 
		Num_list = [] 
		Time_list = []
		for index in range(num):
		#判断锚点编号
			dam_list = Dam.objects.get(dam_num = dam_num[index])
			device_list = Device.objects.filter(device_num = device_num[index],at_tip = 1,dam = dam_list)
			#通过最大的ID查询
			DPast_list = DPast.objects.filter(device = device_list).order_by('-id')[:1]
			Dping_list = Dping.objects.filter(device = device_list).order_by('-id')[:1]
			Average_list = Average_data.objects.filter(device = device_list,station_num = station_num[index]).order_by('-id')[:1]
			D_list = Raw_data.objects.filter(device = device_list).order_by('-id')[:1]

			Name1_list = [] 
			Name2_list = [] 
			Name3_list = []
			Name4_list = []
			Name5_list = []
			Name6_list = []
			#温度
			if type_num_list[index] == '1':
				for t in DPast_list:
					Data_list.append(t.temperature)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
			#原始
			if type_num_list[index] == '2':
				d2_list = []
				for d in D_list :
					Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S:%S"))
					if station_num[index] == "0":
						Data_list.append(d.d1)
					elif station_num[index] == "1":
						Data_list.append(d.d2)
					elif station_num[index] == "2":
						Data_list.append(d.d3)
					elif station_num[index] == "3":
						Data_list.append(d.d4)	
			#平均
			if type_num_list[index] == '3':
				for d in Average_list:
					Data_list.append(d.d)
					Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
			#收敛
			if type_num_list[index] =='4':
				for d in DPast_list:
					Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					if station_num[index] == "0":
						Data_list.append(d.d1)
					elif station_num[index] == "1":
						Data_list.append(d.d2)
					elif station_num[index] == "2":
						Data_list.append(d.d3)
					elif station_num[index] == "3":
						Data_list.append(d.d4)
			#平滑
			if type_num_list[index] == '5':
				for d in Dping_list:
					Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
					if station_num[index] == "0":
						Data_list.append(d.d1)
					elif station_num[index] == "1":
						Data_list.append(d.d2)
					elif station_num[index] == "2":
						Data_list.append(d.d3)
					elif station_num[index] == "3":
						Data_list.append(d.d4)
			#坐标
			if type_num_list[index] == '6':						
				for t in DPast_list:
					Data_list.append(t.x)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
				for t in DPast_list:
					Data_list.append(t.y)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
				for t in DPast_list:
					Data_list.append(t.z)
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))		
		print(Data_list)
		print(Time_list)
		'''判断锚点编号
			device_list = Device.objects.filter(device_num = device_num_list[index],at_tip = 1 )
			#通过最大的ID查询
			D_list = Raw_data.objects.filter(device = device_list).order_by('-id')[:1]
			d = D_list[0]
			#for d in D_list :'''
	return HttpResponse(json.dumps({'Data_list':Data_list,'Time_list':Time_list}))


def label_detail_realtime(request):
	return render(request,'label_detail_realtime.html') 
def label_history_select(request,aid,bid):
	dam_list = Dam.objects.get(dam_num = aid)
	device_list = Device.objects.filter(device_num = bid,dam = dam_list)
	return render(request,'label_history_select.html',{'device_list':device_list})
def history_search(request):
	device_list = Device.objects.filter(at_tip =  1)
	device_num_list= []
	for d in device_list:
		device_num_list.append(d.device_num)
	print (device_num_list)	
	station_list = Device.objects.filter(at_tip =  0)
	station_num_list = []
	for s in station_list:
		station_num_list.append(s.device_num)
	#station_num_list = station_num_list.distinct()
	print (station_num_list)
	return render(request,'history_search.html',{'device_num_list':device_num_list,'station_num_list':station_num_list})
def realTime_search(request):
	device_list = Device.objects.filter(at_tip =  1)
	device_num_list= []
	for d in device_list:
		device_num_list.append(d.device_num)
	print (device_num_list)	
	station_list = Device.objects.filter(at_tip =  0)
	station_num_list = []
	for s in station_list:
		station_num_list.append(s.device_num)
	#station_num_list = station_num_list.distinct()
	print (station_num_list)
	return render(request,'realTime_search.html',{'device_num_list':device_num_list,'station_num_list':station_num_list})