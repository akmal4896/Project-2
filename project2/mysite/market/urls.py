"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path, include
from django.views.generic import ListView, DetailView
from .views import ItemCreateView
from . import views
from market.models import Item

urlpatterns = [
    path('', ListView.as_view(queryset=Item.objects.all().order_by("-date")[:25],
    template_name="market/home.html"), name='homepage'),
    path('<int:pk>', DetailView.as_view(model=Item, template_name="market/item.html"),
         name = 'item-detail'),
    path('item/add/',ItemCreateView.as_view(), name='item-create'),
]
