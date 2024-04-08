"""solution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from tech.views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView 
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tech1/',tech1),
    path('javascript5/',javascript5),
    path('jquery/',jquery),
    path('About/',About),
    path('service/',service),
    path('reg/',reg), 
    path('test/',test), 
     path('slider/',slider),
     path('form/',form),
     path('ourteam/',ourteam),
     path('pricing/',pricing),
     path('faq/',faqs),
     
     path('apply/',apply,name='apply'),
     path('counter/',counter),
     path('home/',house,name='home'),
     path('business/',partner,name='business'),
     path('techblog/',techblog),
     path('blogdetail/<int:id>',blogdetail),
     path('car1/',bike,name='car1'),
     
     path('register/',register,name='register'),
     path('new1/',new1),
    
     path('showmp/',showmp),
     path('fill/',fill,name='fill'),
     path('b/<int:id>',b),
     path('accounts/',include('django.contrib.auth.urls')),
     path('paytm/',include('paytm.urls')),
     path('login1/',LoginView.as_view(),name='login1'),
     path('logout1/',LogoutView.as_view(),name='logout'),
     path('log/',log),   

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
