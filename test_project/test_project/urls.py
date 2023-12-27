from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('website.urls')),

    path('student_login/', include('student_login.urls')),
    
    path('admin_login/', include('admin_login.urls')),
    
    path('users/', include('users.urls')),

    

    
]
