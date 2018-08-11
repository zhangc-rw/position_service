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
		time = request.POST.getlist('reservationtime[]')
		dam_num = request.POST.getlist('dam_num[]')
		device_num = request.POST.getlist('device_num[]')
		qian = request.POST.getlist('d1_num[]')
		hou = request.POST.getlist('d2_num[]')
		ping = request.POST.getlist('d3_num[]')
		temperature = request.POST.getlist('temperature_num[]')
		num = len(dam_num)
		Data_list = []
		Name_list = [] 
		Num_list = [] 
		Time_list = []
		#遍历基站列表取出时间段个数
		for index in range(num):
			start =time[index][0:16]
			#start1=time[index][11:16]
			end = time[index][-16:]
			print(time[index])
			print(start)
			#print(start1)
			#start = start+' '+start1
			#print(start)
			#判断锚点编号
			device_list = Device.objects.filter(device_num = device_num[index],at_tip =  1)
			D_list = DPast.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
			DP_list = Dping.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
			Data3_list = Average_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,station_num = dam_num[index])
			
			Name1_list = [] 
			Name2_list = [] 
			Name3_list = [] 
			Name4_list = [] 
			if temperature[index] == "是":
				temperature_list = []
				for t in D_list:
					temperature_list.append(t.temperature)
					Data_list.append(t.temperature)
				#print(Data_list)
				num = len(temperature_list)
				Num_list.append(num)
				Name3_list.append(device_num[index])
				Name3_list.append(dam_num[index])
				Name3_list.append('1')
				Name3_list=','.join(Name3_list)
				Name_list.append(Name3_list)
				time1_list = []
				for t in D_list:
					time1_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
				#num3 = len(time1_list)
				#Num_list.append(num)			
			if qian[index] =="是":
				d_list = []
				for d in Data3_list:
					d_list.append(d.d)
					Data_list.append(d.d)
				num = len(d_list)#计算list元素个数
				Num_list.append(num)
				Name1_list.append(device_num[index])
				Name1_list.append(dam_num[index])
				Name1_list.append('2')
				Name1_list=','.join(Name1_list)#合并字符串	
				Name_list.append(Name1_list)
				time1_list = []
				for t in D_list:
					time1_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
				#num1 = len(time1_list)
				#Num_list.append(num)
			if hou[index] =="是":
				d2_list = []
				for d in D_list:
					if dam_num[index] == "0":
						d2_list.append(d.d1)
						Data_list.append(d.d1)
					elif dam_num[index] == "1":
						d2_list.append(d.d2)
						Data_list.append(d.d2)
					elif dam_num[index] == "2":
						d2_list.append(d.d3)
						Data_list.append(d.d3)
					elif dam_num[index] == "3":
						d2_list.append(d.d4)
						Data_list.append(d.d4)
				num = len(d2_list)
				Num_list.append(num)
				Name2_list.append(device_num[index])
				Name2_list.append(dam_num[index])
				Name2_list.append('3')
				Name2_list=','.join(Name2_list)
				Name_list.append(Name2_list)
				time1_list = []
				for t in D_list:
					time1_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
				#num2 = len(time1_list)
				#Num_list.append(num)
			if ping[index] =="是":
				d4_list = []
				for d in DP_list:
					if dam_num[index] == "0":
						d4_list.append(d.d1)
						Data_list.append(d.d1)
					elif dam_num[index] == "1":
						d4_list.append(d.d2)
						Data_list.append(d.d2)
					elif dam_num[index] == "2":
						d4_list.append(d.d3)
						Data_list.append(d.d3)
					elif dam_num[index] == "3":
						d4_list.append(d.d4)
						Data_list.append(d.d4)
				num = len(d4_list)
				Num_list.append(num)
				Name4_list.append(device_num[index])
				Name4_list.append(dam_num[index])
				Name4_list.append('4')
				Name4_list=','.join(Name4_list)
				Name_list.append(Name4_list)
				time1_list = []
				for t in D_list:
					time1_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
				#num2 = len(time1_list)
				#Num_list.append(num)
		print(Data_list)
		print(Time_list)
		print(Name_list)
		print(Num_list)

	return render(request, 'label_detail_history_sametime.html', {'Data_list': json.dumps(Data_list),'Time_list': json.dumps(Time_list),'Name_list': json.dumps(Name_list),'Num_list': json.dumps(Num_list)})

#历史位移查看
def DPast_management(request):
	if request.method == "POST":
		time = request.POST.getlist('reservationtime[]')
		dam_num = request.POST.getlist('dam_num[]')
		device_num = request.POST.getlist('device_num[]')
		qian = request.POST.getlist('d1_num[]')
		hou = request.POST.getlist('d2_num[]')
		ping = request.POST.getlist('d3_num[]')
		temperature = request.POST.getlist('temperature_num[]')
		num = len(dam_num)
		Data_list = []
		Name_list = [] 
		Num_list = [] 
		Time_list = []
		for index in range(num):
			start =time[index][0:16]
			end = time[index][-16:]
			#判断锚点编号
			device_list = Device.objects.filter(device_num = device_num[index],at_tip =  1)
			D_list = DPast.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
			DP_list = Dping.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
			Data3_list = Average_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,station_num = dam_num[index])
			Name1_list = [] 
			Name2_list = [] 
			Name3_list = []
			Name4_list = []
			if temperature[index] == "是":
				temperature_list = []
				for t in D_list:
					temperature_list.append(t.temperature)
					Data_list.append(t.temperature)
				#print(Data_list)
				num = len(temperature_list)
				Num_list.append(num)
				Name3_list.append(device_num[index])
				Name3_list.append(dam_num[index])
				Name3_list.append('1')
				Name3_list=','.join(Name3_list)
				Name_list.append(Name3_list)
				time1_list = []
				for t in D_list:
					time1_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
				#num3 = len(time1_list)
				#Num_list.append(num)

			if qian[index] =="是":
				d_list = []
				for d in Data3_list:
					d_list.append(d.d)
					Data_list.append(d.d)
				num = len(d_list)#计算list元素个数
				Num_list.append(num)
				Name1_list.append(device_num[index])
				Name1_list.append(dam_num[index])
				Name1_list.append('2')
				Name1_list=','.join(Name1_list)#合并字符串	
				Name_list.append(Name1_list)
				time1_list = []
				for t in D_list:
					time1_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
				#num1 = len(time1_list)
				#Num_list.append(num)

			if hou[index] =="是":
				d2_list = []
				for d in D_list:
					if dam_num[index] == "0":
						d2_list.append(d.d1)
						Data_list.append(d.d1)
					elif dam_num[index] == "1":
						d2_list.append(d.d2)
						Data_list.append(d.d2)
					elif dam_num[index] == "2":
						d2_list.append(d.d3)
						Data_list.append(d.d3)
					elif dam_num[index] == "3":
						d2_list.append(d.d4)
						Data_list.append(d.d4)
				num = len(d2_list)
				Num_list.append(num)
				Name2_list.append(device_num[index])
				Name2_list.append(dam_num[index])
				Name2_list.append('3')
				Name2_list=','.join(Name2_list)
				Name_list.append(Name2_list)
				time1_list = []
				for t in D_list:
					time1_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
				#num2 = len(time1_list)
				#Num_list.append(num)
			if ping[index] =="是":
				d4_list = []
				for d in DP_list:
					if dam_num[index] == "0":
						d4_list.append(d.d1)
						Data_list.append(d.d1)
					elif dam_num[index] == "1":
						d4_list.append(d.d2)
						Data_list.append(d.d2)
					elif dam_num[index] == "2":
						d4_list.append(d.d3)
						Data_list.append(d.d3)
					elif dam_num[index] == "3":
						d4_list.append(d.d4)
						Data_list.append(d.d4)
				num = len(d4_list)
				Num_list.append(num)
				Name4_list.append(device_num[index])
				Name4_list.append(dam_num[index])
				Name4_list.append('4')
				Name4_list=','.join(Name4_list)
				Name_list.append(Name4_list)
				time1_list = []
				for t in D_list:
					time1_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
				#num2 = len(time1_list)
				#Num_list.append(num)
			
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
		station_num_list = request.POST.getlist('station_num[]')
		#station_num_list = re.findall(r"\d+\.?\d*",station_num_list)#从字符串中取出数字
		print (station_num_list)
		device_num_list = request.POST.getlist('device_num[]')
		#device_num_list = re.findall(r"\d+\.?\d*",device_num_list)#从字符串中取出数字
		print (device_num_list)
		raw = request.POST.getlist('d3_num[]')
		print (raw)
		num = len(station_num_list)
		Data_list = []
		Time_list = []
		
		Name_list = []
		for index in range(num):
			Num_list = []
			
			Num_list.append(station_num_list[index])
			Num_list.append(device_num_list[index])
			Num_list=','.join(Num_list)
			Name_list.append(Num_list)

		#判断锚点编号
			device_list = Device.objects.filter(device_num = device_num_list[index],at_tip = 1)
			#通过最大的ID查询
			D_list = Raw_data.objects.filter(device = device_list).order_by('-id')[:1]
			#D_list = D_list.reverse()[:1]
			if raw[index] =="是":
				for d in D_list :
					if station_num_list[index] == "0":
						Data_list.append(d.d1)
					elif station_num_list[index] == "1":
						Data_list.append(d.d2)
					elif station_num_list[index] == "2":
						Data_list.append(d.d3)
					elif station_num_list[index] == "3":
						Data_list.append(d.d4)
					Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
				
		print(Data_list)
		print(Time_list)
		print(Name_list)
	return  render(request, 'label_detail_realTime_Raw.html',{'Data_list': json.dumps(Data_list),'Time_list': json.dumps(Time_list),'Name_list': json.dumps(Name_list)})
		
def Raw_data_management_real(request):
	if request.method == "POST":
		station_num_list = request.POST.get('station_num')
		station_num_list = re.findall(r"\d+\.?\d*",station_num_list)#从字符串中取出数字
		print (station_num_list)
		device_num_list = request.POST.get('device_num')
		device_num_list = re.findall(r"\d+\.?\d*",device_num_list)#从字符串中取出数字
		print (device_num_list)

		num = len(station_num_list)
		Data_list = []
		Time_list = []
		for index in range(num):
			#判断锚点编号
			device_list = Device.objects.filter(device_num = device_num_list[index],at_tip = 1 )
			#通过最大的ID查询
			D_list = Raw_data.objects.filter(device = device_list).order_by('-id')[:1]


			for d in D_list :
				if station_num_list[index] == "0":
					Data_list.append(d.d1)
				elif station_num_list[index] == "1":
					Data_list.append(d.d2)
				elif station_num_list[index] == "2":
					Data_list.append(d.d3)
				elif station_num_list[index] == "3":
					Data_list.append(d.d4)
				Time_list.append(d.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
				
		print(Data_list)
		print(Time_list)
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