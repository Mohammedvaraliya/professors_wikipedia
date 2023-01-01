from django.shortcuts import render
from django.views.generic import ListView, DetailView
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


class ProfessorDetailView(DetailView):
    model = Professor
    template_name = 'professors/professor_detail.html'
    context_object_name = 'professor'

class ProfessorSearchView(ListView):
    model = Professor
    template_name = 'professors/professor_search.html'
    context_object_name = 'professors'

    def get_queryset(self):
        search_term = self.request.GET.get('q')
        if search_term:
            return Professor.objects.filter(name__icontains=search_term)
        return Professor.objects.all()