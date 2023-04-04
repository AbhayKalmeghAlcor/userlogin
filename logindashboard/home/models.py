from django.db import models
import uuid


# Create your models here.
class Post(models.Model):
    point = models.IntegerField(default=10)
    recipients = models.CharField(max_length=100, null=False)
    hashtags = models.CharField(max_length=150, null=True)
    comments = models.TextField(null=True)
    image = models.ImageField(upload_to='photos/user_form', null=True, max_length=255)

    def __str__(self):
        return "%s %s %s %s" % (self.point, self.recipients, self.image, self.comments)
