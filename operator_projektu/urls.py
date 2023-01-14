from django.urls import path
from . import views

urlpatterns = [

    path('', views.ApiOverview, name='home'),

    path('operator/create/', views.add_operator, name='Dodaj operatora projektu'),
    path('operator/all/', views.view_operator, name='Pokaz operatorow projektu'),
    path('operator/update/<int:pk>/', views.update_operator, name='update-items'),
    path('operator/item/<int:pk>/delete/', views.delete_operator, name='delete-items'),

    path('kategoria/create/', views.add_category, name='Dodaj operatora projektu'),
    path('kategoria/all/', views.view_category, name='Pokaz operatorow projektu'),
    path('kategoria/update/<int:pk>/', views.update_category, name='update-items'),
    path('kategoria/item/<int:pk>/delete/', views.delete_category, name='delete-items'),

    path('inicjatywa/create/', views.add_initiative, name='Dodaj operatora projektu'),
    path('inicjatywa/all/', views.view_initiative, name='Pokaz operatorow projektu'),
    path('inicjatywa/update/<int:pk>/', views.update_initiative, name='update-items'),
    path('inicjatywa/item/<int:pk>/delete/', views.delete_initiative, name='delete-items'),

    # path('uzytkownik/create/', views.add_user, name='Dodaj operatora projektu'),
    # path('uzytkownik/all/', views.view_user, name='Pokaz operatorow projektu'),
    # path('uzytkownik/update/<int:pk>/', views.update_user, name='update-items'),
    # path('uzytkownik/item/<int:pk>/delete/', views.delete_user, name='delete-items'),

    path('uczestnik/create/', views.add_participant, name='Dodaj operatora projektu'),
    path('uczestnik/all/', views.view_participant, name='Pokaz operatorow projektu'),
    path('uczestnik/update/<int:pk>/', views.update_participant, name='update-items'),
    path('uczestnik/accept/<int:pk>/', views.accept_participant, name='update-items'),
    path('uczestnik/item/<int:pk>/delete/', views.delete_participant, name='delete-items'),
]