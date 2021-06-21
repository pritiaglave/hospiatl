"""new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', About,name='about'),
    path('home/', Home,name='home'),
    path('admin_login/', Login,name='login'),
    path('logout/', Logout_admin,name='logout'),
    path('contact/', views.Contact),
    path('facilities/', views.Facilities),
    path('view_doctor/', views.view_doctor),
    path('update_doctor/<int:id>', views.update_doctor),
    path('delete_doctor/<int:id>', views.delete_doctor),
    path('insert_doctor/', views.insert_doctor),
    path('insert_patient/', views.insert_patient),
    path('view_patient/', views.view_patient),
    path('update_patient/<int:id>', views.update_patient),
    path('delete_patient/<int:id>', views.delete_patient),
    path('insert_appoinment/', views.insert_appoinment),
    path('view_appoinment/', views.view_appoinment),
    path('delete_appoinment/<int:id>', views.delete_appoinment),
    path('dumy/', views.dumy),
]
