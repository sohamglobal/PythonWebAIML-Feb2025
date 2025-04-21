"""
URL configuration for fitnessai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fitness/',views.index,name="index"),
    path('login/',views.login),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addprofile/',views.addprofile,name="addprofile"),
    path('storeprofile/',views.storeprofile),
    path('changeprofile/',views.change),
    path('editprofile/',views.edit),
    path('deleteprofile/',views.delete),
    path('logout/',views.logout),
    path('report/',views.report),
    path('search/',views.search),
    path('searchprofiles/',views.searchprofiles),
    path('tips/',views.tips),
]
