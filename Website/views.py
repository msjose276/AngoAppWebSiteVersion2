from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Partner
from .models import Person



def index(request):
    template = loader.get_template('Website/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def about(request):
    partners = Partner.objects.order_by('name')
    people = Person.objects.order_by('-role')

    template = loader.get_template('Website/about.html')
    context = {
        'partners' : partners,
        'people' : people,
    }
    return HttpResponse(template.render(context, request))



def services(request):


    template = loader.get_template('masters/master.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def process(request):

    template = loader.get_template('Website/process.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def portfolio(request):

    template = loader.get_template('Website/portfolio.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
