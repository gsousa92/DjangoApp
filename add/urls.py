from django.urls import path

from . import views

urlpatterns = [
    path('', views.AddPage, name='add'),
]