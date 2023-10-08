from django.shortcuts import render
from .models import *
from django.http import Http404
from .serializers import *
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import *



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
    
@api_view(['GET' , 'POST'])
@permission_classes([IsAuthenticated , IsAdminUser])
def Works_serializer(request):
    
    if request.method == "GET":
        try:
            content = Works.objects.all()
        except Works.DoesNotExist:
            return Response({
                'error':'the content does not exist'
            } ,status=HTTP_404_NOT_FOUND)
        serializer = WorksSerializer(content , many = True)

        return Response(serializer.data)
    elif request.method == "POST":
        serializer = WorksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)