from django.shortcuts import render

# Create your views here.
#指令与参数信息显示
def XXX_management(request):
	order_list = Order.objects.all()
	parameter_list = Parameter.objects.all()
	return render(request,'XXX.html',{'order_list':order_list,'parameter_list':parameter_list})

#指令信息
def add_form_Order(request):
	if request.method == "POST":
		dam_num = request.POST['dam_num']
		order_type = request.POST['order_type']
		order_data = request.POST['order_data']
		stationID = request.POST['stationID']
		#由大坝编号查询大坝信息
		dam_list = Dam.objects.get(dam_num= dam_num)
		o_list = Order()
		o_list.order_type = order_type
		o_list.order_data = order_data
		o_list.stationID = stationID
		o_list.dam = dam_list
		o_list.save()
		return HttpResponseRedirect('/carrier_management/PandG_management')

#参数信息
def add_form_Dam_Parameter(request):
	if request.method == "POST":
		dam_num = request.POST['dam_num']
		parameter_data = request.POST['parameter_data']
		#由大坝编号查询大坝信息
		dam_list = Dam.objects.get(dam_num= dam_num)
		p_list = Parameter()
		p_list.parameter_data = parameter_data
		p_list.dam = dam_list
		p_list.save()
		return HttpResponseRedirect('/carrier_management/PandG_management')