from django.db import models

# Create your models here.
class emp_info(models.Model):
    choice = [['Male','MALE'],['Female','FEMALE']]
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=50,choices=choice)
    pic=models.ImageField(upload_to='profile/')
    age = models.IntegerField()
    phone_number = models.BigIntegerField()
