from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    username=models.CharField(primary_key=True,max_length=255,blank=False,null=False)
    image=models.ImageField(upload_to="images/",blank=True,null=True)
    is_online=models.BooleanField(default=False)
    rating=models.IntegerField(default=1000)
    max_rating=models.IntegerField(default=1000)
    def __str__(self):
        return self.username

class Question(models.Model):
    problem_name=models.CharField(max_length=100,blank=False)
    problem=models.TextField()
    answer=models.TextField()
    solution=models.TextField()
    difficulty=models.CharField(default='A',max_length=10,blank=True)
    points=models.IntegerField(default=1000)
    is_available_for_practice=models.BooleanField(default=False)
    contest=models.ForeignKey('Contest',related_name='questions',on_delete=models.CASCADE,default=None,null=True)
    solved_by=models.ManyToManyField('Participant',related_name='questions_solved')
    solved_by_count=models.IntegerField(default=0)
    def __str__(self):
        return self.problem_name

#learn to schedule a task
class Contest(models.Model):
    name=models.CharField(max_length=100,blank=False)
    end_time=models.TimeField(null=True)
    end_date=models.DateField(null=True)
    starting_time=models.TimeField(null=True)
    starting_date=models.DateField(null=True)
    #questions=models.ManyToManyField(Question)
    no_of_questions=models.IntegerField()
    is_finished=models.BooleanField(default=False)
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
    questions_solved_count=models.IntegerField(default=0)
    def __str__(self):
        return self.user.username
