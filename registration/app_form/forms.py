from django import forms
from .models import *
class regis_form(forms.ModelForm):
    name=forms.CharField(required=True)
#     dob = forms.DateField(help_text='(yyyy-mm-dd)')
#     address = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':35}),required=True)
#     country=forms.CharField(required=True)
#     pincode = forms.IntegerField(required=True)
#     email=forms.EmailField(required=True)
    c_email = forms.EmailField(label='Confirm Email', required=True)
#     contact = forms.IntegerField(required = True)
    CHOICES = [('M', 'Male'), ('F', 'Female')]
    Gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))

    class Meta:
        model = Registered_Users
        # fields=('author.username','dob','address','country','pincode','email','contact','gender','create_date')
        fields = "__all__"
        extra_fields = ('name','c_email','CHOICES','Gender')
    def all_clr(self):
        all_wipe = super().clean()
        print('all_wipe', all_wipe)
        email = all_wipe['email']
        vmail = all_wipe['c_email']

        if email!=vmail:
            raise forms.ValidationError("make sure emails match")
        return True
