from django.contrib import admin
from .models import Book, Author, Category, Publisher


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'name')



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')



@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('publisher_id', 'name')



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'price',
        'quantity',
        'publisher',
    )
