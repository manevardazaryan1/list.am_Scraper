from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('scrap', views.scrap, name='scrap'),
]
