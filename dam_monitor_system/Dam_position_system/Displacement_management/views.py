from django.shortcuts import render
# Create your views here.
from Displacement_management.models import DReal
from Displacement_management.models import DPast
from Displacement_management.models import Average_data
from Dam_Device_management.models import Device
from Dam_Device_management.models import Dam
import datetime
import json
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
		temperature = request.POST.getlist('temperature_num[]')
		num = len(dam_num)
		Data_list = []
		Name_list = [] 
		Num_list = [] 
		Time_list = []
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
			if dam_num[index] == "0":
				device_list = Device.objects.filter(device_num = device_num[index])
				D_list = DPast.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
				Data3_list = Average_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,station_num = dam_num[index])	
			elif dam_num[index] == "1":
				device_list = Device.objects.filter(device_num = device_num[index])
				D_list = DPast.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
				Data3_list = Average_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,station_num = dam_num[index])
			elif dam_num[index] == "2":
				device_list = Device.objects.filter(device_num = device_num[index])
				D_list = DPast.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
				Data3_list = Average_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,station_num = dam_num[index])
			elif dam_num[index] == "3":
				device_list = Device.objects.filter(device_num = device_num[index])
				D_list = DPast.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
				Data3_list = Average_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,station_num = dam_num[index])
			Name1_list = [] 
			Name2_list = [] 
			Name3_list = [] 			
			if qian[index] =="是":
				d_list = []
				for d in Data3_list:
					d_list.append(d.d)
					Data_list.append(d.d)
				num = len(d_list)#计算list元素个数
				Num_list.append(num)
				Name1_list.append(device_num[index])
				Name1_list.append(dam_num[index])
				Name1_list.append('1')
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
				Name2_list.append('2')
				Name2_list=','.join(Name2_list)
				Name_list.append(Name2_list)
				time1_list = []
				for t in D_list:
					time1_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
				#num2 = len(time1_list)
				#Num_list.append(num)
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
				Name3_list.append('3')
				Name3_list=','.join(Name3_list)
				Name_list.append(Name3_list)
				time1_list = []
				for t in D_list:
					time1_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
				#num3 = len(time1_list)
				#Num_list.append(num)
		#print(Data_list)
		#print(Time_list)
		#print(Name_list)
		#print(Num_list)

	return render(request, 'label_detail_history_sametime.html', {'Data_list': json.dumps(Data_list),'Time_list': json.dumps(Time_list),'Name_list': json.dumps(Name_list),'Num_list': json.dumps(Num_list)})

#历史位移查看
def DPast_management(request):
	if request.method == "POST":
		time = request.POST.getlist('reservationtime[]')
		dam_num = request.POST.getlist('dam_num[]')
		device_num = request.POST.getlist('device_num[]')
		qian = request.POST.getlist('d1_num[]')
		hou = request.POST.getlist('d2_num[]')
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
			if dam_num[index] == "0":
				device_list = Device.objects.filter(device_num = device_num[index])
				D_list = DPast.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
				Data3_list = Average_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,station_num = dam_num[index])	
			elif dam_num[index] == "1":
				device_list = Device.objects.filter(device_num = device_num[index])
				D_list = DPast.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
				Data3_list = Average_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,station_num = dam_num[index])
			elif dam_num[index] == "2":
				device_list = Device.objects.filter(device_num = device_num[index])
				D_list = DPast.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
				Data3_list = Average_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,station_num = dam_num[index])
			elif dam_num[index] == "3":
				device_list = Device.objects.filter(device_num = device_num[index])
				D_list = DPast.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list)
				Data3_list = Average_data.objects.filter(dreal_update_time__range=(start, end)).filter(device = device_list,station_num = dam_num[index])
			Name1_list = [] 
			Name2_list = [] 
			Name3_list = [] 			
			if qian[index] =="是":
				d_list = []
				for d in Data3_list:
					d_list.append(d.d)
					Data_list.append(d.d)
				num = len(d_list)#计算list元素个数
				Num_list.append(num)
				Name1_list.append(device_num[index])
				Name1_list.append(dam_num[index])
				Name1_list.append('1')
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
				Name2_list.append('2')
				Name2_list=','.join(Name2_list)
				Name_list.append(Name2_list)
				time1_list = []
				for t in D_list:
					time1_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
				#num2 = len(time1_list)
				#Num_list.append(num)
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
				Name3_list.append('3')
				Name3_list=','.join(Name3_list)
				Name_list.append(Name3_list)
				time1_list = []
				for t in D_list:
					time1_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
					Time_list.append(t.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
				#num3 = len(time1_list)
				#Num_list.append(num)
		print(Data_list)
		print(Time_list)
		print(Name_list)
		print(Num_list)

	return render(request, 'label_detail_history.html', {'Data_list': json.dumps(Data_list),'Time_list': json.dumps(Time_list),'Name_list': json.dumps(Name_list),'Num_list': json.dumps(Num_list)})
			
		
	#return HttpResponseRedirect('/Dam_Device_management/DandL_management')
	#return HttpResponse(json.dumps({'d_list':d_list,'time_list':time_list}))
	#return render(request,'label_detail_history.html')'''


def label_detail_realtime(request):
	return render(request,'label_detail_realtime.html') 
def label_history_select(request,aid,bid):
	dam_list = Dam.objects.get(dam_num = aid)
	device_list = Device.objects.filter(device_num = bid,dam = dam_list)
	return render(request,'label_history_select.html',{'device_list':device_list})