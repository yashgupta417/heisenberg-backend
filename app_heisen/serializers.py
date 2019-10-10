from .models import User,Question,Contest,Participant
from rest_framework import serializers
from django.contrib.auth import get_user_model



class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model=get_user_model()
        fields='__all__'

class QuestionMiniSerializer(serializers.ModelSerializer):
    class Meta():
        model=Question
        exclude=['solved_by']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta():
        model=Question
        fields='__all__'
        depth=1

class ContestMiniSerializer(serializers.ModelSerializer):
    class Meta():
        model=Contest
        exclude=['questions']

class ParticipantSerializer(serializers.ModelSerializer):
    contest=ContestMiniSerializer(read_only=True)
    class Meta():
        model=Participant
        fields='__all__'
        depth=1

class ContestSerializer(serializers.ModelSerializer):
    #participants=ParticipantSerializer(many=True,read_only=True)
    questions=QuestionMiniSerializer(many=True,read_only=True)
    class Meta():
        model=Contest
        fields='__all__'
        depth=1
