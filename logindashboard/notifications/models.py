from django.db import models
from accounts.models import Account


class Notification(models.Model):
    recipient = models.ForeignKey(Account, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
