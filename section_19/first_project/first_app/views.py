from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello I am from views.py"}
    return render(request, 'index.html', context=my_dict)


def help(request):
    my_dict = {'help_insert': "Help Page"}
    return render(request, 'ProTwo/help.html', context=my_dict)
