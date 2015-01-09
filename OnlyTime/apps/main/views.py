from django.shortcuts import render,render_to_response
import datetime

def index_page(request):
	now = datetime.datetime.now()
	current_time = now.strftime('%Y%m%d')
	return render(request,'base.html',{'current_time':current_time})