from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.getchat),
    path('getusers/',views.getusers),
    path('insertchat/',views.insertchat)
]
