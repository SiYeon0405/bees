from django.urls import path

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('api/', include('group_join.group_joinurls')), 
]