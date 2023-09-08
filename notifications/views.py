from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from .forms import SearchForm
from time import sleep
from django.http import Http404
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *


def notifications(request):
    all_notifications = Notification.objects.filter(status = 'p').order_by('-create_time')
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            all_notifications = Notification.objects.all().filter(title__icontains = cd['title']).order_by('-create_time')
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


@api_view(['GET' , 'POST'])
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
        

