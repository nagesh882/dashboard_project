from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from admin_login.models import manage_course


def mac(request):
    template = loader.get_template("jocker.html")
    
    return HttpResponse(template.render())


def blog(request):
    template = loader.get_template("blog.html")
    
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template("contact.html")
    
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template("login.html")

    return HttpResponse(template.render())


def about(request):
    template = loader.get_template("about.html")

    return HttpResponse(template.render())


def register(request):
    template = loader.get_template("register.html")

    return HttpResponse(template.render())


def python(request):
    template = loader.get_template("python.html")
    
    return HttpResponse(template.render())

def news_single(request):
    template = loader.get_template("news-single.html")
    
    return HttpResponse(template.render())


def experence(request):
    template = loader.get_template("experence.html")
    
    return HttpResponse(template.render())


def fplace(request):
    template = loader.get_template("fplace.html")

    return HttpResponse(template.render())


def eplace(request):
    template = loader.get_template("eplace.html")
    
    return HttpResponse(template.render())

def tens(request):
    template = loader.get_template("tens.html")
    
    return HttpResponse(template.render())

def campus(request):
    template = loader.get_template("campus.html")
    
    return HttpResponse(template.render())


def clients(request):
    template = loader.get_template("clients.html")
    
    return HttpResponse(template.render())





def display_data_from_app2(request):
    app2_data = manage_course.objects.all()

    context = {
        'app2_data': app2_data
    }

    return render(request, 'all_courses.html', context)


def my_call1(request):
    return render(request, 'all_courses.html' )

