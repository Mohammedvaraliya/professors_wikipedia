from django.urls import path
from . import views
from .views import ProfessorsListView, ProfessorDetailView, ProfessorSearchView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home-template'),
    path('professors/', ProfessorsListView.as_view(), name='professor-list'),
    path('professors/<int:pk>/', ProfessorDetailView.as_view(), name='professor-detail'),
    path('search/', ProfessorSearchView.as_view(), name='professor_search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)