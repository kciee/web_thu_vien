from django.db import models



class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'CATEGORIES'

    def __str__(self):
        return self.category_name


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'AUTHOR'

    def __str__(self):
        return self.name


class Publisher(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'PUBLISHER'



class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    image_url = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    publisher = models.ForeignKey(
        Publisher,
        db_column='publisher_id',
        on_delete=models.SET_NULL,
        null=True
    )

    authors = models.ManyToManyField(
        Author,
        through='BookAuthor'
    )

    categories = models.ManyToManyField(
        Category,
        through='BookCategory'
    )

    class Meta:
        managed = True
        db_table = 'BOOK'
        
class BookAuthor(models.Model):
    book = models.ForeignKey(Book, db_column='book_id', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, db_column='author_id', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'BOOK_AUTHOR'
        unique_together = ('book', 'author')
        
class BookCategory(models.Model):
    book = models.ForeignKey(Book, db_column='book_id', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, db_column='category_id', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'BOOK_CATEGORY'
        unique_together = ('book', 'category')
        


class BorrowRecord(models.Model):
    borrow_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        'LibraryUser',
        db_column='user_id',
        on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book,
        db_column='book_id',
        on_delete=models.CASCADE
    )
    borrow_date = models.DateField(null=True, blank=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20)
    notified = models.BooleanField(default=False) 
    class Meta:
        managed = True
        db_table = 'BORROW_RECORDS'

class LibraryUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'USERS'

    def __str__(self):
        return self.username

class BorrowHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    borrow = models.ForeignKey(
        BorrowRecord,
        on_delete=models.CASCADE,
        db_column='borrow_id'
    )
    returned_at = models.DateField()
    days_late = models.IntegerField()
    fine = models.IntegerField()

    class Meta:
        db_table = 'BORROW_HISTORY'

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)

    user = models.ForeignKey(
        LibraryUser,
        on_delete=models.CASCADE,
        db_column='user_id'
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        db_column='book_id',
        related_name='reviews'
    )

    rating = models.IntegerField()
    comment = models.TextField()
    sentiment = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'REVIEWS'

class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        LibraryUser,
        on_delete=models.CASCADE,
        db_column='user_id'
    )
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'NOTIFICATIONS'
