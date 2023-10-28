from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from .forms import SearchForm
from time import sleep
from django.http import Http404
from .serializers import *
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from rest_framework.status import *
from rest_framework import generics



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



class NotificationApiView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    
class NotificationUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    
    
class CircularApiView(generics.ListCreateAPIView):
    queryset = Circular.objects.all()
    serializer_class = CircularSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CircularUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Circular.objects.all()
    serializer_class = CircularSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
