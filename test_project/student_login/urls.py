from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('email', views.only, name="email"),

    path('student_base', views.student_base, name="student_base"),

    # path('student_profile', views.my_call, name="student_profile"),

    path('student_home', views.home_page, name="student_home"),

 
    # path('display_app1_data', views.display_data_from_app1, name='display_app1_data'),

    path('login',views.login,name="milogin"),
    
    path('validate_otp',views.validate_otp,name="validate_otp"),

]