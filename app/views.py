from django.shortcuts import render
from .models import Book, Reader, Category

def dashboard(request):
    total_books = Book.objects.count()
    total_readers = Reader.objects.count()
    total_categories = Category.objects.count()
    
    recent_books = Book.objects.order_by('-id')[:5]

    context = {
        'total_books': total_books,
        'total_readers': total_readers,
        'total_categories': total_categories,
        'recent_books': recent_books
    }
    return render(request, 'app/dashboard.html', context)
def bookList(request):
    books = Book.objects.all().order_by('-id') 
    return render(request, 'app/bookList.html', {'books': books})

def readerList(request):
    readers = Reader.objects.all().order_by('-created_at')
    return render(request, 'app/readerList.html', {'readers': readers})