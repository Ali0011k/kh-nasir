from django.shortcuts import render
from .models import *
from django.http import Http404
from .serializers import *
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.exceptions import ParseError



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
        
        
@api_view(['GET' , 'PUT' , 'DELETE'])
@permission_classes([IsAuthenticated , IsAdminUser])
def work_update(request):
    if request.GET.get('id'):
        try:
        
            id = request.GET.get('id')
            work = Works.objects.get(id = id)

        except Works.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = WorksSerializer(instance=work)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = WorksSerializer(instance=work, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


        elif request.method == 'DELETE':
            work.delete()
            return Response(status=HTTP_204_NO_CONTENT)
    else:
        raise ParseError('you should send an id with your query parametrs' , code=HTTP_400_BAD_REQUEST)