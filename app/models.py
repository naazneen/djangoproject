from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    manager = models.ForeignKey(User,on_delete = models.CASCADE,default = None)
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    email = models.EmailField()
    gender = models.CharField(max_length = 20,choices = (('male','MALE'),('female','FEMALE'),('other','OTHER')))
    date_added = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return self.firstname
    
    