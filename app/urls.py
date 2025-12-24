from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('resource/', views.resource, name='resource'),
    path('borrow-requests/', views.borrow_request_list, name='borrow_request_list'),
    path('borrow/create/', views.create_borrow, name='create_borrow'),

]