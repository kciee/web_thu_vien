from django.contrib import admin
from .models import Book, Author, Category, Publisher, Review


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

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'book', 'user', 'rating', 'sentiment', 'created_at')
