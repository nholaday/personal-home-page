from django.urls import path
from homepage_app import views

urlpatterns = [
    path('', views.index, name='index')
]
