from django.urls import path

from . import views
from .views import *


urlpatterns=[
    # path('help',views.help,name='HELP'),
    path('', views.indexx, name='indexx'),
    path('form/', views.form_view, name='form'),
    path('form/new/', views.form_view,name='form'),
    path('success/', views.success, name='success'),
    path('otp/<str:username>/', views.otp, name='otp'),
    # path('otp/<user:r_us.name>',views)
    path('email_send/', views.email_send, name='email_send'),
    path('login/', views.login, name='login'),
    path('time_over/', views.time_over, name='time_over'),
    path('mail_success/', views.mail_success, name='mail_success'),

]