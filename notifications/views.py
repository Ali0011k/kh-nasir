from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from .forms import SearchForm
from time import sleep
from django.http import Http404
from .serializers import *
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.status import *


def notifications(request):
    all_notifications = Notification.objects.filter(status = 'p').order_by('-create_time')
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            all_notifications = Notification.objects.filter(status = 'p').filter(title__icontains = cd['title']).order_by('-create_time')
            if all_notifications is not None and len(all_notifications) >= 1:
                return render(request,'notifications/notifications_searched.html',{'notifications':all_notifications})
            else:
                
                sleep(1)
                return Http404('محتوای مورد نظر یافت نشد')
    else:
        form = SearchForm()
    return render(request,'notifications/notifications.html',{'notifications':all_notifications})


def notification_detail(request):
    
    pk = request.GET.get('pk')
    
    notification_detail = get_object_or_404(Notification,pk = pk)

    ip_address =  request.user.ip_address
    if ip_address not in notification_detail.hits.all():
        notification_detail.hits.add(ip_address)

    return render(request,'notifications/notification_detail.html',{'notification':notification_detail})





@api_view(['GET' , 'POST'])
@permission_classes([IsAuthenticated , IsAdminUser])
def Notification_serializer(request):
    
    if request.method == "GET":
        try:
            content = Notification.objects.all()
        except Notification.DoesNotExist:
            return Response({
                'error':'the content does not exist'
            } ,status=HTTP_404_NOT_FOUND)
        serializer = NotificationSerializer(content , many = True)

        return Response(serializer.data)
    elif request.method == "POST":
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)


@api_view(['GET' , 'PUT' , 'DELETE'])
@permission_classes([IsAuthenticated , IsAdminUser])
def Notification_update(request):
    if request.GET.get('id'):
        try:
        
            id = request.GET.get('id')
            notification = Notification.objects.get(id = id)

        except Notification.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = NotificationSerializer(instance=notification)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = NotificationSerializer(instance=notification, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


        elif request.method == 'DELETE':
            notification.delete()
            return Response(status=HTTP_204_NO_CONTENT)
    else:
        raise ParseError('you should send an id with your query parametrs' , code=HTTP_400_BAD_REQUEST)



@api_view(['GET' , 'POST'])
@permission_classes([IsAuthenticated , IsAdminUser])
def Circular_serializer(request):
    
    if request.method == "GET":
        try:
            content = Circular.objects.all()
        except Circular.DoesNotExist:
            return Response({
                'error':'the content does not exist'
            } ,status=HTTP_404_NOT_FOUND)
        serializer = CircularSerializer(content , many = True)

        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CircularSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        
@api_view(['GET' , 'PUT' , 'DELETE'])
@permission_classes([IsAuthenticated , IsAdminUser])
def Circular_update(request):
    if request.GET.get('id'):
        try:
        
            id = request.GET.get('id')
            circular = Circular.objects.get(id = id)

        except Circular.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CircularSerializer(instance=circular)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = CircularSerializer(instance=circular, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


        elif request.method == 'DELETE':
            circular.delete()
            return Response(status=HTTP_204_NO_CONTENT)
    else:
        raise ParseError('you should send an id with your query parametrs' , code=HTTP_400_BAD_REQUEST)

