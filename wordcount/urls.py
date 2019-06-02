from django.urls import path

from . import views


urlpatterns = [
    path('count/', views.count, name="count"),
    path('', views.wordcount, name="wordcount"),

]