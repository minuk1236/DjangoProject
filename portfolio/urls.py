from django.urls import path

from . import views


urlpatterns = [
    path('', views.portfolio, name="portfolio"),
    path('upload/', views.upload, name="upload"),
]