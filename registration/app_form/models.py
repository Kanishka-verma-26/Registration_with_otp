from django.db import models
from django.utils import timezone
from datetime import timedelta
import datetime
from django.urls import reverse


# Create your models here.
class Registered_Users(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,default="", editable=False)
    dob = models.CharField(max_length=10)
    address = models.TextField(max_length=200, default='xyz')
    country = models.CharField(max_length=150)
    pincode = models.IntegerField(max_length=6,default=110093)
    email=models.EmailField()
    contact = models.IntegerField(max_length=10,default=1234567890)
    # gender = models.CharField(max_length= 6, null=True, blank=True)
    create_date = models.DateTimeField(default=timezone.now)

    class Meta:
        # verbose_name_plural='Registered User'
        verbose_name='Registered User'


    def get_absolute_url(self):
        return reverse("user_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.author.username


class User_otp(models.Model):
    registered_user = models.OneToOneField(Registered_Users,on_delete=models.CASCADE)
    otp = models.IntegerField()
    expiration_time = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(minutes=5))

    def __str__(self):
        return self.registered_user.author.username