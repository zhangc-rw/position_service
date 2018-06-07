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
	DPast_list = DReal.objects.all()
		return render(request,'XXX.html',{'DPast_list':DPast_list})