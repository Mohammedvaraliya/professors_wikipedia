from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Professors Wikipedia',
    }
    return render(request, 'professors/index.html', context)
