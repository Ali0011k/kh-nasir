from typing import Any, Optional
from django.db import models
from django.shortcuts import render,redirect, get_object_or_404
from .forms import LoginForm  ,SignUpForm , ResetForm ,edit_userForm
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib import messages
from .mixins import *
from notifications.models import Notification , Circular
from shopping.models import Works
from pictures.models import *
from gallery.models import Works_Images , Circular_Images
from courses.models import Faq , Handout
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import *
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.status import *
from django.utils.translation import gettext as _
from time import sleep




def home(request):
    slider_pictures = HomePictures.objects.all()
    recent_notifications = Notification.objects.all().order_by('-create_time')[:3]
    recent_works = Works.objects.all().order_by('-create_time')[:3]
    home_info = HomeInfo.objects.first()
    return render(request,'users/home.html',{
        'slider_pictures':slider_pictures , 
        'recent_notifications'  :recent_notifications,
        'recent_works': recent_works,
        'home_info' : home_info
    })




def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username = cd['username'],password = cd['password'])
            if user is not None:
                if user.is_active:
                    auth_login(request,user)
                    for i in User.objects.filter(username = cd['username']):                
                        if i == user:
                            log_user = i
                        request.session['name'] = log_user.username
                        request.session['email'] = log_user.email
                        request.session['password'] = log_user.password
                        if log_user.is_staff == True or log_user.is_superuser == True:
                            return redirect('/User/Update/{}'.format(request.user.pk))
                        else:
                            return redirect('/auth/user/user_info/')
            else:
                message = messages.error(request, "نام کاربری یا رمز عبور نامعتبر است")
                return render(request,'users/login.html',{'message':message})

                
        else:
            form = LoginForm()
    else:
        form = LoginForm()
    return render(request,'users/login.html')




@login_required(login_url='/login/',redirect_field_name="/login/")
def user_information(request):
    name = request.session.get('name')
    email = request.session.get('email')
    if name == None :
        return redirect('/login/')
    return render(request,'users/user_informations.html',{
        'name':name,
        'email':email,
    })
    


class edit_info(LoginRequiredMixin, UpdateView):
    model = User
    success_url = '/login/'
    template_name = "users/edit_info.html"
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
    ]





@login_required(login_url='/login/')
def admin(request):
    return render(request,'users/adminlte.html')


# Notifications


class NotificationCreate(NotificationFiedsMixin, CreateView):
    model = Notification
    template_name = "users/notification-create.html"


class NotificationList(ListView, NotificationFiedsMixin):
    model = Notification
    template_name = "users/notification-list.html"

    ordering = ['-create_time']


class NotificationUpdate(NotificationFiedsMixin, UpdateView):
    model = Notification
    template_name = "users/notification-update.html"

class NotificationDelet(NotificationFiedsMixin, DeleteView):
    model = Notification
    success_url = reverse_lazy("users:notification-list")
    template_name = "users/notification_confirm_delete.html"
    
    
# Circulars

    
class CircularCreate(CircularFiedsMixin, CreateView):
    model = Circular
    success_url = reverse_lazy("users:Circular-list")
    template_name = "users/circular-create.html"


class CircularList(ListView, CircularFiedsMixin):
    model = Circular
    template_name = "users/circular-list.html"

    ordering = ['-create_time']


class CircularUpdate(CircularFiedsMixin, UpdateView):
    model = Circular
    success_url = reverse_lazy("users:Circular-list")
    template_name = "users/circular-update.html"

class CircularDelet(CircularFiedsMixin, DeleteView):
    model = Circular
    success_url = reverse_lazy("users:Circular-list")
    template_name = "users/circular_confirm_delete.html"
    

# Works

class WorksCreate(WorksFiedsMixin, CreateView):
    model = Works
    success_url = reverse_lazy("users:Works-list")
    template_name = "users/Works-create.html"


class WorksList(ListView, WorksFiedsMixin):
    model = Works
    template_name = "users/Works-list.html"




class WorksUpdate(WorksFiedsMixin, UpdateView):
    model = Works
    success_url = reverse_lazy("users:Works-list")
    template_name = "users/Works-update.html"

class WorksDelet(WorksFiedsMixin, DeleteView):
    model = Works
    success_url = reverse_lazy("users:Works-list")
    template_name = "users/Works_confirm_delete.html"
    


# Users


class UserCreate(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('users:User-list')
    template_name = 'users/User-create.html'


class UserList(ListView, UserFiedsMixin):
    model = User
    template_name = "users/User-list.html"




class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy("users:User-list")
    template_name = "users/User-update.html"
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_superuser'
    ]


    def get_object(self , queryset = None):
        if  self.request.user.is_superuser:
            user = get_object_or_404(User , pk = self.kwargs['pk'])
        else:
            user = self.request.user
        return user




class UserDelet(UserFiedsMixin, DeleteView):
    model = User
    success_url = reverse_lazy("users:User-list")
    template_name = "users/User_confirm_delete.html"
    
    
def validate_new_password(new_password):
    try:
        validate_password(new_password)
        return True  
    except ValidationError as e:
        return False
    
@login_required(login_url='/login/')
def password_recovery(request ,pk ):
    error_reset = None
    if request.method == 'POST':
        form = ResetForm(request.POST)
        if form.is_valid():
            form_info = form.cleaned_data
            user_info = User.objects.get(pk = pk)
            if form_info['password'] == form_info['password_confrim']:
                if validate_new_password(form_info['password']):
                
                    new_password = form_info['password_confrim']
                    user_info.set_password(new_password)
                    user_info.save()
                    if request.user.pk == user_info.pk:
                        return redirect('/login/')
                    else:
                        return redirect('/password_change/done/')
                else:
                    error_reset = messages.error(request, "رمز عبور نامعتبر است")
            else:
                error_reset = messages.error(request, "رمز های عبور یکسان نیستند")                
                return render(request,'users/password_change.html',{
                'form':form,
                'error_reset':error_reset
                })
    else :
        form = ResetForm()
    return render(request,'users/password_change.html',{
        'form':form,
        })
    

def password_change_done(request):
    return render(request , 'users/password_done.html')
    

    
# Gallery
    
class Work_Image_List(ListView):
    model = Works_Images
    ordering = ['-pk']
    template_name = "users/Work_Images-list.html"
    

class Circular_Images_List(ListView):
    model = Circular_Images
    ordering = ['-pk']
    template_name = "users/Circular_Images-list.html"
    
# faq

class faqlist(ListView):
    model = Faq
    ordering = ['-create_time']
    template_name = "users/faq_list.html"

   
class FaqCreate(FaqFiedsMixin, CreateView):
    model = Faq
    success_url = reverse_lazy("users:faq-list")
    template_name = "users/faq-create.html"
 

class faqUpdate(FaqFiedsMixin, UpdateView):
    model = Faq
    success_url = reverse_lazy("users:faq-list")
    template_name = "users/faq-update.html"

class faqDelet(WorksFiedsMixin, DeleteView):
    model = Faq
    success_url = reverse_lazy("users:faq-list")
    template_name = "users/faq_confirm_delete.html"
    
    
    
# Hnadout

from .forms import *




class HandoutCreate(CreateView):
    model = Handout
    form_class = HandoutForm
    template_name = "users/Handout-create.html"
    success_url = reverse_lazy("users:Handout-list")

    def form_valid(self, form):
        # ابتدا فرم را ذخیره می‌کنیم تا نمونه Handout ایجاد شود
        response = super().form_valid(form)
        
        # ایجاد نمونه‌های File و ذخیره آن‌ها به همراه نمونه Handout مربوطه
        other_files_data = self.request.FILES.getlist('other_files')
        if other_files_data:
            for other_file_data in other_files_data:
                other_file = File(post=self.object)
                other_file.other_files.save(other_file_data.name, other_file_data, save=True)

        return response



class HandoutList(ListView):
    model = Handout
    ordering = ['-create_time']
    template_name = "users/Handout-list.html"

    


class HandoutUpdate(UpdateView):
    
    model = Handout
    form_class = HandoutForm
    template_name = "users/Handout-update.html"
    success_url = reverse_lazy("users:Handout-list")
    context_object_name = 'handout'

    def form_valid(self, form):
        # ابتدا فرم را ذخیره می‌کنیم تا نمونه Handout ایجاد شود
        response = super().form_valid(form)
        
        # ایجاد نمونه‌های File و ذخیره آن‌ها به همراه نمونه Handout مربوطه
        other_files_data = self.request.FILES.getlist('other_files')
        if other_files_data:
            for other_file_data in other_files_data:
                other_file = File(post=self.object)
                other_file.other_files.save(other_file_data.name, other_file_data, save=True)

        return response





class HandoutDelet(HandoutFiedsMixin, DeleteView):
    model = Handout
    success_url = reverse_lazy("users:Handout-list")
    template_name = "users/Handout_confirm_delete.html"






    
@api_view(['GET' , 'POST'])
@permission_classes([IsAuthenticated , IsAdminUser])
def User_serializer(request):
    
    if request.method == "GET":
        try:
            content = User.objects.all()
        except User.DoesNotExist:
            return Response({
                'error':'the content does not exist'
            } ,status=HTTP_404_NOT_FOUND)
        serializer = UserSerializer(content , many = True)

        return Response(serializer.data)
    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        
@api_view(['GET' , 'PUT' , 'DELETE'])
@permission_classes([IsAuthenticated , IsAdminUser])
def user_serializer_update(request):
    if request.GET.get('id'):
        try:
        
            id = request.GET.get('id')
            user = User.objects.get(id = id)

        except Notification.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = UserSerializer(instance=user)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = UserSerializer(instance=user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


        elif request.method == 'DELETE':
            user.delete()
            return Response(status=HTTP_204_NO_CONTENT)
    else:
        raise ParseError('you should send an id with your query parametrs' , code=HTTP_400_BAD_REQUEST)

# SectionChoicese

class SectionChoice_list(ListView):
    model = SectionChoice
    template_name = "users/SectionChoice_list.html"
    
    
class SectionChoice_Delet(SectionChoiceFieldMixin, DeleteView):
    model = SectionChoice
    success_url = reverse_lazy("users:sectionchoice-list")
    template_name = "users/SectionChoice_confirm_delete.html"
    
    
    
    
class picture_list(ListView):
    model = HomePictures
    template_name = "users/picture_list.html"
    
    
class delete_picture(HomePicturesFieldMixin, DeleteView):
    model = HomePictures
    success_url = reverse_lazy("users:picture-list")
    template_name = "users/picture_confirm_delete.html"
    
    
class create_picture(HomePicturesFieldMixin, CreateView):
    model = HomePictures
    success_url = reverse_lazy("users:picture-list")
    template_name = "users/picture-create.html"
    
    
# HomeInfo

class HomeInfoCreate(HomeInfoFiedsMixin, CreateView):
    model = HomeInfo
    success_url = reverse_lazy("users:HomeInfo-list")
    template_name = "users/HomeInfo-create.html"


class HomeInfoList(ListView, HomeInfoFiedsMixin):
    model = HomeInfo
    template_name = "users/HomeInfo-list.html"




class HomeInfoUpdate(HomeInfoFiedsMixin, UpdateView):
    model = HomeInfo
    success_url = reverse_lazy("users:HomeInfo-list")
    template_name = "users/HomeInfo-update.html"

class HomeInfoDelet(HomeInfoFiedsMixin, DeleteView):
    model = HomeInfo
    success_url = reverse_lazy("users:HomeInfo-list")
    template_name = "users/HomeInfo_confirm_delete.html"