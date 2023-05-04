from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def other(request):
    return render(request, 'basicapp/other.html')

def base(request):
    my_dict = {'text': 'this is a Demo text', 'number': 1000}
    return render(request, 'basicapp/base.html', context=my_dict)

def relatives(request):
    return render(request, 'basicapp/relative_url_template.html')
