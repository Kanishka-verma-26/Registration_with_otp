from django.urls import path

from . import views
from .views import *


urlpatterns=[
    # path('help',views.help,name='HELP'),
    path('', views.indexx, name='indexx'),
    path('form/', views.form_view, name='form'),
    path('form/new/', views.CreateUser.as_view(),name='form_new'),
    path('success/', views.success, name='success'),
    path('otp/', views.otp, name='otp'),
    path('email_send/', views.email_send, name='email_send'),
    path('login/', views.login, name='login'),

]