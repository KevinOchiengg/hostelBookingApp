from django.contrib.auth import get_user_model
from .models import Chat
from django.http import JsonResponse

User = get_user_model()

def getchat(request):
    if request.user.is_staff:
        chats = Chat.objects.filter(admin__email=request.user.email)
        data = list(chats.values())
        return JsonResponse(data,safe=False)
    elif not request.user.is_staff:
        user_email = request.user.email
        admin_email = request.GET['admin_email']


def getusers(request):
    if request.user.is_staff:
        admin_email = request.user.email
        user_email = request.GET['user_email']
        data = []
        users = User.objects.filter(is_staff=False)
        for user in users:
            user_email = user.email
            chat = Chat.objects.filter(user__email=user_email,admin__email=admin_email)
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

