from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from admin_login.models import manage_course
from admin_login.models import manage_student

# model_2

def login(request):
    return render(request, 'admin_login.html')


def display(request):
    return render(request, 'admin_home.html')


def vince1(request):
    
    # template = loader.get_template("index.html")
    
    equal = manage_course.objects.all()

    context = {
        "equal":equal,
    }

    return render(request, 'admin_manage_course.html', context)

    # return HttpResponse(template.render(context))

def add1(request):
    equal = manage_course.objects.all()
    context = {
        "equal":equal
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        learning_hours = request.POST.get('learning_hours')
        subject = request.POST.get('subject')

        equal = manage_course(
            title = title,
            description = description,
            start_date = start_date,
            end_date = end_date,
            learning_hours = learning_hours,
            subject = subject
        )
        equal.save()
        return redirect('index1')
    return render(request, 'admin_manage_course.html', context)
    

def update1(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        learning_hours = request.POST.get('learning_hours')
        subject = request.POST.get('subject')

        equal = manage_course(
            id = id,
            title = title,
            description = description,
            start_date = start_date,
            end_date = end_date,
            learning_hours = learning_hours,
            subject = subject
        )
        equal.save()
        return redirect('index1')

    return redirect(request, 'admin_manage_course.html')

def delete1(request, id):
    if request.method=="POST":
        data1 = manage_course.objects.all()
        data1.delete()
        return redirect("index1")



# model_2

def vince2(request):
    
    # template = loader.get_template("index.html")
    
    correct = manage_student.objects.all()

    context = {
        "correct":correct,
    }

    return render(request, 'admin_manage_student.html', context)

    # return HttpResponse(template.render(context))

def add2(request):
    correct=manage_student.objects.all()
    context = {
        "correct":correct
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        aadhar = request.POST.get('aadhar')
        course = request.POST.get('course')

        correct = manage_student(
            name = name,
            mobile = mobile,
            email = email,
            dob = dob,
            aadhar = aadhar,
            course = course,
        )
        correct.save()
        return redirect('index2')
    return render(request, 'admin_manage_student.html', context)
    


def update2(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        aadhar = request.POST.get('aadhar')
        course = request.POST.get('course')

        correct = manage_student(
            id = id,
            name = name,
            mobile = mobile,
            email = email,
            dob = dob,
            aadhar = aadhar,
            course = course,
        )
        correct.save()
        return redirect('index2')

    return redirect(request, 'admin_manage_student.html')

def delete2(request, id):
    if request.method=="POST":
        data2 = manage_student.objects.filter(id=id)
        data2.delete()
        return redirect("index2")   
          