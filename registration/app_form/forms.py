from django import forms
from .models import *
class regis_form(forms.ModelForm):
    # password = forms.PasswordInput()

    class Meta:
        model = Registered_Users
        fields = ('name','email','c_email','dob','contact','address','pincode','country','Gender','password')

        widgets = {
            'password':forms.PasswordInput(),
            'address' :forms.Textarea(attrs={'rows':3,'cols':27}),
        }
    def all_clr(self):
        all_wipe = super().clean()
        print('all_wipe', all_wipe)
        email = all_wipe['email']
        vmail = all_wipe['c_email']

        if email!=vmail:
            raise forms.ValidationError("make sure emails match")
        return True


class generate_otp(forms.ModelForm):

    class Meta:
        model = User_otp
        fields = "__all__"
