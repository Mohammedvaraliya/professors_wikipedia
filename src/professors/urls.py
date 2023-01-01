from django.urls import path
from . import views
from .views import ProfessorsListView

urlpatterns = [
    path('', views.home, name='home-template'),
    path('professors/', ProfessorsListView.as_view(), name='professor-list'),
]