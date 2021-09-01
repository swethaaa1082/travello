from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
class blog(models.Model):
    day=models.IntegerField()
    month=models.CharField(max_length=20)
    name=models.CharField(max_length=250)
    desc=models.TextField()
    image=models.ImageField(upload_to='images')