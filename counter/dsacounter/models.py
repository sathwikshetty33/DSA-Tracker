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
    score=models.FloatField(blank=True,null=True)
    def calculate_score(self):
        # Example score calculation formula, adjust as needed
        easy_weight = 1
        medium_weight = 2
        hard_weight = 3

        # Convert takentime from HH:MM:SS to seconds
        h, m, s = map(int, self.takentime.split(":"))
        time_in_seconds = h * 3600 + m * 60 + s
        if time_in_seconds == 0:
            return 0  # Avoid division by zero

        # Calculate score (example formula)
        question_score = (self.easy * easy_weight +
                          self.medium * medium_weight +
                          self.hard * hard_weight)
        score = question_score / time_in_seconds
        return round(score, 2)  # Rounded to 2 decimal places

    def save(self, *args, **kwargs):
        # Update score before saving
        self.score = self.calculate_score()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username}"


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
