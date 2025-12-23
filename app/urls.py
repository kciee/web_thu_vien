from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('books/', views.bookList, name='bookList'),
    path('readers/', views.readerList, name='readerList')
]
