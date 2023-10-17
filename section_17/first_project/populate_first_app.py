import os


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SETTINGS_DIR = os.path.join(BASE_DIR, 'first_project')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE',
#                       SETTINGS_DIR.first_project.settings)

import django
django.setup()

# Fake pop script
import random
from faker import Faker
from first_app.models import AccessRecord, Topic, Webpage

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    # Get or create the topic
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        # Get the topic for the entry
        top = add_topic()

        # Create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(
            topic=top, url=fake_url, name=fake_name)[0]

        # Create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(
            name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print('Populating script!')
    populate(20)
    print('Populating complete!')

# Run the script
# python populate_first_app.py
