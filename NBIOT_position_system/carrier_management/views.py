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
		#carrier_list = Carrier.objects.all()
		return render(request,'PandG_management.html',{'carrier_list_person':carrier_list_person,'carrier_list_gun':carrier_list_gun})

#人员及枪支增加
def add_form_PG(request):
	if request.method == "POST":	
		carrier_num  = request.POST['carrier_num']
		print (carrier_num)
		carrier_name  = request.POST['carrier_name']
		carrier_type  = request.POST['carrier_type']
#		identity_num = request.POST['identity_num']
#		print (identity_num)
		if request.POST['identity_num'] == "":
			identity_num  = None
		else:
			identity_num  = request.POST['identity_num']
		sex  = request.POST['sex']
		birthday  = request.POST['birthday']
		print (birthday)
		nationality  = request.POST['nationality']
		work_unit  = request.POST['work_unit']
		remarks  = request.POST['remarks']
		b_list = Carrier(carrier_num=carrier_num,carrier_name=carrier_name,carrier_type=carrier_type,identity_num=identity_num ,sex=sex,birthday=birthday,nationality=nationality,work_unit=work_unit,remarks=remarks)
		#b_list = Carrier(carrier_num=8,carrier_name='四妹',carrier_type='学员',identity_num='6' ,sex='女',birthday='2018-04-03',nationality='1',work_unit='1',remarks='1')
		b_list.save()
		b_list = Carrier.objects.all()
		#return render(request,'PandG_management.html',{'b_list' : b_list})
		return HttpResponseRedirect('/PandG_management')

#人员及枪支删除
def delete_form_PG(request,aid):
		Carrier.objects.filter(id = aid ).delete()
		carrier_list = Carrier.objects.all()
		return HttpResponseRedirect('/PandG_management')

#人员及枪支修改
def update_form_PG(request,aid):
    if request.method == "POST":
        #carrier_list = Carrier.objects.get(id = aid)
        #print (request.POST['carrier_num'])
        carrier_num  = request.POST['carrier_num']
        carrier_name  = request.POST['carrier_name']
        carrier_type  = request.POST['carrier_type']
        if request.POST['identity_num'] == "" or "None":
        	identity_num  = None
        else:
        	identity_num  = request.POST['identity_num']
        print (request.POST['identity_num'])
        sex  = request.POST['sex']
        birthday  = request.POST['birthday']
        nationality  = request.POST['nationality']
        work_unit  = request.POST['work_unit']
        remarks  = request.POST['remarks']
        Carrier.objects.filter(id = aid).update(carrier_num=carrier_num,carrier_name=carrier_name,carrier_type=carrier_type,identity_num=identity_num ,sex=sex,birthday=birthday,nationality=nationality,work_unit=work_unit,remarks=remarks)
        print(carrier_type)
        print(aid)
        #print (identity_num)

        #carrier_list.save()
        return HttpResponseRedirect('/PandG_management')

#人员查看
def personnel_management_form_update(request,aid):
		#print('line.id %s' %aid)
		carrier_list_person = Carrier.objects.get(id = aid)
		return render(request,'personnel_management_form_update.html',{'carrier_list_person' : carrier_list_person})

#枪支查看
def gun_management_form_update(request,aid):
		#print('line.id %s' %aid)
		carrier_list_gun = Carrier.objects.get(id = aid)
		return render(request,'gun_management_form_update.html',{'carrier_list_gun' : carrier_list_gun})



	
def track_the_playback(request):		
	return render(request,'track_the_playback.html')
def real_time_monitoring(request):		
	return render(request,'real_time_monitoring.html')
def map_real_time_monitoring(request):		
	return render(request,'map_real_time_monitoring.html')
def personnel_management_form(request):		
	return render(request,'personnel_management_form.html')
def gun_management_form(request):		
	return render(request,'gun_management_form.html')


