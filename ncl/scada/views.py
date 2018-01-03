from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'scada/home.html')

def contact(request):
	return render(request, 'scada/basic.html', {'content':['If you want to contact me please email me.', 'purva.tendulkar@gmail.com']})

def login(request):
	return render(request, 'scada/login.html')
