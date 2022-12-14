"""buse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from bdata import views
from user.views import signup,login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', views.home, name='home'),
    path('find/', views.find, name="find"),
    path('search/', views.find, name="search"),
    path('bus/<int:bus_id>/<int:bpoint>', views.bus, name="bus_details"),
    path('updateloc', views.loc, name="updateloc"),
    path('our_team',views.ot,name='our_team'),
    path('signup',signup,name='signup/'),
    path('login/',login,name='/login')
    
   
]
