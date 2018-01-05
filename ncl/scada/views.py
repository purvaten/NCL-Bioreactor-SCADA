from django.shortcuts import render
from scada.models import Values
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	return render(request, 'scada/home.html')

def contact(request):
	return render(request, 'scada/basic.html', {'content':['If you want to contact me please email me.', 'purva.tendulkar@gmail.com']})

def login(request):
	return render(request, 'scada/login.html')

def dashboard(request):
	#return render(request, 'scada/dashboard.html')
	context = RequestContext(request)
	category_list = Values.objects.order_by('-start_date')[:5]
	context_dict = {'values': category_list}
	return render_to_response('scada/dashboard.html', context_dict, context)

def stats(request):
	return render(request, 'scada/stats.html')

def history(request):
	return render(request, 'scada/history.html')

def control(request):
	return render(request, 'scada/control.html')
