import os 
import django

from faker import Faker 

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

django.setup()

from AppTwo.models import User

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name =  fakegen.name().split()
        fake_first_name= fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name = fake_first_name, last_name= fake_last_name, email_name= fake_email)

if __name__ =='__main__':
    print('Populate Script!')
    populate(30)
    print('populate Completed')