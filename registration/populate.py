import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CBV.settings')

import django
django.setup()

## fake pop script
import random
from app_form.models import *
from faker import Faker


fakegen = Faker()
skl = ['Delhi Public School','Nutan Vidya Mandir','Green Fields','Green Way','Kendra Vidyalaya', 'St. Jones']
def school_add(N=6):
    for i in range(6):
        fake_pname = fakegen.name()
        fake_loc = fakegen.address()
        fake_name = skl[i]
        school = School.objects.get_or_create(principle=fake_pname, name=fake_name, location=fake_loc)

def student_add():
    for i in range(40):
        fake_name = fakegen.name()
        fake_dob = fakegen.date_of_birth()
        fake_nation = fakegen.objects.get_or_create(name=random.choice(skl))[0]
        fake_sname.save()
        student = Student.objects.get_or_create(age=fake_age, school=fake_sname, name=fake_name)[0]


if __name__=='__main__':
    print("populating script!")
    student_add()
    print("populating complete!")