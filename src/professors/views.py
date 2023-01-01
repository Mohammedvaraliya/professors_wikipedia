from django.shortcuts import render
from django.views.generic import ListView
from .models import Professor

# Create your views here.
def home(request):
    context = {
        'title': 'Professors Wikipedia',
        'professors': Professor.objects.all()
    }
    return render(request, 'professors/base.html', context)

class ProfessorsListView(ListView):
    model = Professor
    template_name = 'professors/professors_list.html' # reference -> <app>/<model>_<viewtype>.html = blog/post_list.html
    context_object_name = 'professors'