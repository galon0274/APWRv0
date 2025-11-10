from django.urls import path
from . import views

urlpatterns = [
    path('', views.apptest, name='apptest'),
    path('apptest/', views.apptest, name='apptest'),
    path('first/', views.first, name='first'),
    path('api/receive-text/', views.receive_text_data, name='receive_text'),
]