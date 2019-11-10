from django.urls import path

from HomeworkBackend.Homework1 import views

urlpatterns= [
    path('pokemon/', views.pokemon_list),
    path('pokemon/<int:id>/', views.pokemon_detail),
    path('pokemon_trainer/', views.pokemon_trainer_list),
    path('pokemon_trainer/<int:id>/', views.pokemon_trainer_detail),
]
