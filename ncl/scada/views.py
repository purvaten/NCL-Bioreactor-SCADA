from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from scada.models import Values
from .forms import DataForm
from django.utils import timezone
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
#from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    return render(request, 'scada/home.html')

def contact(request):
    return render(request, 'scada/contact.html', {'content':['If you want to contact me please email me.', 'purva.tendulkar@gmail.com']})

def projects(request):
    return render(request, 'scada/projects.html')

def people(request):
    return render(request, 'scada/people.html')

def logged_out(request):
    return render(request, 'registration/logged_out.html')

@csrf_protect
def dashboard(request):
    context = RequestContext(request)
    category_list = Values.objects.order_by('-start_date')
    context_dict = {'values': category_list}
    return render_to_response('scada/dashboard.html', context_dict, context)

def stats(request):
    return render(request, 'scada/stats.html')

#@staff_member_required
@csrf_protect
def control(request):
    """Control."""
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.start_date = timezone.now()
            post.save()
            return redirect('dashboard')
    else:
        form = DataForm()
    return render(request, 'scada/control.html', {'form': form})


# Trying to pass parameter to send_data which specifies which table entry is needed
# This will be called in a for loop in the template to display the contents
@csrf_protect
def send_data(request, index):
    """Sending data."""
    category_list = Values.objects.values('pressure', 'temperature', 'ph', 'levels', 'start_date').order_by('-start_date')[:index]

    users_list = list(category_list)
    result = {}
    for d in users_list:
        result.update(d)

    x = result['start_date']
    # y = x.strftime('%m/%d/%Y')
    y = x.strftime('%b. %d, %Y, %I:%M %P.')
    result['start_date'] = y

    return HttpResponse(json.dumps(result), content_type='application/json')

@csrf_protect
def get_num(request):
    c = Values.objects.count()
    return HttpResponse(json.dumps(c), content_type='application/json')
