from django.shortcuts import render
from Warning_management.models import WReal
from Warning_management.models import WPast
from django.http import HttpResponse
from django.http import JsonResponse
import datetime
# Create your views here.

#实时告警信息
def WReal_management(request):
	W_list = WReal.objects.all()
	WReal_list = []
	for i in W_list:
		WReal_list.append(i.device)
		WReal_list.append(i.stationID)
		WReal_list.append(i.wreal_time.strftime("%Y-%m-%d %H:%M:%S"))
		WReal_list.append(i.wreal_type)
		WReal_list.append(i.Logo)
	print(WReal_list)	
	WReal.objects.all().delete()
	#return HttpResponse(json.dumps({'WReal_list':WReal_list}))
	return render(request,'label_detail.html',{'WReal_list':WReal_list})
	#return HttpResponseRedirect('/XXX/XXX')
	
#历史告警信息
def WPast_management(request):
	start = '2018-06-10 02:06:11'
	end = '2018-06-12 02:09:11'
	start_date = datetime.datetime.strptime(start,'%Y-%m-%d %H:%M:%S')
	end_date = datetime.datetime.strptime(end,'%Y-%m-%d %H:%M:%S')
	print(start_date)
	print(end_date)
	W_list = WPast.objects.filter(wreal_time__range=(start_date, end_date))
	#W_list = WReal.objects.filter(wreal_time__day=12)
	#W_list = WReal.objects.all()
	WPast_list = []
	for i in W_list:
		WPast_list.append(i.device)
		WPast_list.append(i.stationID)
		WPast_list.append(i.wreal_time.strftime("%Y-%m-%d %H:%M:%S"))
		WPast_list.append(i.wreal_type)
		WPast_list.append(i.Logo)
	print(WPast_list)
	return render(request,'XXX.html',{'WPast_list':WPast_list})	