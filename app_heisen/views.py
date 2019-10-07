from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import UserSerializer,QuestionSerializer,ContestSerializer,ParticipantSerializer
from django.contrib.auth import get_user_model
from .models import Question,Contest,Participant
# Create your views here.
def IndexView(request):
    return HttpResponse("HeisenBerg.")

class SignupAPIView(generics.CreateAPIView):
    serializer_class=UserSerializer
    def get_queryset(self):
        return get_user_model().objects.all()

class UserListAPIView(generics.ListAPIView):
    serializer_class=UserSerializer
    def get_queryset(self):
        return get_user_model().objects.all()

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=UserSerializer

    def get_queryset(self):
        return get_user_model().objects.all()

    def get_object(self):
        return get_user_model().objects.get(username=self.kwargs['username'])

class QuestionListAPIView(generics.ListCreateAPIView):
    serializer_class=QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()

class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()

    def get_object(self):
        return Question.objects.get(id=self.kwargs['id'])

class ContestListAPIView(generics.ListCreateAPIView):
    serializer_class=ContestSerializer

    def get_queryset(self):
        return Contest.objects.all()

class ContestDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ContestSerializer

    def get_queryset(self):
        return Contest.objects.all()

    def get_object(self):
        return Contest.objects.get(id=self.kwargs['id'])

class ParticipantListAPIView(generics.ListCreateAPIView):
    serializer_class=ParticipantSerializer

    def get_queryset(self):
        contest_id=self.kwargs['contest_id']
        return Participant.objects.filter(contest=contest_id)
