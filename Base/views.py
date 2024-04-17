from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import EventSerializer,NewsLetterSerializer,TicketSerializer
from .models import Event,NewsLettre,Ticket,Student,Prof
from rest_framework import status
from django.contrib.auth.models import User
from .decorators import group_required

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@group_required(group_name='Admin')
def Create_Event(request):
    data = request.data
    serializer = EventSerializer(data=data)
    if serializer.is_valid():
        Event.objects.create(
            title = data['title'],
            description = data['description'],
            number = data['number'],
            image = data['image'],
        )
        return Response({'info':'created succesfully','ser':serializer.data},status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Enroll_Event(request,pk):
    event = get_object_or_404(Event,pk=pk)
    if request.user in event.enrolled_users.all() :
        return Response({'info':'user already exists'},status=status.HTTP_400_BAD_REQUEST)
    else:
        event.enrolled_users.add(request.user)
        event.number = event.number - 1
        event.save()
        Ticket.objects.create(
            student = request.user,
            Event = event,
        )
        return Response({"info":"created succesfully"},status=status.HTTP_201_CREATED)
    

    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Get_Student_Tickets(request):
    student = get_object_or_404(User, username=request.user)
    tickets = Ticket.objects.filter(student=student)
    serializer = TicketSerializer(tickets, many=True)
    data = serializer.data
    for ticket_data in data:
        event_id = ticket_data.pop('Event')  # Remove the Event ID from the response
        event_name = Event.objects.get(pk=event_id).title  # Get the name of the event
        ticket_data['event_name'] = event_name  # Add event_name to the response
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@group_required(group_name='Prof')
def Create_newsletter(request):
    data = request.data
    serializer = NewsLetterSerializer(data=data)
    if serializer.is_valid():
        NewsLettre.objects.create(
            author = request.user,
            content = data['content'],
            image = data['image']
        )
        return Response({"info":"news good"},status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@group_required(group_name='Prof')
def Get_Prof_NewsLetters(request):
    news = NewsLettre.objects.filter(author=request.user)
    serializer = NewsLetterSerializer(news, many=True)
    for item in serializer.data:
        author_id = item.pop('author')  
        author_name = request.user.username if author_id == request.user.id else None
        item['author'] = author_name  

    return Response(serializer.data)

@api_view(['GET'])
def get_all_newslettres(request):
    news = NewsLettre.objects.all()
    serializer = NewsLetterSerializer(news, many=True)
    for item in serializer.data:
        author_id = item['author']
        author_name = User.objects.get(pk=author_id).username
        item['author'] = author_name
    return Response(serializer.data)
