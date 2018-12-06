from django.shortcuts import render,reverse
from Dam_Device_management.models import Dam
from Dam_Device_management.models import Landing_record
from Dam_Device_management.models import Device
from django.core.exceptions import ObjectDoesNotExist 
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.http import HttpResponse

from django.contrib.auth import authenticate, login as d_login, logout as d_logout
#from django.views.decorators.http import require_http_methods
import json
import socket
import uuid
from django.utils import timezone

# Create your views here.
#127跳转
def Old_login(request):
	return HttpResponseRedirect(reverse('tiao'))
#退出
def Login_out(request):
	if request.session.get('userName'):
		request.session.clear() 
		#d_logout(request)
		return render(request, 'islog.html')
	else:
		return render(request, 'login.html')
def Login(request):
	if request.method == 'GET':
		#user = request.user
		name = request.session.get('userName')
		#request.session.set_expiry(0) 
		#if user.is_authenticated:
		if name != None:
			print(111)   #如果已登录
			return render(request, 'DandL_management.html')
		else:
			print(222)
			return render(request, 'login.html')
	if request.method == 'POST':
	 	userName = request.POST['username']
	 	userPassword = request.POST['password']
	 	print (userName)
	 	print (userPassword)
	 	user = authenticate(username=userName, password=userPassword) #django认证
	 	if user is not None:
	 		if user.is_active:  # 用户 在 Admin后台，被设置为 “激活状态”
	 			request.session['userName'] = userName
	 			#request.session.set_expiry(0)
	 			#request.session.set_expiry()
	 			#request.session['is_login'] = True
	 			#d_login(request, user)  #将 登录信息 存储到 django自身的 login模块 中
	 			# 获取主机名
	 			Computer_name = socket.gethostname()
	 			Computer_ip = socket.gethostbyname(Computer_name)
	 			Landing_time = timezone.now()
	 			Landing_record_list = Landing_record(Computer_name = Computer_name,Computer_ip=Computer_ip,Landing_time=Landing_time)
	 			Landing_record_list.save()
	 			print(Computer_name)
	 			print(Computer_ip)
	 			print(Landing_time)
	 			return render(request,'DandL_management.html')
	 		else:
	 			print(222222)
	 			return render(request,'DandL_management.html')
	 	else:
	 		print(3333333)
	 		return render(request,'logwrong.html')

#大坝与设备信息显示
def DandL_management(request):
	if request.session.get('userName'):
		dam_list = Dam.objects.all()
		device_list = Device.objects.all()
		return render(request,'DandL_management.html',{'dam_list':dam_list,'device_list':device_list})
	else:
		return render(request, 'login.html')
#大坝与设备列表显示
def List_show_realTime(request):
	if request.session.get('userName'):
		dam_list = Dam.objects.all()
		device_list = Device.objects.filter(at_tip = 1)
		station_list = Device.objects.filter(at_tip = 0)
		return render(request,'list_show_realTime.html',{'dam_list':dam_list,'device_list':device_list,'station_list':station_list})
	else:
		return render(request, 'login.html')
def List_show_history(request):
	if request.session.get('userName'):
		dam_list = Dam.objects.all()
		dam_num_list =[]
		for d in dam_list:
			dam_num_list.append(d.dam_num)	
		#print (dam_num_list)
		device_list_123 = Device.objects.filter(at_tip =  1,dam_id = 1)
		device_list_456 = Device.objects.filter(at_tip =  1,dam_id = 2)
		device_num_list =[]
		device_num_list_1 = []
		device_num_list_2 = []
		device_num_total_list = []
		for d in device_list_123:
			device_num_list_1.append(d.device_num)
			device_num_list.append(d.device_num)
		device_num_total_list.append(len(device_num_list_1))
		for d in device_list_456:
			device_num_list_2.append(d.device_num)
			device_num_list.append(d.device_num)
		device_num_total_list.append(len(device_num_list_2))
		#print (device_num_list)
		station_list_123 = Device.objects.filter(at_tip =  0,dam_id = 1)
		station_list_456 = Device.objects.filter(at_tip =  0,dam_id = 2)
		station_num_list= []
		station_num_list_1 = []
		station_num_list_2 = []
		station_num_total_list = []
		for d in station_list_123:
			station_num_list_1.append(d.device_num)
			station_num_list.append(d.device_num)
		station_num_total_list.append(len(station_num_list_1))
		for d in station_list_456:
			station_num_list_2.append(d.device_num)
			station_num_list.append(d.device_num)
		station_num_total_list.append(len(station_num_list_2))
		print(device_num_total_list)
		print(station_num_total_list)
		return render(request,'list_show_history.html',{'device_num_total_list':json.dumps(device_num_total_list),'station_num_total_list':json.dumps(station_num_total_list),'dam_num_list':json.dumps(dam_num_list),'device_num_list':json.dumps(device_num_list),'station_num_list':json.dumps(station_num_list)})
	else:
		return render(request, 'login.html')



#大坝增加
def add_form_Dam(request):
	if request.session.get('userName'):
		if request.method == "POST":
			dam_num = request.POST['dam_num']
			dam_name = request.POST['dam_name']
			dam_status = request.POST['dam_status']
			port_num = request.POST['port_num']
			domain_name = request.POST['domain_name']
			D_list = Dam(dam_num = dam_num,dam_name = dam_name,dam_status = dam_status,port_num = port_num,domain_name = domain_name)
			D_list.save()
			return HttpResponseRedirect('/Dam_Device_management/DandL_management')
	else:
		return render(request, 'login.html')
#设备增加
def add_form_Device(request):
	if request.session.get('userName'):
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
	else:
		return render(request, 'login.html')
#大坝删除
def delete_form_Dam(request,aid):
	if request.session.get('userName'):
		#根据获取ID，删除信息
		Dam.objects.filter(id = aid ).delete()
		return HttpResponseRedirect('/Dam_Device_management/DandL_management')
	else:
		return render(request, 'login.html')
#设备删除
def delete_form_Device(request,aid):
	if request.session.get('userName'):
		#根据获取ID，删除信息
		Device.objects.filter(id = aid ).delete()
		return HttpResponseRedirect('/Dam_Device_management/DandL_management')
	else:
		return render(request, 'login.html')

#大坝修改
def update_form_Dam(request,aid):
	if request.session.get('userName'):
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
	else:
		return render(request, 'login.html')

#设备修改
def update_form_Device(request,aid):
	if request.session.get('userName'):
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
	else:
		return render(request, 'login.html')

#大坝查看
def dam_management_form_update(request,aid):
	if request.session.get('userName'):
		dam_list = Dam.objects.get(id = aid)
		return render(request,'dam_management_form_update.html',{'dam_list' : dam_list})
	else:
		return render(request, 'login.html')
#设备查看
def device_management_form_update(request,aid):
	if request.session.get('userName'):
		device_list = Device.objects.get(id = aid)
		return render(request,'device_management_form_update.html',{'device_list' : device_list})
	else:
		return render(request, 'login.html')

#添加页面跳转
def dam_management_form(request):
	if request.session.get('userName'):		
		return render(request,'dam_management_form.html')   
	else:
		return render(request, 'login.html')


def device_management_form(request):
	if request.session.get('userName'):		
		return render(request,'device_management_form.html')  
	else:
		return render(request, 'login.html')