from django.urls import path
from . import views

urlpatterns = [
    path('', views.apptest, name='apptest'),
    path('apptest/', views.apptest, name='apptest'),
]