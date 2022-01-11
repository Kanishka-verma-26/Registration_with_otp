from django.shortcuts import render,redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import *
import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
from django.views.generic import (DeleteView, CreateView,UpdateView)


def indexx(request):
    return render(request,'indexx.html')

def mail_success(request):
    return render(request,'mail_success.html')

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
        message = request.POST["msg"]
        print(receiver_email, ' ',subject, ' ', email_from, ' ', message)
        send_mail(subject, message, email_from, receiver_email)
        # return render(request,'otp.html')
        return redirect('mail_success')
    return render(request,'email_send.html')


def enter_otp(request):
    print("11111111111111111111 in enter otps")
    if request.method=='POST':
        # email_otp()
        otp_code=request.POST["dig1"]+request.POST["dig2"]+request.POST["dig3"]+request.POST["dig4"]+request.POST["dig5"]+request.POST["dig6"]
    return otp_code



def otp(request,username):

    otp_validation =0
    if request.method=='POST':
        print("in otp")

        #Get the user from url

        user = User.objects.get(username=username)
        r_us = Registered_Users.objects.get(author=user)
        print("inside POST ",r_us)

        #get the otp from otp db
        u_us = User_otp.objects.get(registered_user = r_us)
        print("inside POST ",u_us.otp)
        e_time = str(u_us.otp_expiration_time)[:-6]
        print("expiration time : " ,str(u_us.otp_expiration_time)[:-6]," recent time : ",datetime.datetime.now())
        # code = (User_otp.objects.get(otp=otp))
        # print("Dear ", r_us," your otp code is ",code)

        #validate whether entered otp== queried otp

        form = User_otp(request.POST)
        otp_code=request.POST["dig1"]+request.POST["dig2"]+request.POST["dig3"]+request.POST["dig4"]+request.POST["dig5"]+request.POST["dig6"]
        i=0

        while str(datetime.datetime.now()) <= e_time:
            print("recent: ",str(datetime.datetime.now())," and expire ", e_time)
            if u_us.otp == otp_code:
                    user.is_active = True
                    user.save()
                    print("ran successfully")
                    return render(request,'success.html')
            else:
                return HttpResponse("click back n try again ")
                # return redirect(reverse('otp',kwargs={'username':str(user.username),'e_time':str(three_mins_after)}))
        r_us.delete()
        return render(request,'time_over.html')
    # return otp_code
    else:
        otp_form = generate_otp()
        user = User.objects.get(username=username)
        r_us=(Registered_Users.objects.get(author=user))
        print("outside post ",r_us)
        u_us = User_otp.objects.get(registered_user=r_us)
        print("ouside POST ", u_us.otp)
        print("hello there")

        return render(request,'otp.html')


def send_otp(email):
    subject = "welcome to Django world"
    email_from = settings.EMAIL_HOST_USER
    num = ran(6)
    message = f'Hi , thankyou for registering in Django World. your 6 digit OTP number is {num}. kindly proceed further'
    print(email, ' ', subject, ' ', email_from, ' ', message)
    send_mail(subject, message, email_from, email)
    print(type(num))
    return num


def time_over(request):
    # if request.method=='post':
    return render(request, 'time_over.html')

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
                    a=(send_otp([str(form.cleaned_data['email'])]))
                    if a:
                        user = User.objects.create(username = form.cleaned_data['name'])
                        user.is_active = False
                        user.save()

                        # adding Superuser in Registered Users model also so that every superuser can be the registered user also
                        r_us = Registered_Users(author = user)
                        r_us.name = form.cleaned_data['name']
                        r_us.dob = form.cleaned_data['dob']
                        r_us.address = form.cleaned_data['address']
                        r_us.country = form.cleaned_data['country']
                        r_us.pincode = form.cleaned_data['pincode']
                        r_us.email = form.cleaned_data['email']
                        r_us.c_email = form.cleaned_data['c_email']
                        r_us.contact = form.cleaned_data['contact']
                        r_us.Gender = form.cleaned_data['Gender']
                        r_us.password = form.cleaned_data['password']

                        r_us.save()

                        # calling User_otp model
                        User_otp.objects.create(registered_user = r_us, otp = a)

                        print(datetime.datetime.now())
                        expiretime=(datetime.datetime.now()+ datetime.timedelta(minutes=1))
                        three_mins_after = str(expiretime).split()[1]
                        print(expiretime)


                        return redirect(reverse('otp',kwargs={'username':str(user.username)}))
                    else:
                        return HttpResponse("Something went wrong")

                    # r_us.dob = '456'
                    # u = Registered_Users.objects.get(id = 1)
                    # u.dob = '789'Kanishka
                    # u.save()
                    mail_validation = 1

            except Exception as e:
                print("Exception is:- ",e)
                mail_validation = 0
                return render(request, 'form.html', {'form': form, 'mail_validation':mail_validation})


    return render(request,'form.html',{'form':form, 'mail_validation':mail_validation})


class CreateUser(CreateView):
    model = Registered_Users
    form_class = regis_form

def login(request):
    print("outside")

    if request.method == "POST":
        print("inpost")
        print(request.POST)
        entered_email = (request.POST.get('Email'))
        entered_password = (request.POST.get('Password'))
        print('email : ', entered_email, " and pssword : ", entered_password)
        r_em = Registered_Users.objects.filter(email=entered_email)
        r_ps = Registered_Users.objects.filter(password=entered_password)
        print("Emails : ",r_em)
        print("Passwords : ",r_ps)
        # print(r_em[0])
        print(r_em.exists())
        print(r_ps.exists())
        print("length ",len(r_ps))
        if r_em.exists() == False and r_ps.exists() == False:
            return HttpResponse("User doesn't exist...... kindlt register yourself!!!!!!!!!!!")

        elif r_em.exists() == False or r_ps.exists() == False:
            return HttpResponse("Incorrect username or password")

        else:
            for i in range(len(r_ps)):
                if r_em[0] == r_ps[i]:
                    return HttpResponse ("WOoHoOo!!!!!  User exists")


    return render(request,'login.html')

