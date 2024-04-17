from rest_framework import serializers
from .models import Event,NewsLettre,Ticket

class EventSerializer(serializers.ModelSerializer):
    enrolled_users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'number', 'image', 'enrolled_users']

        

class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLettre
        fields = ['id','author','image','content','created_time']
        extra_kwargs = {
            'author' : {'required': False },
        }

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id','student','Event']
