from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.all_view, name='all'),
    path('actors/', views.actors, name='actors'),
]