
from django.shortcuts import render
from .models import Book, Category, LibraryUser, Author, Publisher
from django.shortcuts import redirect, get_object_or_404
from .models import BorrowRecord
from .models import BorrowHistory
from .models import Review
from .ai.sentiment import analyze_sentiment
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import LibraryUser
from django.contrib.auth.hashers import make_password, check_password

def create_borrow(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        borrow_date = request.POST.get('borrow_date')
        due_date = request.POST.get('return_date')

        book = get_object_or_404(Book, pk=book_id)

        user = LibraryUser.objects.first()  # TẠM (sau này thay bằng user login)

        BorrowRecord.objects.create(
            user=user,
            book=book,
            borrow_date=borrow_date,
            due_date=due_date,
            status='pending'
        )

        return redirect('borrow_request_list')

@staff_member_required
def admin_borrow_manage(request):
    borrows = BorrowRecord.objects.select_related(
        'user', 'book'
    ).order_by('-borrow_id')

    return render(request, 'app/admin_borrow_manage.html', {
        'borrows': borrows
    })
    
@staff_member_required
def admin_approve_borrow(request, borrow_id):
    borrow = get_object_or_404(BorrowRecord, borrow_id=borrow_id)

    if borrow.status == 'pending' and borrow.book.quantity > 0:
        borrow.status = 'borrowing'
        borrow.book.quantity -= 1

        borrow.book.save()
        borrow.save()

    return redirect('admin_borrow_manage')

from datetime import date
from .models import BorrowHistory

@staff_member_required
def admin_approve_return(request, borrow_id):
    borrow = get_object_or_404(BorrowRecord, borrow_id=borrow_id)

    if borrow.status == 'return_pending':
        today = date.today()

        days_late = max((today - borrow.due_date).days, 0)
        fine = days_late * 2000 if days_late > 14 else 0

        BorrowHistory.objects.create(
            borrow=borrow,
            returned_at=today,
            days_late=days_late,
            fine=fine
        )

        borrow.status = 'returned'
        borrow.book.quantity += 1

        borrow.book.save()
        borrow.save()

    return redirect('admin_borrow_manage')


def request_return(request, borrow_id):
    borrow = get_object_or_404(BorrowRecord, pk=borrow_id)

    # chỉ cho phép trả khi đang mượn
    if borrow.status == 'borrowing':
        borrow.status = 'return_pending'
        borrow.save()

    return redirect('borrow_request_list')

from datetime import date

def approve_return(request, borrow_id):
    borrow = get_object_or_404(BorrowRecord, pk=borrow_id)

    if borrow.status == 'return_pending':
        borrow.status = 'returned'
        borrow.save()

        days_late = max((date.today() - borrow.due_date).days, 0)
        fine = days_late * 2000 if days_late > 0 else 0

        BorrowHistory.objects.create(
            borrow=borrow,
            returned_at=date.today(),
            days_late=days_late,
            fine=fine
        )

        # tăng lại số lượng sách
        borrow.book.quantity += 1
        borrow.book.save()

    return redirect('dashboard')

def reject_return(request, borrow_id):
    borrow = get_object_or_404(BorrowRecord, pk=borrow_id)

    if borrow.status == 'return_pending':
        borrow.status = 'borrowing'  # quay lại đang mượn
        borrow.save()

    return redirect('dashboard')


# admin  duyệt mượn
@staff_member_required
def admin_approve_borrow(request, borrow_id):
    borrow = get_object_or_404(BorrowRecord, borrow_id=borrow_id)

    if borrow.status == 'pending' and borrow.book.quantity > 0:
        borrow.status = 'borrowing'
        borrow.book.quantity -= 1

        borrow.book.save()
        borrow.save()

    return redirect('admin_borrow_manage')



def home(request):
    # Lấy 6 cuốn sách mới nhất
    new_books = Book.objects.all().order_by('-book_id')[:6]

    # Gửi vào template
    context = {
        'new_books': new_books
    }

    return render(request, 'app/home.html', context)
# Create your views here.
def login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = LibraryUser.objects.get(username=username)
            if check_password(password, user.password):
                # Lưu session
                request.session['user_id'] = user.user_id
                request.session['username'] = user.username
                request.session['full_name'] = user.full_name
                request.session['role'] = user.role
                if user.role == 'admin':
                    return redirect('dashboard')
                else:
                    return redirect('book_list')
            else:
                error = 'Sai mật khẩu'
        except LibraryUser.DoesNotExist:
            error = 'Người dùng không tồn tại'

    return render(request, 'app/login.html', {'error': error})

def user_logout(request):
    request.session.flush()  # xóa toàn bộ session
    return redirect('login')


def register(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Kiểm tra mật khẩu
        if password != confirm_password:
            error = 'Mật khẩu không khớp'
        # Kiểm tra username/email trùng
        elif LibraryUser.objects.filter(username=username).exists():
            error = 'Username đã tồn tại'
        elif LibraryUser.objects.filter(email=email).exists():
            error = 'Email đã tồn tại'
        else:
            # Lưu vào DB
            LibraryUser.objects.create(
                username=username,
                email=email,
                full_name=full_name,
                password=make_password(password),  # hash password
                created_at=timezone.now(),
                role='user'
            )
            return redirect('login')

    return render(request, 'app/register.html', {'error': error})


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

def fine_list(request):
    fines = BorrowHistory.objects.select_related(
        'borrow__user',
        'borrow__book'
    )
    return render(request, 'app/fine_list.html', {
        'fines': fines
    })

def add_review(request, book_id):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        rating = int(request.POST.get('rating'))

        book = get_object_or_404(Book, book_id=book_id)
        user = LibraryUser.objects.first()  # tạm thời

        sentiment = analyze_sentiment(comment, rating)

        Review.objects.create(
            user=user,
            book=book,
            rating=rating,
            comment=comment,
            sentiment=sentiment
        )

        return redirect('book_list')
#admin page
def dashboard(request):
    total_books = Book.objects.count()
    total_users = LibraryUser.objects.count()
    total_categories = Category.objects.count()
    
    recent_books = Book.objects.order_by('-book_id')[:5]

    context = {
        'total_books': total_books,
        'total_users': total_users,
        'total_categories': total_categories,
        'recent_books': recent_books
    }
    return render(request, 'app/dashboard.html', context)

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'app/category_list.html', {'categories': categories})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'app/author_list.html', {'authors': authors})

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'app/publisher_list.html', {'publishers': publishers})

def bookList(request):
    books = Book.objects.all().order_by('-book_id')
    categories = Category.objects.all()
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    
    context = {
        'books': books,
        'categories': categories, 
        'authors': authors, 
        'publishers': publishers 
    }
    return render(request, 'app/bookList.html', context)

def readerList(request):
    readers = LibraryUser.objects.all().order_by('-created_at')
    return render(request, 'app/readerList.html', {'readers': readers})
def add_reader(request):
    if request.method == 'POST':
        LibraryUser.objects.create(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            created_at=timezone.now()
        )
    return redirect('readerList')
def delete_reader(request, user_id):
    user = get_object_or_404(LibraryUser, pk=user_id)
    user.delete()
    return redirect('readerList')

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('category_name')
        if name:
            Category.objects.create(category_name=name)
        next_url = request.POST.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('bookList')
    return redirect('bookList')

def delete_category(request, category_id):
    cat = get_object_or_404(Category, pk=category_id)
    cat.delete()
    return redirect('category_list')

def edit_category(request, category_id):
    cat = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        name = request.POST.get('category_name')
        if name:
            cat.category_name = name # Lưu ý: Model bạn đặt tên là category_name
            cat.save()
    return redirect('category_list') 

def add_author(request):
    if request.method == 'POST':
        name = request.POST.get('author_name')
        if name:
            Author.objects.create(name=name)
        next_url = request.POST.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('bookList')
    return redirect('bookList')

def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    author.delete()
    return redirect('author_list')

def edit_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        name = request.POST.get('author_name')
        if name:
            author.name = name
            author.save()
    return redirect('author_list')

def add_publisher(request):
    if request.method == 'POST':
        name = request.POST.get('publisher_name')
        if name:
            Publisher.objects.create(name=name)
        next_url = request.POST.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('bookList')
    return redirect('bookList')

def delete_publisher(request, publisher_id):
    pub = get_object_or_404(Publisher, pk=publisher_id)
    pub.delete()
    return redirect('publisher_list')

def edit_publisher(request, publisher_id):
    pub = get_object_or_404(Publisher, pk=publisher_id)
    if request.method == 'POST':
        name = request.POST.get('publisher_name')
        if name:
            pub.name = name
            pub.save()
    return redirect('publisher_list')

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        category_id = request.POST.get('category')
        publisher = request.POST.get('publisher')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        
        image = request.FILES.get('image')

        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            category = None

        Book.objects.create(
            title=title,
            price=price,
            quantity=quantity,
            image_url=image 
        )

        return redirect('bookList') 
    
    categories = Category.objects.all()
    return render(request, 'app/add_book.html')
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('bookList')
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.price = request.POST.get('price')
        book.quantity = request.POST.get('quantity')
        
        if request.FILES.get('image'):
            book.image_url = request.FILES.get('image')

        pub_id = request.POST.get('publisher')
        if pub_id:
            book.publisher = Publisher.objects.get(pk=pub_id)
        author_id = request.POST.get('author')
        category_id = request.POST.get('category')
        
        if author_id:
            book.authors.clear()
            book.authors.add(Author.objects.get(pk=author_id))
            
        if category_id:
            book.categories.clear()
            book.categories.add(Category.objects.get(pk=category_id))

        book.save()
        return redirect('bookList')

    context = {
        'book': book,
        'categories': Category.objects.all(),
        'authors': Author.objects.all(),
        'publishers': Publisher.objects.all(),
    }
    return render(request, 'app/edit_book.html', context)