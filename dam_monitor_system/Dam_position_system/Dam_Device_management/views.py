from django.shortcuts import render
from Dam_Device_management.models import Dam
from Dam_Device_management.models import Device
from django.core.exceptions import ObjectDoesNotExist 
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.http import HttpResponse



# Create your views here.

#大坝与设备信息显示
def DandL_management(request):
	dam_list = Dam.objects.all()
	device_list = Device.objects.all()
	return render(request,'DandL_management.html',{'dam_list':dam_list,'device_list':device_list})

#大坝增加
def add_form_Dam(request):
	if request.method == "POST":
		dam_num = request.POST['dam_num']
		dam_name = request.POST['dam_name']
		dam_status = request.POST['dam_status']
		port_num = request.POST['port_num']
		domain_name = request.POST['domain_name']
		D_list = Dam(dam_num = dam_num,dam_name = dam_name,dam_status = dam_status,port_num = port_num,domain_name = domain_name)
		D_list.save()
		return HttpResponseRedirect('/Dam_Device_management/DandL_management')

#设备增加
def add_form_Device(request):
	if request.method == "POST":
		device_num = request.POST['device_num']
		card_num = request.POST['card_num']
		power = request.POST['power']
		x = request.POST['x']
		y = request.POST['y']
		z = request.POST['z']
		remark = request.POST['remark']
		dam_num = request.POST['dam_num']
		#由大坝编号查询大坝信息
		dam_list = Dam.objects.get(dam_num= dam_num)
		d_list = Device()
		d_list.device_num = device_num
		d_list.card_num = card_num
		d_list.power = power
		d_list.x = x
		d_list.y = y
		d_list.z = z
		d_list.remark = remark
		d_list.dam = dam_list
		d_list.save()
		return HttpResponseRedirect('/Dam_Device_management/DandL_management')

#大坝删除
def delete_form_Dam(request,aid):
		#根据获取ID，删除信息
		Dam.objects.filter(id = aid ).delete()
		return HttpResponseRedirect('/Dam_Device_management/DandL_management')
#设备删除
def delete_form_Device(request,aid):
		#根据获取ID，删除信息
		Device.objects.filter(id = aid ).delete()
		return HttpResponseRedirect('/Dam_Device_management/DandL_management')

#大坝修改
def update_form_Dam(request,aid):
	if request.method == "POST":
		dam_num = request.POST['dam_num']
		dam_name = request.POST['dam_name']
		port_num = request.POST['port_num']
		domain_name = request.POST['domain_name']
		dam_status = request.POST['dam_status']
		'''dam_grade = request.POST['dam_grade']
		information = request.POST['information']
		'''
		Dam.objects.filter(id = aid).update(dam_num=dam_num,dam_name=dam_name,dam_status=dam_status,port_num=port_num,domain_name=domain_name)

		'''update(dam_num=dam_num,dam_name=dam_name,dam_grade=dam_grade,
        	dam_status=dam_status,information=information)'''
		return HttpResponseRedirect('/Dam_Device_management/DandL_management')

#设备修改
def update_form_Device(request,aid):
	if request.method == "POST":
		device_num = request.POST['device_num']
		card_num = request.POST['card_num']
		power = request.POST['power']
		x = request.POST['x']
		y = request.POST['y']
		z = request.POST['z']
		remark = request.POST['remark']
		dam_num = request.POST['dam_num']
		#获得大坝信息
		dam_list = Dam.objects.get(dam_num = dam_num)
		Device.objects.filter(id = aid).update(device_num=device_num,card_num=card_num,power=power,
        	x=x,y=y,z=z,remark=remark,dam=dam_list)
		return HttpResponseRedirect('/Dam_Device_management/DandL_management')

#大坝查看
def dam_management_form_update(request,aid):
		dam_list = Dam.objects.get(id = aid)
		return render(request,'dam_management_form_update.html',{'dam_list' : dam_list})
#设备查看
def device_management_form_update(request,aid):
		device_list = Device.objects.get(id = aid)
		return render(request,'device_management_form_update.html',{'device_list' : device_list})

#添加页面跳转
def dam_management_form(request):		
	return render(request,'dam_management_form.html')   

def device_management_form(request):		
	return render(request,'device_management_form.html')  