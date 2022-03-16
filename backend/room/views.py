from django.shortcuts import render
from .models import Room
from hostel.models import Hostel
from django.http import JsonResponse

def add_room(request):
    if request.method == "POST":
        proceed = True
        checkhostel = Hostel.objects.filter(hostel_name=request.POST['hostel_name'])
        if checkhostel:
            proceed = False
            return JsonResponse({'HostelError':request.POST['hostel_name']+' is not a registered hostel'})
        checkroom = Room.objects.filter(hostel__hostel_name=request.POST['hostel_name'],room_number=request.POST['room_number'])
        if checkroom:
            proceed = False
            return JsonResponse({'RoomError':'Room already exists'})
        if proceed:
            room = Room()
            room.hostel = Hostel.objects.get(hostel_name=request.POST['hostel_name'])
            room.room_number = request.POST['room_number']
            room.room_price = request.POST['room_price']
            room.max_occupants = request.POST['max_occupants']
            room.save()
            return JsonResponse({'success':'Room added succesfully'})


def remove_room(request):
    if request.method == "POST":
        proceed = True
        checkhostel = Hostel.objects.filter(hostel_name=request.POST['hostel_name'])
        if checkhostel:
            proceed = False
            return JsonResponse({'HostelError':request.POST['hostel_name']+' is not a registered hostel'})
        checkroom = Room.objects.filter(hostel__hostel_name=request.POST['hostel_name'],room_number=request.POST['room_number'])
        if not checkroom:
            proceed = False
            return JsonResponse({'RoomError':'Room does not exist'})
        if proceed:
            room = Room.objects.get(hostel__hostel_name=request.POST['hostel_name'],room_number=request.POST['room_number'])
            room.delete()
            return JsonResponse({'success':'Room removed succesfully'})