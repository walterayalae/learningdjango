from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content':'Hello im from third app'}
    return render(request, 'third_app/index.html', context=my_dict)
