
from django.shortcuts import render
from .models import Book, Category, LibraryUser
from django.shortcuts import redirect
from .models import BorrowRecord
from .models import BorrowHistory

def create_borrow(request):
    if request.method == 'POST':
        # tạm thời chưa xử lý DB
        return redirect('book_list')



def home(request):
    return render(request, 'app/home.html')
# Create your views here.
def login(request):
    return render(request, 'app/login.html')

def register(request):
    return render(request, 'app/register.html')


def book_list(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(request, 'app/book_list.html', {
        'books': books,
        'categories': categories
    })
    
def resource(request):
    return render(request, 'app/resource.html')


def borrow_request_list(request):
    borrow_requests = BorrowRecord.objects.all()
    return render(request, 'app/borrow_request_list.html', {
        'borrow_requests': borrow_requests
    })


def dashboard(request):
    total_books = Book.objects.count()
    total_users = LibraryUser.objects.count()
    total_categories = Category.objects.count()
    
    recent_books = Book.objects.order_by('-id')[:5]

    context = {
        'total_books': total_books,
        'total_users': total_users,
        'total_categories': total_categories,
        'recent_books': recent_books
    }
    return render(request, 'app/dashboard.html', context)

def bookList(request):
    books = Book.objects.all().order_by('-id') 
    return render(request, 'app/bookList.html', {'books': books})

def readerList(request):
    readers = LibraryUser.objects.all().order_by('-created_at')
    return render(request, 'app/readerList.html', {'readers': users})

def fine_list(request):
    fines = BorrowHistory.objects.select_related(
        'borrow__user',
        'borrow__book'
    )
    return render(request, 'app/fine_list.html', {
        'fines': fines
    })

