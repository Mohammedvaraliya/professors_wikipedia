from django.urls import path
from . import views
from .views import ProfessorsListView, ProfessorDetailView, ProfessorSearchView

urlpatterns = [
    path('', views.home, name='home-template'),
    path('professors/', ProfessorsListView.as_view(), name='professor-list'),
    path('professors/<int:pk>/', ProfessorDetailView.as_view(), name='professor-detail'),
    path('search/', ProfessorSearchView.as_view(), name='professor_search'),
]