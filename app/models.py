from django.db import models
from django.utils import timezone
from datetime import timedelta

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên thể loại")
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tên sách")
    author = models.CharField(max_length=100, verbose_name="Tác giả")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Thể loại")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="Mã ISBN")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Số lượng tổng")
    available_copies = models.PositiveIntegerField(default=1, verbose_name="Sẵn có")
    
    def __str__(self):
        return self.title
    
class Reader(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="Họ và tên")
    library_card_id = models.CharField(max_length=20, unique=True, verbose_name="Mã thẻ thư viện")
    phone = models.CharField(max_length=15, verbose_name="Số điện thoại")
    email = models.EmailField(verbose_name="Email", null=True, blank=True)
    address = models.TextField(verbose_name="Địa chỉ", null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name="Ngày làm thẻ")

    def __str__(self):
        return f"{self.fullname} ({self.library_card_id})"