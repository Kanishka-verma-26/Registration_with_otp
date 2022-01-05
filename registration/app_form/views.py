from django.shortcuts import render,redirect, get_object_or_404
from . import forms
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .models import *
from django.views.generic import (DeleteView, CreateView,UpdateView)


def indexx(request):
    return render(request,'indexx.html')
#
# def otp(request):
#     if
#     return render(request,'login.html')

def success(request):
    return render(request,'success.html')
from random import randint
def ran(n):
    num = ''
    for i in range(n):
        num += str(randint(0, 9))
    return (num)
# for Email in navbar
def email_send(request):
    if request.method=='POST':
        receiver_email = [request.POST["r_email"],]
        subject = request.POST["sub"]
        email_from = settings.EMAIL_HOST_USER
        num = ran(6)
        message = request.POST["msg"]+" "+num


        print(receiver_email, ' ',subject, ' ', email_from, ' ', message)
        send_mail(subject, message, email_from, receiver_email)
        # return render(request,'otp.html')
        return redirect('success')
    return render(request,'email_send.html')

# def email_otp(request):
#     if request.method=='POST':
#         # receiver_email = [request.POST["r_email"],]
#         subject = "welcome to Django world"
#         email_from = settings.EMAIL_HOST_USER
#         num = ran(6)
#         message = f'Hi , thankyou for registering in Django World. your 6 digit OTP number is {num}. kindly proceed further'
#
#
#         print(receiver_email, ' ',subject, ' ', email_from, ' ', message)
#         send_mail(subject, message, email_from, receiver_email)
#         # return render(request,'otp.html')
#     #     return redirect('success')
#     # return render(request,'email_send.html')

# def otp(request):
#
#     if request.method=='POST':
#         # email_otp()
#         otp_code=request.POST["dig1"]+request.POST["dig2"]+request.POST["dig3"]+request.POST["dig4"]+request.POST["dig5"]+request.POST["dig6"]
#     return render(request,'otp.html')




def otp(request):

    if request.method=='POST':
        # email_otp()
        otp_code=request.POST["dig1"]+request.POST["dig2"]+request.POST["dig3"]+request.POST["dig4"]+request.POST["dig5"]+request.POST["dig6"]
    return otp_code
    # return render(request,'otp.html')

def send_otp(email):
    subject = "welcome to Django world"
    email_from = settings.EMAIL_HOST_USER
    num = ran(6)
    message = f'Hi , thankyou for registering in Django World. your 6 digit OTP number is {num}. kindly proceed further'
    print(email, ' ', subject, ' ', email_from, ' ', message)
    send_mail(subject, message, email_from, email)
    print(type(num))
    return [True,num]


def form_view(request):
    form = regis_form()
    mail_validation = 1

    if request.method == 'POST':
        form=regis_form(request.POST)
        print(request.POST.items())
        # print("form data is:- ",form)
        print(form.is_valid())

        if form.is_valid():
            # print(form.all_clr())
            try:
                if form.all_clr():
                    print(type(form.cleaned_data['dob']))
                    print("VALIDATION SUCCESS!")
                    print("Name: "+form.cleaned_data['name'])
                    print("D.O.B.: "+str(form.cleaned_data['dob']))
                    print("Email: "+form.cleaned_data['email'])
                    print("Nationality: "+form.cleaned_data['country'])
                    print("Contact: "+str(form.cleaned_data['contact']))
                    print("Gender: "+form.cleaned_data['Gender'])

                    # ********* creating db **********8

                    # creating Superuser by accessing 'auth.User' from Registered_Users model
                    user = User.objects.create(username = form.cleaned_data['name'])
                    # adding Superuser in Registered Users model also so that every superuser can be the registered user also
                    r_us = Registered_Users(author = user)
                    print("2111111111111111111111",r_us)
                    r_us.save()
                    # r_us.dob = '456'
                    # u = Registered_Users.objects.get(id = 1)
                    # u.dob = '789'
                    # u.save()


                    mail_validation = 1

                    # if(send_otp([str(form.cleaned_data['email'])])):
                    #     return redirect('otp')
                    # else:
                    #     return HttpResponse('''Some err occurred''')

                    # a = send_otp([str(form.cleaned_data['email'])])

                    # if a[0]:
                    #     valid_otp = (a[1])
                    #     # print(valid_otp)
                    #     z=otp_validatn()
                    #     print(z)
                    #     entered_otp = z[0]
                    #     while datetime.datetime.now != z[1]:
                    #         if valid_otp == entered_otp :
                    #             return render(request,'success.html')


                    # return render(request,'form.html')
                    return render(request, 'success.html')



            except Exception as e:
                print("Exception is:- ",e)
                mail_validation = 0
                return render(request, 'form.html', {'form': form, 'mail_validation':mail_validation})


    return render(request,'form.html',{'form':form, 'mail_validation':mail_validation})



def otp_validatn():
    u_otp=User_otp.objects.get(otp)
    print(u_otp)
    time_valid = User_otp.objects.get(id=3)
    return [u_otp,time_valid]

# User_otp.objects.create(registered_user = )
class CreateUser(CreateView):
    form_class = regis_form
    model=Registered_Users



