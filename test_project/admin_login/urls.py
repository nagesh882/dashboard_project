from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.login, name="admin_login"),

    path('home', views.display, name="admin_home"),
    
    # model_1

    path('admin_manage_course', views.vince1, name="index1"),
    
    path('add1', views.add1, name='add1'),
        
    path('update1/<str:id>', views.update1, name='update1'),
    
    path('delete1/<str:id>', views.delete1, name='delete1'),
    
    # model_2
    
    path('admin_manage_student', views.vince2, name="index2"),
    
    path('add2', views.add2, name='add2'),
        
    path('update2/<str:id>', views.update2, name='update2'),
    
    path('delete2/<str:id>', views.delete2, name='delete2'),
    

]