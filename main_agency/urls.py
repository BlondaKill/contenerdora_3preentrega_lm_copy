"""
URL configuration for main_agency project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from agency.views import *
# from agency.views import listar_model_girl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Laura', create_static),
    path('list', listar_main_agency),
    # path('model_girl/', listar_model_girl),
    path('create-girl/', create_model_girl, name='create_model_girl'),
    path('list-girl/', list_model_girl, name='list_model_girl'),
    path('search-girl/', search_model_girl, name='search_model_girl'),
    # path Brand
    path('create-brand/', create_brand, name='create_brand'),
    path('list-brand/', list_brand, name='list_brand'),
    path('search-brand/', search_brand, name='search_brand'),
    # path Client
    path('create-client/', create_client, name='create_client'),
    path('list-client/', list_client, name='list_client'),
    path('search-client/', search_client, name='search_client'),
]
