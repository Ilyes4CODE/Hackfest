from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/',null=True,default='image.jpg')
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    univ_number = models.CharField(max_length=150)
    study_year = models.CharField(max_length=150)
    speciality = models.CharField(max_length=150)
    Group = models.CharField(max_length=150)
    expired_token = models.CharField(max_length=150)

    def __str__(self):
        return self.first_name

class Prof(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/',null=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    prof_number = models.CharField(max_length=150)
    expired_token = models.CharField(max_length=150)

    def __str__(self):
        return self.first_name


class NewsLettre(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/',null=True)
    content = models.CharField(max_length=150)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.author.username} at {self.created_time}"
    
class Event(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='event_place/',null=True)
    description = models.CharField(max_length=150)
    number = models.IntegerField(null=True)
    enrolled_users = models.ManyToManyField(User)

    def __str__(self):
        return self.title
    
class Ticket(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    Event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.student.username
    

