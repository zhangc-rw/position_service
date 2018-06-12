from django.shortcuts import render
from Warning_management.models import WReal
from Warning_management.models import WPast
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
#实时告警信息
def WReal_management(request):
	W_list = WReal.objects.all()
	WReal_list = []
	for i in W_list:
		WReal_list.append(i.device)
		WReal_list.append(i.stationID)
		WReal_list.append(i.wreal_time)
		WReal_list.append(i.wreal_type)
		WReal_list.append(i.Logo)
	print(WReal_list)	
	WReal.objects.all().delete()
	return HttpResponse(json.dumps({'WReal_list':WReal_list}))
	#return render(request,'label_detail.html',{'WReal_list':WReal_list})
	#return HttpResponseRedirect('/XXX/XXX')
	
#历史告警信息
def WPast_management(request):
	WPast_list = WPast.objects.all()
	return render(request,'XXX.html',{'WPast_list':WPast_list})