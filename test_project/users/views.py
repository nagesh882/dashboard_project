from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from users.models import Employees

def index(request):
    template = loader.get_template("dashbord.html")

    return HttpResponse(template.render())
    # return render(request, 'dashbord.html')


def chart(request):
    template = loader.get_template("chartjs.html")

    return HttpResponse(template.render())
    # return render(request, 'chartjs.html')


def forms(request):
    template = loader.get_template("basic_elements.html")
    # return render(request, 'basic_elements.html')

    return HttpResponse(template.render())

def icons(request):
    template = loader.get_template("mdi.html")
    # return render(request, 'mdi.html')

    return HttpResponse(template.render())

def sample1(request):
    template = loader.get_template("blank-page.html")
    # return render(request, 'blank-page.html')

    return HttpResponse(template.render())

def sample2(request):
    template = loader.get_template("error-404.html")
    # return render(request, 'error-404.html')

    return HttpResponse(template.render())

def sample3(request):
    template = loader.get_template("error-500.html")
    # return render(request, 'error-500.html')

    return HttpResponse(template.render())

def sample4(request):
    template = loader.get_template("login.html")
    # return render(request, 'login.html')

    return HttpResponse(template.render())

def sample5(request):
    template = loader.get_template("register.html")
    # return render(request, 'register.html')

    return HttpResponse(template.render())

def table(request):
    template = loader.get_template("basic-table.html")

    return HttpResponse(template.render())

def ui1(request):
    template = loader.get_template("buttons.html")
    # return render(request, 'buttons.html')

    return HttpResponse(template.render())

def ui2(request):

    template = loader.get_template("typography.html")
    # return render(request, 'typography.html')

    return HttpResponse(template.render())


def vince(request):
    
    # template = loader.get_template("index.html")
    
    emp = Employees.objects.all()

    context = {
        "emp":emp,
    }

    return render(request, 'index.html', context)

    # return HttpResponse(template.render(context))

def add(request):
    emp=Employees.objects.all()
    context = {
        "emp":emp
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        emp.save()
        return redirect('index')
    return render(request, 'index.html', context)
    


def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        emp.save()
        return redirect('index')

    return redirect(request, 'index.html')

def delete(request, id):
    if request.method=="POST":
        data=Employees.objects.filter(id=id)
        data.delete()
        return redirect("index")   
          