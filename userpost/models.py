from django.db import models
from django.conf import settings
# Create your models here.
class UserPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField()
#python manage.py startapp userpost
#python manage.py makemigrations
# python manage.py migrate

#createsuperuser
#1st user : maru12/1234

#2nd user : iu516/1234

class Album(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    desc = models.CharField(max_length=100)

class Files(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    myfile = models.FileField(blank=False, null=False,upload_to='files')
    desc = models.CharField(max_length=100)