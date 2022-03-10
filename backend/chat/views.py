from django.contrib.auth import get_user_model
from .models import Chat
from django.http import JsonResponse

User = get_user_model()

def getchat(request):
    if request.user.is_staff:
        data = Chat.objects.filter(admin__email=request.user.email,user__email=request.GET['user_email'])
        chats = list(.values())
        return JsonResponse(chats,safe=False)
    elif not request.user.is_staff:
        data = Chat.objects.filter(user__email=request.user.email,admin__email=request.GET['admin_email'])
        chats = list(data.values())
        return JsonResponse(chats,safe=False)


def getusers(request):
    if request.user.is_staff:
        data = []
        users = User.objects.filter(staff=False)
        for user in users:
            user_email = user.email
            chat = Chat.objects.filter(user__email=user_email,admin__email=request.user.email)
            if chat:
                data.append(chat.values()[0])
        print(data)
        return  JsonResponse(data,safe=False) 
    elif not request.user.is_staff::
        data = []
        users = User.objects.filter(staff=True)
        for user in users:
            user_email = user.email
            chat = Chat.objects.filter(user__email=user_email,admin__email=request.user.email)
            if chat:
                data.append(chat.values()[0])
        print(data)
        return  JsonResponse(data,safe=False) 


def insertchat(request):
    if request.user.is_staff:
        chat = Chat()
        chat.user = User.objects.get(email=request.GET['user_email'])
        chat.admin = User.objects.get(email=request.user.email)
        chat.sender = "admin"
        chat.save()
    elif not request.user.is_staff:
        chat = Chat()
        chat.user = User.objects.get(email=request.user.email)
        chat.admin = User.objects.get(email=request.GET['admin_email'])
        chat.sender = "user"
        chat.save()

