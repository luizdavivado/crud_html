from django.urls import path 
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('autor/', views.autor, name='autor'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('delete/<int:id>', views.delete, name='delete'),
 
]