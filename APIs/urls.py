from django.urls import path
from . import views

urlpatterns = [
    path(r'Dailymenus/', views.DailyMenu.as_view()),
    path(r'Restaurants/', views.Restaurants.as_view()),

]
