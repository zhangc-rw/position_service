from django.shortcuts import render

# Create your views here.
from Displacement_management.models import DReal
from Displacement_management.models import DPast
#实时位移查看
def DReal_management(request):
	DReal_list = DReal.objects.all()
		return render(request,'XXX.html',{'DReal_list':DReal_list})



#历史位移查看
def DPast_management(request):
	start = '2018-06-10 02:06:11'
	end = '2018-06-12 02:09:11'
	start_date = datetime.datetime.strptime(start,'%Y-%m-%d %H:%M:%S')
	end_date = datetime.datetime.strptime(end,'%Y-%m-%d %H:%M:%S')
	print(start_date)
	print(end_date)
	D_list = DPast.objects.filter(dreal_update_time__range=(start_date, end_date))
	#W_list = WReal.objects.filter(wreal_time__day=12)
	#W_list = WReal.objects.all()
	DPast_list = []
	for i in D_list:
		DPast_list.append(i.device)
		WPast_list.append(i.stationID)
		WPast_list.append(i.dreal_update_time.strftime("%Y-%m-%d %H:%M:%S"))
		WPast_list.append(i.temperature)
		WPast_list.append(i.voltage)
		WPast_list.append(i.d1)
		WPast_list.append(i.d2)
		WPast_list.append(i.d3)
		WPast_list.append(i.d4)
		WPast_list.append(i.d5)
		WPast_list.append(i.d6)
		WPast_list.append(i.d7)
		WPast_list.append(i.d8)
		WPast_list.append(i.x)
		WPast_list.append(i.y)
		WPast_list.append(i.z)
		WPast_list.append(i.d)
		WPast_list.append(i.dx)
		WPast_list.append(i.dy)
		WPast_list.append(i.dz)
	print(DPast_list)
		return render(request,'XXX.html',{'DPast_list':DPast_list})