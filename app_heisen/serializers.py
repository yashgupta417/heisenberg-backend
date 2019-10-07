from .models import User,Question,Contest,Participant
from rest_framework import serializers
from django.contrib.auth import get_user_model



class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model=get_user_model()
        fields='__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta():
        model=Question
        fields='__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta():
        model=Participant
        fields='__all__'
        depth=1

class ContestSerializer(serializers.ModelSerializer):
    #participants=ParticipantSerializer(many=True,read_only=True)

    class Meta():
        model=Contest
        fields='__all__'
        depth=1
