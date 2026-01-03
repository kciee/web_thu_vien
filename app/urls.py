from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('resource/', views.resource, name='resource'),
    path('borrow-requests/', views.borrow_request_list, name='borrow_request_list'),
    path('borrow/create/', views.create_borrow, name='create_borrow'),
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('books_manage/', views.bookList, name='bookList'),
=======
    path('dashboard/', views.dashboard, name='dashboard'),
    path('books_admin/', views.bookList, name='bookList'),
>>>>>>> 453804d9ca8fcd9dfdd7ee8d22b17187d30ed355
    path('readers/', views.readerList, name='readerList'),
    path('fines/', views.fine_list, name='fine_list'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
<<<<<<< HEAD
    path('profile/', views.home, name='profile'),
    path('add_book/', views.add_book, name='add_book')
=======
    path('books/<int:book_id>/review/', views.add_review, name='add_review'),

>>>>>>> 453804d9ca8fcd9dfdd7ee8d22b17187d30ed355
]

