from django.contrib.auth import views
from django.urls import path
from django.contrib.auth.views import PasswordChangeDoneView,PasswordChangeView
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "users"

urlpatterns = [
    path('',home, name="home"),
    path('home/',home),
    path('login/',login, name="login"),
    path('auth/admin/',admin, name="admin-lte"),
    path('auth/user/user_info/',user_information),
    path('auth/user/user_info/edit/<int:pk>',edit_info.as_view()),
    path('data/User/content/' , User_serializer),
    path('data/User/content/update/' , user_serializer_update),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Notification
urlpatterns += [
    path('Notification/create/', NotificationCreate.as_view(), name="notification-create"),
    path('Notification/List/', NotificationList.as_view(), name="notification-list"),
    path('Notification/Update/<int:pk>', NotificationUpdate.as_view(), name="notification-update"),
    path('Notification/Delet/<int:pk>', NotificationDelet.as_view(), name="notification-delet"),
]

# Circular
urlpatterns += [
    path('Circular/create/', CircularCreate.as_view(), name="Circular-create"),
    path('Circular/List/', CircularList.as_view(), name="Circular-list"),
    path('Circular/Update/<int:pk>', CircularUpdate.as_view(), name="Circular-update"),
    path('Circular/Delet/<int:pk>', CircularDelet.as_view(), name="Circular-delet"),
    
]

# Works

urlpatterns += [
    path('Works/create/', WorksCreate.as_view(), name="Works-create"),
    path('Works/List/', WorksList.as_view(), name="Works-list"),
    path('Works/Update/<int:pk>', WorksUpdate.as_view(), name="Works-update"),
    path('Works/Delet/<int:pk>', WorksDelet.as_view(), name="Works-delet"),
    
]

# Users

urlpatterns += [
    path('User/create/', UserCreate.as_view(), name="User-create"),
    path('User/List/', UserList.as_view(), name="User-list"),
    path('User/Update/<int:pk>', UserUpdate.as_view(), name="User-update"),
    path('User/Delet/<int:pk>', UserDelet.as_view(), name="User-delet"),
    path("logout/", views.LogoutView.as_view(), name="logout")
    
]

urlpatterns += [
    path('password_change/<int:pk>',password_recovery,name='password_change'),
    path('password_change/done/',password_change_done,name='password_change_done'),

]

# gallery

urlpatterns += [
    path('Gallery/images/WorkList/' , Work_Image_List.as_view() , name='Work_Image-List'),
    path('Gallery/images/CircularList/',Circular_Images_List.as_view() , name='Circular_Image-List')
]


# faq 

urlpatterns += [
    path('faq/List/', faqlist.as_view(), name="faq-list"),
    path('faq/create/', FaqCreate.as_view(), name="faq-create"),
    path('faq/Update/<int:pk>', faqUpdate.as_view(), name="faq-update"),
    path('faq/Delet/<int:pk>', faqDelet.as_view(), name="faq-delet")
]

# Handout


urlpatterns += [
    path('Handout/List/', HandoutList.as_view(), name="Handout-list"),
    path('Handout/create/', HandoutCreate.as_view(), name="Handout-create"),
    path('Handout/Update/<int:pk>', HandoutUpdate.as_view(), name="Handout-update"),
    path('Handout/Delet/<int:pk>', HandoutDelet.as_view(), name="Handout-delet")
]

# SectionChoice 

urlpatterns += [
    path('sectionchoice/List/', SectionChoice_list.as_view(), name="sectionchoice-list"),
    path('sectionchoice/Delete/<int:pk>', SectionChoice_Delet.as_view(), name="sectionchoice-delete")
]

urlpatterns += [
    path('picture/create/' , create_picture.as_view(),name="picture-create"),
    path('picture/list/' , picture_list.as_view(),name="picture-list"),
    path('picture/delete/<int:pk>' , delete_picture.as_view(),name="picture-delete"),
    
]

urlpatterns += [
    path('HomeInfo/List/', HomeInfoList.as_view(), name="HomeInfo-list"),
    path('HomeInfo/create/', HomeInfoCreate.as_view(), name="HomeInfo-create"),
    path('HomeInfo/Update/<int:pk>', HomeInfoUpdate.as_view(), name="HomeInfo-update"),
    path('HomeInfo/Delet/<int:pk>', HomeInfoDelet.as_view(), name="HomeInfo-delet")
]