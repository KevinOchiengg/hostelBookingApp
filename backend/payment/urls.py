from django.urls import path,include
from . import views

urlpatterns = [  
    path('', view=views.payment_view, name='payment'),   
]
