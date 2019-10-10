from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import UserSerializer,QuestionSerializer,ContestSerializer,ParticipantSerializer
from django.contrib.auth import get_user_model
from .models import Question,Contest,Participant
from django.db.models import Q
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
        query=self.request.query_params.get('q',None)
        if query!=None:
            return get_user_model().objects.filter(Q(username__icontains=query)|Q(first_name__icontains=query))
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
        q=self.request.query_params.get('q','all')
        if q=='upcoming':
            return Contest.objects.filter(is_finished=False)
        elif q=='finished':
            return Contest.objects.filter(is_finished=True)
        return Contest.objects.all()

class ContestDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ContestSerializer

    def get_queryset(self):
        return Contest.objects.all()

    def get_object(self):
        return Contest.objects.get(id=self.kwargs['id'])

class ContestParticipantsAPIView(generics.ListAPIView):
    serializer_class=ParticipantSerializer

    def get_queryset(self):
        contest_id=self.kwargs['contest_id']
        return Participant.objects.filter(contest=contest_id).order_by('score')

class UserAsParticipantsAPIView(generics.ListAPIView):
    serializer_class=ParticipantSerializer

    def get_queryset(self):
        username=self.kwargs['username']
        return Participant.objects.filter(user__username=username)

from rest_framework.views import APIView
from rest_framework.response import Response
class RegisterForContestAPIView(APIView):
    def post(self,request,*args,**kwargs):
        c_id=self.kwargs['contest_id']
        u_username=self.kwargs['user_username']
        contest=Contest.objects.get(id=c_id)
        user=get_user_model().objects.get(username=u_username)
        p=Participant.objects.create(contest=contest,user=user,intital_rating=user.rating)
        return Response({})
