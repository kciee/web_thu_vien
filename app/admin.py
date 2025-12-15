from django.contrib import admin
from .models import Category, Book, Reader

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'quantity', 'available_copies') 
    search_fields = ('title', 'author', 'isbn') 
    list_filter = ('category',) 

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('library_card_id', 'fullname', 'phone', 'created_at') 
    search_fields = ('fullname', 'library_card_id', 'phone')

admin.site.register(Category)