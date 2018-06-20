from django.shortcuts import render

# Create your views here.
from Displacement_management.models import DReal
from Displacement_management.models import DPast
from Dam_Device_management.models import Device
from Dam_Device_management.models import Dam
import datetime
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
def DPast_management(request,aid,bid):
	if request.method == "POST":
		time = request.POST['reservationtime']
		print(time)
		start =time[0:16]
		end = time[-16:]
		start_date = datetime.datetime.strptime(start,'%Y-%m-%d %H:%M')
		end_date = datetime.datetime.strptime(end,'%Y-%m-%d %H:%M')
		print(start_date)
		print(end_date)
		dam_list = Dam.objects.get(dam_num = aid)
		device_list = Device.objects.filter(device_num = bid,dam = dam_list)
		D_list = DPast.objects.filter(dreal_update_time__range=(start_date, end_date)).filter(device = device_list)
		DPast_list = []
		for i in D_list:
			DPast_list.append(i.device)
			DPast_list.append(i.stationID)
			DPast_list.append(i.dreal_update_time.strftime("%Y-%m-%d %H:%M"))
			DPast_list.append(i.temperature)
			DPast_list.append(i.voltage)
			DPast_list.append(i.d1)
			DPast_list.append(i.d2)
			DPast_list.append(i.d3)
			DPast_list.append(i.d4)
			DPast_list.append(i.d5)
			DPast_list.append(i.d6)
			DPast_list.append(i.d7)
			DPast_list.append(i.d8)
			DPast_list.append(i.x)
			DPast_list.append(i.y)
			DPast_list.append(i.z)
			DPast_list.append(i.d)
			DPast_list.append(i.dx)
			DPast_list.append(i.dy)
			DPast_list.append(i.dz)
		print(DPast_list)
		return render(request,'label_detail_history.html',{'DPast_list':DPast_list})


def label_detail_realtime(request):
	return render(request,'label_detail_realtime.html') 
def label_history_select(request,aid,bid):
	dam_list = Dam.objects.get(dam_num = aid)
	device_list = Device.objects.filter(device_num = bid,dam = dam_list)
	return render(request,'label_history_select.html',{'device_list':device_list})