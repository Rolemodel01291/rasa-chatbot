from django.shortcuts import render
from .models import Report
from .models import Heat_map
from django.http import HttpResponse

def index_view(request):
	heat_map = Heat_map.objects.all()	
	return render(request, 'index.html',{'heat_maps':heat_map})

def get_garan(request):
	print("get_garan_____________")
	heat_map = Heat_map.objects.all()
	report = Report.objects.filter( ticker_db='GARAN_TI_EQUITY').values('report_content')
	text = ''
	for i in report:
		# report = i
		text = i['report_content']
		print(i['report_content'])	
	return HttpResponse(text)

