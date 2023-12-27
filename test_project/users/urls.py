from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('records', views.vince, name="index"),
    
    path('add', views.add, name='add'),
        
    path('update/<str:id>', views.update, name='update'),
    
    path('delete/<str:id>', views.delete, name='delete'),
    
    path('dashbord', views.index, name='dashbord'),

    path('chartjs', views.chart, name='chartjs'),

    path('basic_elements', views.forms, name='basic_elements'),

    path('mdi', views.icons, name='mdi'),

    path('blank-page', views.sample1, name='blank-page'),

    path('error-404', views.sample2, name='error-404'),

    path('error-500', views.sample3, name='error-500'),

    path('login', views.sample4, name='login'),

    path('register', views.sample5, name='register'),

    path('basic-table', views.table, name='basic-table'),

    path('buttons', views.ui1, name='buttons'),

    path('typography', views.ui2, name='typography'),



    
]