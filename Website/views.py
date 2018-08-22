from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Partner
from .models import Person
from .models import Project
from .models import Photo
from django.core.mail import EmailMessage,BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect



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

    if request.POST:
        first_name_from_html = request.POST['first_name']
        last_name_from_html = request.POST['last_name']
        email_from_html = request.POST['email']
        cellphone_from_html = request.POST['cellphone']
        content_from_html = request.POST['content']
        tipo_de_servico_from_html = request.POST['tipo_de_servico']
        message_sent="";

        context = {
            'message_sent':message_sent,
        }
        #send email to the user
        subject = 'Contacto com a AngoApp'
        message = 'A sua mensagem foi recebida com sucesso. A Angoapp irá contactá-lo brevemente.'

        context = {
            'message_sent': message,
        }
        from_email = 'angoapp2016@gmail.com'
        message_from_client='tipo de servico: '+tipo_de_servico_from_html+'\nMENSAGEM: '+ content_from_html +'\n\n nome: '+first_name_from_html+' '+last_name_from_html+ '\n numero de telefone: ' + cellphone_from_html + '\nemail: ' + email_from_html
        try:
            #send notification to the client and to angoapp email
            email_to_client = EmailMessage(subject, message, to=[email_from_html])
            email_to_angoapp = EmailMessage('PEDIDO PELO WEBSITE',message_from_client, to=[from_email])
            email_to_client.send()
            email_to_angoapp.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse(template.render(context, request))

    return HttpResponse(template.render(context, request))

def handler404(request):
    template = loader.get_template('Website/portfolio.html')
    error='pagina nao encontrada'
    context = {
        'error': error,
    }
    return HttpResponse(template.render(context, request))

def portfolio(request):
    projects = Project.objects.order_by('title')

    template = loader.get_template('Website/portfolio.html')
    context = {
        'projects' : projects,
    }
    return HttpResponse(template.render(context, request))


def project_detail(request, keyword):
    project = Project.objects.get(title=keyword)
    photos = Photo.objects.filter(projectName=project.id)

    #projects = Project.objects.order_by('title')

    template = loader.get_template('Website/portfolio.html')
    context = {
        'project' : project,
        'photos':photos,
    }
    return HttpResponse(template.render(context, request))