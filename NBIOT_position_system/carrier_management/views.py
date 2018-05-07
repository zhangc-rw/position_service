from real_time_monitoring import models
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from carrier_management.models import Carrier
from real_time_monitoring.models import Target
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.template import loader, Context, RequestContext  

#人员及枪支列表显示
def PandG_management(request):
		carrier_list_gun = Carrier.objects.filter(carrier_type__gt= 100,carrier_type__lte = 200)#筛选大于多少
		carrier_list_person = Carrier.objects.filter(carrier_type__gte = 1,carrier_type__lte = 100)#筛选小于多少
		return render(request,'PandG_management.html',{'carrier_list_person':carrier_list_person,'carrier_list_gun':carrier_list_gun})

#人员及枪支增加
def add_form_PG(request):
	if request.method == "POST":	
		carrier_num  = request.POST['carrier_num']
		carrier_name  = request.POST['carrier_name']
		carrier_type  = request.POST['carrier_type']
		#判断字符串，为空输出none
		if request.POST['identity_num'] == "":
			identity_num  = None
		else:
			identity_num  = request.POST['identity_num']
		#print (identity_num)
		sex  = request.POST['sex']
		birthday  = request.POST['birthday']
		#查看日期格式
		#print (birthday)
		nationality  = request.POST['nationality']
		work_unit  = request.POST['work_unit']
		remarks  = request.POST['remarks']
		#存储各项数据
		b_list = Carrier(carrier_num=carrier_num,carrier_name=carrier_name,carrier_type=carrier_type,identity_num=identity_num ,sex=sex,birthday=birthday,nationality=nationality,work_unit=work_unit,remarks=remarks)
		b_list.save()
		return HttpResponseRedirect('/carrier_management/PandG_management')

#人员及枪支删除
def delete_form_PG(request,aid):
		#根据获取ID，删除信息
		Carrier.objects.filter(id = aid ).delete()
		carrier_list = Carrier.objects.all()
		return HttpResponseRedirect('/carrier_management/PandG_management')

#人员及枪支修改
def update_form_PG(request,aid):
    if request.method == "POST":
        carrier_num  = request.POST['carrier_num']
        carrier_name  = request.POST['carrier_name']
        carrier_type  = request.POST['carrier_type']
		#判断字符串，为空或‘none’输出none
        if (request.POST['identity_num'] == "") or (request.POST['identity_num'] == "None"):
        	identity_num  = None
        else:
        	identity_num = request.POST['identity_num']
        #print(identity_num)
        sex  = request.POST['sex']
        birthday  = request.POST['birthday']
        nationality  = request.POST['nationality']
        work_unit  = request.POST['work_unit']
        remarks  = request.POST['remarks']
        #获取id,更改信息
        Carrier.objects.filter(id = aid).update(carrier_num=carrier_num,carrier_name=carrier_name,carrier_type=carrier_type,identity_num=identity_num ,sex=sex,birthday=birthday,nationality=nationality,work_unit=work_unit,remarks=remarks)
        return HttpResponseRedirect('/carrier_management/PandG_management')

#人员查看
def personnel_management_form_update(request,aid):
		carrier_list_person = Carrier.objects.get(id = aid)
		return render(request,'personnel_management_form_update.html',{'carrier_list_person' : carrier_list_person})

#枪支查看
def gun_management_form_update(request,aid):
		carrier_list_gun = Carrier.objects.get(id = aid)
		return render(request,'gun_management_form_update.html',{'carrier_list_gun' : carrier_list_gun})



#跳转页面链接	

def personnel_management_form(request):		
	return render(request,'personnel_management_form.html')
def gun_management_form(request):		
	return render(request,'gun_management_form.html')


