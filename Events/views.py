
from django.shortcuts import render
from .models import Events
from user.models import Users
from Events.serializers import EventsSerializer
from user.serializers import UsersSerializer
from rest_framework import permissions, status
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from EventsHistory.serilazers import EventsHistorySerializer
from EventsHistory.models import EventsHistory


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def events_list(request):
    if request.method == 'GET':
        events = Events.objects.all()
        serializer = EventsSerializer(events, many=True)
        return Response(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = EventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST', 'DELETE', 'PUT', 'COPY'])
@permission_classes((permissions.AllowAny,))
def delete_event(request, pk):
    if request.method == 'DELETE':
        events = Events.objects.filter(id=pk)
        events.delete()
        return JsonResponse({}, status=200)
    elif request.method == 'PUT':
        events = Events.objects.get(id=pk)
        serializer = EventsSerializer(events, many=False)
        serializer.update(serializer.instance, request.data)
        return JsonResponse({}, status=200)
    elif request.method == 'GET':
        events = Events.objects.filter(id=pk)
        serializer = EventsSerializer(events, many=True)
        users = Users.objects.filter(id=events.members)
        serializeru = UsersSerializer(users, many=True)
        return Response({"event": serializer.data, "users": serializeru.data})
    elif request.method == 'POST':
        Request = EventsHistory(userId=Users.objects.get(id=1), eventId=Events.objects.get(id=pk))
        Request.save()
        return Response({}, status=200)
    elif request.method == 'COPY': # OPTIONAL
        requests = EventsHistory.objects.all()
        serializer = EventsHistorySerializer(requests, many=True)
        return JsonResponse(serializer.data, safe=False)
