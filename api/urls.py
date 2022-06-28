from django.urls import path

from .views import PredictView
from . import views

urlpatterns = [
    path('', views.PredictView, name="house-predict"),
    path('send/', views.SendData, name="send-data")
]