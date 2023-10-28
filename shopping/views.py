from django.shortcuts import render
from .models import *
from django.http import Http404
from .serializers import *
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from rest_framework.status import *
from rest_framework.exceptions import ParseError
from rest_framework import generics


def works_detail(request):
    pk = request.GET.get('pk')
    try:
            works = Works.objects.get(pk = pk , status = 'p')
    except Works.DoesNotExist:
        raise Http404('در حال حاظر چنین نمونه کاری وجود ندارد یا در حالت به روزرسانی میباشد')
    
    return render(request , 'work_detail.html' , {
        'work' : works
    })


def works(request):
    try:
        works = Works.objects.filter(status = 'p')
    except Works.DoesNotExist:
        raise Http404('در حال حاظر چنین نمونه کاری وجود ندارد یا در حالت به روزرسانی میباشد')
    return render(request , 'work_list.html' , {
        'works':works
    })
    
    

class WorkApiView(generics.ListCreateAPIView):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    
class WorkUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
