from django.http import HttpResponseForbidden , Http404
from django.shortcuts import get_object_or_404 
from rest_framework.status import HTTP_403_FORBIDDEN
class NotificationFiedsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self. fields = [
                "title", 
                "text",
                "status"
            ]
        elif request.user.is_staff:
            self. fields = [
                "title",
                "text",
            ]
        else :
            return HttpResponseForbidden("شما به این صفحه دسترسی ندارید" )
        return super().dispatch(request, *args, **kwargs)


class CircularFiedsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self. fields = [
                "title",
                "text",
                "image",
                "status"
            ]
        elif request.user.is_staff:
            self. fields = [
                "title",
                "text",
                "image"
            ]
        else :
            return HttpResponseForbidden("شما به این صفحه دسترسی ندارید")
        return super().dispatch(request, *args, **kwargs)


class WorksFiedsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self. fields = [
                "name",
                "caption",
                "image",
                "file",
                "video",
                "status"
            ]
        elif request.user.is_staff:
            self. fields = [
                "name",
                "caption",
                "image",
                "file",
                "video"
            ]
        else :
            return HttpResponseForbidden("شما به این صفحه دسترسی ندارید")
        return super().dispatch(request, *args, **kwargs)
    
    
class UserFiedsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser :
            self. fields = [
                "username",
                "first_name",
                "last_name",
                "email",
                "is_superuser",
                "password",
                "is_staff",
            ]
        else :
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)
    
    
class FaqFiedsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self. fields = '__all__'
        elif request.user.is_staff:
            self. fields = [
                "question",
                "awnser",
                "section",
                "create_by",
               "lesson_sections"
            ]
        else :
            return HttpResponseForbidden("شما به این صفحه دسترسی ندارید")
        return super().dispatch(request, *args, **kwargs)
    
    
    
class HandoutFiedsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self. fields = '__all__'
        elif request.user.is_staff:
            self. fields = '__all__'
        else :
            return HttpResponseForbidden("شما به این صفحه دسترسی ندارید")
        return super().dispatch(request, *args, **kwargs)
    

class SectionChoiceFieldMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self. fields = '__all__'
        else :
            return HttpResponseForbidden("شما به این صفحه دسترسی ندارید")
        return super().dispatch(request, *args, **kwargs)
    
    
class HomePicturesFieldMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self. fields = '__all__'
        else :
            return HttpResponseForbidden("شما به این صفحه دسترسی ندارید")
        return super().dispatch(request, *args, **kwargs)
    


class HomeInfoFiedsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self. fields = '__all__'
        else :
            return HttpResponseForbidden("شما به این صفحه دسترسی ندارید")
        return super().dispatch(request, *args, **kwargs)