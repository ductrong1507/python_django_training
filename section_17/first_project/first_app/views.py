from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.


def index(request):
    context_dict = {'text': 'hello world', 'number': 100}
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}


    return render(request, 'index.html', context = date_dict)
