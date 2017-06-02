from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def help(request):
    my_dir = {'insert_help':'Here is the help page!'}
    return render(request, 'second_app/help.html', context=my_dir)
