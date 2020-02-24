"""plot_for_sale URL Configuration

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
from django.conf.urls.static import static
from django.urls import path

from app1 import views
from plot_for_sale import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',views.Showmain),
    path('loginadmin/',views.AdminSuccess),
    path('addplot/',views.Addplot),
    path('saveplot/',views.Saveplot),
    path('editplot/',views.editplot),
    path('serchplot/',views.Searchplot),
    path('updateplot/',views.updateplot),
    path('viewplot/',views.viewallplot),
    path('Addnewapt/',views.addaptmpt),
    path('saveaptmpt/',views.saveaptmpt),
    path('viewallapt/',views.viewallapt),
    path('editapt/',views.editaptmpt),
    path('serchaptmpt/',views.searchaptmpt),
    path('updateatmpt/',views.updateatmpt),
    path('about/',views.about),
    path('addemployee/',views.Addemployee),
    path('savemployee/',views.Saveemployee),
    path('viewemployee/',views.viewemployee)
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


