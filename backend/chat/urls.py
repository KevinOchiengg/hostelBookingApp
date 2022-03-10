from django.urls import path 

urlpatterns = [
    path('',views.getchat),
    path('getusers/',views.getusers),
    path('insertchat/',views.insertchat)
]
