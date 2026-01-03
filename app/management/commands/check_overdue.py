from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail

from app.models import BorrowRecord, Notification


class Command(BaseCommand):
    help = 'Check overdue borrow records and notify users'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()

        # 👉 DÒNG BẠN HỎI NẰM CHÍNH XÁC Ở ĐÂY
        overdue_records = BorrowRecord.objects.filter(
            status='borrowing',
            due_date__lt=today,
            notified=False
        )

        for record in overdue_records:
            user = record.user
            book = record.book

            # 1️⃣ Lưu notification DB
            Notification.objects.create(
                user=user,
                message=f"Sách '{book.title}' đã quá hạn. Vui lòng trả sách."
            )

            # 2️⃣ Gửi email
            if user.email:
                send_mail(
                    subject='Thông báo quá hạn mượn sách',
                    message=f"Sách '{book.title}' bạn mượn đã quá hạn từ {record.due_date}.",
                    from_email='admin@library.com',
                    recipient_list=[user.email],
                    fail_silently=True
                )

            # 3️⃣ Update trạng thái
            record.status = 'late'
            record.notified = True
            record.save()

        self.stdout.write(
            self.style.SUCCESS(f'Đã xử lý {overdue_records.count()} bản ghi quá hạn')
        )
