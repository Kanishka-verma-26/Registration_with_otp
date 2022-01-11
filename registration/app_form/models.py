from django.db import models
from django.utils import timezone
from datetime import timedelta
import datetime
from django.urls import reverse


# Create your models here.
class Registered_Users(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,default="", editable=False)
    name=models.CharField(max_length=50,default="",unique=False)
    dob = models.CharField(max_length=10,help_text='(yyyy-mm-dd)')
    address = models.TextField(max_length=200, default='xyz')
    country = models.CharField(max_length=150,default="")
    pincode = models.IntegerField(max_length=6,default=110093)
    email=models.EmailField()
    c_email = models.EmailField(verbose_name="Confirm Email",default='')
    contact = models.IntegerField(max_length=10,default=1234567890)
    CHOICES = [('M', 'Male'), ('F', 'Female')]
    Gender = models.CharField(choices=CHOICES,max_length=6, default='')
    create_date = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=50,default='Hash@123',null=False)

    class Meta:
        # verbose_name_plural='Registered User'
        verbose_name='Registered User'


    def get_absolute_url(self):
        return reverse("user_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.author.username


class User_otp(models.Model):
    registered_user = models.OneToOneField(Registered_Users,on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    otp_generate_time = models.DateTimeField(default=datetime.datetime.now(tz=timezone.utc))
    otp_expiration_time = models.DateTimeField(default=datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(minutes=2))

    def __str__(self):
        return self.registered_user.author.username

