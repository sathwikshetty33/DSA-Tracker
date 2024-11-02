from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model


class teacher(models.Model):
    teacher=models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)

class progress( models.Model):
    username= models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    takentime=models.CharField(max_length=20)
    date = models.DateField()
    submittime = models.CharField(max_length=20)
    easy=models.IntegerField()
    medium=models.IntegerField()
    hard=models.IntegerField()
    def __str__(self):
        return f"{self.username} "

class rooms(models.Model):
    roomid=models.CharField(max_length=20,primary_key=True)
    teacherid=models.ForeignKey(User, on_delete=models.CASCADE)
    roomname=models.CharField(max_length=20,default='class')
    students = models.ManyToManyField(User, through='studying', related_name='studying_rooms')
    description=models.TextField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f"{self.roomid}"
class studying(models.Model):
    student=models.ForeignKey( User, on_delete=models.CASCADE)
    room=models.ForeignKey( rooms, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.student} - {self.room}"
