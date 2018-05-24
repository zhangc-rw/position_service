from real_time_monitoring import models
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from carrier_management.models import Carrier
from real_time_monitoring.models import Target
from device_management.models import Device
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.template import loader, Context, RequestContext  

#设备列表显示
def XXX_management(request):
	device_list = Device.objects.all()
	return render(request,'XXX.html',{'device_list':device_list})

#设备增加
def add_form_XXX(request):
	if request.method == "POST":	
		carrier_num  = request.POST['carrier_num']
		device_num  = request.POST['device_num']
		device_type  = request.POST['device_type']
		#print (identity_num)
		card_num  = request.POST['card_num']
		remark  = request.POST['remark']
		#存储各项数据
		carrier = Carrier.objects.get(carrier_num = carrier_num)
		b_list = Device()
		#b_list.associated_carrier.carrier_num
		b_list.device_num = 1
		b_list.device_type = 1
		b_list.card_num = 1
		b_list.remark = 1
		b_list.associated_carrier = carrier
		b_list.save()
		return HttpResponseRedirect('/device_management/XXX_management')

#设备删除
def delete_form_XXX(request,aid):
		#根据获取ID，删除信息
		Device.objects.filter(id = aid ).delete()
		device_list = Device.objects.all()
		return HttpResponseRedirect('/device_management/XXX_management')

#设备修改
def update_form_XXX(request,aid):
    if request.method == "POST":
		carrier_num  = request.POST['carrier_num']
		device_num  = request.POST['device_num']
		device_type  = request.POST['device_type']
		card_num  = request.POST['card_num']
		remark  = request.POST['remark']
        #获取carrier_num,更改信息
        carrier = Carrier.objects.get(carrier_num = carrier_num)
        Device.objects.filter(device_num = 8).update(device_num = 9,device_type = 7 ,
			card_num = 7,remark = 7 , associated_carrier = carrier)
        return HttpResponseRedirect('/carrier_management/XXX_management')

#设备查看
def XXX_management_form_update(request,aid):
		device_list = Device.objects.get(id = aid)
		return render(request,'XXX_management_form_update.html',{'device_list' : device_list})





#跳转页面链接	

def XXX_management_form(request):		
	return render(request,'XXX_management_form.html')



