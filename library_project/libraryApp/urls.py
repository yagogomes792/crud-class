from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/<int:book_id>', views.update),
    path('delete/<int:book_id>', views.delete),
]