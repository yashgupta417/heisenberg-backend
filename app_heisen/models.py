from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    image=models.ImageField(upload_to="images/",blank=True,null=True)
    is_online=models.BooleanField(default=False)
    rating=models.IntegerField(default=1000)
    def __str__(self):
        return self.username

class Question(models.Model):
    problem_name=models.CharField(max_length=100,blank=False)
    problem=models.TextField()
    answer=models.TextField()
    solution=models.TextField()
    def __str__(self):
        return self.problem_name

#learn to schedule a task
class Contest(models.Model):
    name=models.CharField(max_length=100,blank=False)
    length=models.TimeField()
    starting_time=models.TimeField()
    date=models.DateField(blank=True,null=True)
    questions=models.ManyToManyField(Question)
    no_of_questions=models.IntegerField()

    def __str__(self):
        return self.name

class Participant(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='as_participant',on_delete=models.CASCADE)
    contest=models.ForeignKey(Contest,related_name='participants',on_delete=models.CASCADE)
    intital_rating=models.IntegerField()
    rating_change=models.IntegerField(default=0)
    score=models.IntegerField(default=0)
    rank=models.IntegerField(default=0)
    final_rating=models.IntegerField(default=0)
    def __str__(self):
        return self.user.username