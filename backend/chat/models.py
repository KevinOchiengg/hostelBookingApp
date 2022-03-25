from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admins')
    sender = models.CharField(max_length=50, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    time_sent = models.TimeField(default=timezone.localtime)
    date_sent = models.DateField(default=timezone.localdate)

    def __str__(self):
        return self.sender
    
