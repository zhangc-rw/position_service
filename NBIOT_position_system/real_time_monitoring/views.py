from real_time_monitoring import models
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import re
from carrier_management.models import Carrier
from real_time_monitoring.models import Target
from device_management.models import Device
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
#默认主页跳转
def old_real_time_monitoring(request):
	return HttpResponseRedirect(reverse('tiao'))
#主页
def real_time_monitoring(request):
		carrier_list = Carrier.objects.all()#全部信息
		return render(request,'real_time_monitoring.html',{'carrier_list':carrier_list})
from django.core.exceptions import ObjectDoesNotExist 
#实时坐标选择显示
def canvas_realTime(request):
    if request.method == "POST":
    	Num_list  = request.POST.get('nums')
    	#print (Num_list)
    	Num_list = re.findall(r"\d+\.?\d*",Num_list)#从字符串中取出数字
    	print (Num_list)
    	#print (Num_list[0])
    	target_list = []
    	for Num in Num_list:
    		try:
    			t_list = Target.objects.get(device__associated_carrier__carrier_num = Num)
	    		target_list.append(t_list.coordinates)
	    	except ObjectDoesNotExist:
	    		target_list.append('')
	    	'''if len(t_list) == 1 :
	    		for target in t_list:
	    			target_list.append(target.coordinates)
	    	else:
	    		target_list.append("")'''
    	print (target_list)
    return HttpResponse(json.dumps({'target_list':target_list}))
#轨迹回放
def canvas_pastTime(request):
    if request.method == "POST":
    	Num_list  = request.POST.get('nums')
    	#print (Num_list)
    	Num_list = re.findall(r"\d+\.?\d*",Num_list)#从字符串中取出数字
    	print (Num_list)
    	#print (Num_list[0])
    	target_list = []
    	for Num in Num_list:
    		try:
    			t_list = Past_Target.objects.get(device__associated_carrier__carrier_num = Num)
	    		target_list.append(t_list.coordinates)
	    	except ObjectDoesNotExist:
	    		target_list.append("信号消失")
    	print (target_list)
    return HttpResponse(json.dumps({'target_list':target_list}))
#测试1
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

#测试2
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
#页面跳转	
def track_the_playback(request):		
	return render(request,'track_the_playback.html')


