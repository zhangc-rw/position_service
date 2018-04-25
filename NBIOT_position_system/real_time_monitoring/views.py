from real_time_monitoring import models
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json

from carrier_management.models import Carrier
from real_time_monitoring.models import Target
from django.shortcuts import HttpResponse
def postdata(request):
	if request.method == "POST":
		ID  = request.POST.get('input')
		print (request.POST['input']) 
		detailed_list = [] 	
		carrier_list = Carrier.objects.filter(carrier_num = ID) #从载体模型中取出性别为sex_front的对象

		#target_list = Target.objects.filter(device__associated_carrier__carrier_num = ID) #从载体模型中取出性别为sex_front的对象
		for carrier in carrier_list: #遍历每个目标对象
			detailed_list.append(carrier.carrier_num)
			detailed_list.append(carrier.carrier_name)
			detailed_list.append(carrier.carrier_type)
			detailed_list.append(carrier.identity_num)
			detailed_list.append(carrier.sex)		
			detailed_list.append(carrier.birthday.strftime('%Y-%m-%d'))
			detailed_list.append(carrier.nationality)
			detailed_list.append(carrier.work_unit)


		print(detailed_list)
		return HttpResponse(json.dumps({'detailed_list':detailed_list}))
		
		#return render(request,'T.html',{'coordinates_list':json.dumps(coordinates_list)})
		
		#return render(request,'T.html',{'aaa':json.dumps(jin_wei),'bbb':json.dumps(wei_jin)})


def postdata1(request):
	if request.method == "POST":
		print (request.POST['carrier_name'])
		print (request.POST['sex'])
		name  = request.POST.get('carrier_name')
		s  = request.POST.get('sex')
		carrier_list = [] 	
		c_list = Carrier.objects.filter(carrier_name = name,sex = s) #从载体模型中取出性别为sex_front的对象

		#target_list = Target.objects.filter(device__associated_carrier__carrier_num = ID) #从载体模型中取出性别为sex_front的对象
		for carrier in c_list: #遍历每个目标对象
			carrier_list.append(carrier.carrier_num)
			carrier_list.append(carrier.carrier_name)
			carrier_list.append(carrier.carrier_type)
			carrier_list.append(carrier.identity_num)
			carrier_list.append(carrier.sex)		
			carrier_list.append(carrier.birthday.strftime('%Y-%m-%d'))
			carrier_list.append(carrier.nationality)
			carrier_list.append(carrier.work_unit)


		print(carrier_list)
		return HttpResponse(json.dumps({'carrier_list':carrier_list}))
		
def track_the_playback(request):		
	return render(request,'track_the_playback.html')
def real_time_monitoring(request):		
	return render(request,'real_time_monitoring.html')
def map_real_time_monitoring(request):		
	return render(request,'map_real_time_monitoring.html')
def personnel_management_form(request):		
	return render(request,'personnel_management_form.html')


