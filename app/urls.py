from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('resource/', views.resource, name='resource'),
    path('borrow-requests/', views.borrow_request_list, name='borrow_request_list'),
    path('borrow/create/', views.create_borrow, name='create_borrow'),
    path('fines/', views.fine_list, name='fine_list'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.home, name='profile'),
    path('add_book/', views.add_book, name='add_book'),
    path('books/<int:book_id>/review/', views.add_review, name='add_review'),
    path('borrow/<int:borrow_id>/return/', views.request_return, name='request_return'),
    #admin
    path('borrow/<int:borrow_id>/approve-return/',views.admin_approve_return,name='approve_return'),

    path('borrow/<int:borrow_id>/reject-return/', views.reject_return),
    # ✅ ĐÚNG
    path('dashboard/borrow/', views.admin_borrow_manage, name='admin_borrow_manage'),
    path('dashboard/borrow/<int:borrow_id>/approve/', views.admin_approve_borrow, name='admin_approve_borrow'),
    path('dashboard/borrow/<int:borrow_id>/return/', views.admin_approve_return, name='admin_approve_return'),

    path('fines/pay/<int:history_id>/', views.request_payment, name='pay_fine'),
    path('dashboard/payments/', views.admin_payment_list, name='admin_payment_list'),
    path('dashboard/payments/approve/<int:payment_id>/', views.approve_payment, name='approve_payment'),


    path('dashboard/', views.dashboard, name='dashboard'),
    path('books_manage/', views.bookList, name='bookList'),
    path('readers/', views.readerList, name='readerList'),
    path('add_reader/', views.add_reader, name='add_reader'),
    path('delete_reader/<int:user_id>/', views.delete_reader, name='delete_reader'),
    path('categories/', views.category_list, name='category_list'),
    path('add_category/', views.add_category, name='add_category'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('authors/', views.author_list, name='author_list'),
    path('add_author/', views.add_author, name='add_author'),
    path('delete_author/<int:author_id>/', views.delete_author, name='delete_author'),
    path('edit_author/<int:author_id>/', views.edit_author, name='edit_author'),
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('add_publisher/', views.add_publisher, name='add_publisher'),
    path('delete_publisher/<int:publisher_id>/', views.delete_publisher, name='delete_publisher'),
    path('edit_publisher/<int:publisher_id>/', views.edit_publisher, name='edit_publisher'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
]

