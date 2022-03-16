from django.urls import path
from . import views

urlpatterns = [
    path('AddRoom/',views.add_room),
    path('RemoveRoom/',views.remove_room)
]

