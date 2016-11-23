from django.shortcuts import render
#from django.urls import reverse
#from forms import ClientsForm, Myform
from django.http import HttpResponseRedirect, HttpResponse
from models import Clients
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf


def index(request):
    res = Clients.objects.all()
    return render(request, 'QA/index.html', {
        'res':res,
    })

def add(request):
    if request.method == 'POST':
        #form = ClientsForm(request.POST)
        user_id = request.POST.get('registerID')
        user_name = request.POST.get('registername')
        user_no = request.POST.get('registernum')
        user_network = request.POST.get('registernetwork')
        user_dob = request.POST.get('registerdob')
        q1 = Clients(name= user_name, mob_no= user_no, network= user_network, dob = user_dob)
        q1.save()
        #registered = True
    else:
        pass

    return render(request,'QA/add.html')

def save(request):
    if request.method == "POST":
        temp = Clients.objects.get(id = request.POST.get('id'))
        temp.name = request.POST.get('registername')
        temp.mob_no = request.POST.get('registernum')
        temp.network = request.POST.get('registernetwork')
        temp.dob = request.POST.get('registerdob')
        temp.save()

        return index(request)


def edit(request):
    if request.method == "POST" and 'edit' in request.POST:
        res = Clients.objects.get(id = request.POST.get('user_id'))
        return render(request, 'QA/edit.html', { 'id':res.id,
            'name': res.name, 'no': res.mob_no, 'network':res.network, 'dob': res.dob,
        })

    if request.method == "POST" and 'delete' in request.POST:
        Clients.objects.get(id=request.POST.get('user_id')).delete()
        return index(request)


#def delete(request):
    #if request.method == "POST":
        #res = Clients.objects.get(id = request.POST.get('this_id').delete())

       # return index(request)
