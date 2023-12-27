from django.shortcuts import render, redirect
import random
from admin_login.models import manage_student, manage_course
from django.core.mail import send_mail

# def my_call(request):
#     return render(request, 'student_profile.html' )


# def display_data_from_app1(request):
#     app1_data = manage_student.objects.all()

#     context = {
#         'app1_data': app1_data
#     }

#     return render(request, 'student_manage_profile.html', context)


# def my_fun(request):
#     return render(request, 'student_login.html')


def home_page(request):
    return render(request, 'student_home.html')


def student_base(request):
    return render(request,"student_base.html")


def only(request):
    return render(request,"onlymail.html")




def generate_otp():
    return str(random.randint(100000, 999999))

def login(request):
    if request.method == "POST":
        email = request.POST["email1"]
        
        otp = generate_otp()
          
        send_mail(
            'Subject: Your OTP',
            f'Your OTP is: {otp}',
            'yashchavanee05@gmail.com',
            [email],
            fail_silently=False,

        )

        # Save the OTP in the session for later validation
        request.session['otp'] = otp
        request.session['email'] = email
        return redirect("validate_otp")


    return render(request,"onlymail.html")



def validate_otp(request):
    if request.method == 'POST':
        user_entered_otp = request.POST["otp"]
        stored_otp = request.session['otp']
        print(stored_otp)
        email_store = request.session['email']

        print(email_store)
        if user_entered_otp == stored_otp :

            data=manage_student.objects.filter(email=email_store )
            print(data)
            context={"data":data}
            if len(data) is not 0 :
                print("yes")

                return render(request, "student_base.html",context)
            
    return render(request, "onlyotp.html")

            
            