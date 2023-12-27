from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [


    path('', views.mac, name='jocker'),
    
    path('blog', views.blog, name='blog'),

    path('contact', views.contact, name='contact'),

    path('about', views.about, name='about'),

    path('login', views.login, name='login'),

    path('register', views.register, name='register'),

    path('python', views.python, name='python'),

    path('news-single', views.news_single, name='news-single'),

    path('experence', views.experence, name='experence'),

    path('fplace', views.fplace, name='fplace'),

    path('eplace', views.eplace, name='eplace'),

    path('tens', views.tens, name='tens'),

    path('campus', views.campus, name='campus'),

    path('clients', views.clients, name='clients'),

    path('display_app2_data/', views.display_data_from_app2, name='display_app2_data'),

    path('all_courses', views.display_data_from_app2, name='all_courses'),




]