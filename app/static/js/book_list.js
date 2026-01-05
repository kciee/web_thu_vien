function toggleMenu(id) {
    document.querySelectorAll('.action-menu')
        .forEach(m => m.style.display = 'none');

    const menu = document.getElementById('menu-' + id);
    if (menu) menu.style.display = 'block';
}

/* ================= CHI TIẾT ================= */
function openDetail(el) {
    const title = el.dataset.title;
    const description = el.dataset.description;

    document.getElementById("detailTitle").value = title;
    document.getElementById("detailDesc").value = description;

    document.getElementById("detailModal").style.display = "flex";
}

function closeDetail() {
    document.getElementById('detailModal').style.display = 'none';
}

/* ================= MƯỢN SÁCH (ĐÃ SỬA) ================= */
function openBorrow(bookId) {
    const modal = document.getElementById('borrowModal');
    modal.style.display = 'flex';

    document.getElementById('borrowBookId').value = bookId;

    const today = new Date();

    // ===== Ngày mượn = hôm nay =====
    const borrowDate = today.toISOString().split('T')[0];
    const borrowInput = document.getElementById('borrowDate');
    borrowInput.value = borrowDate;
    borrowInput.readOnly = true;

    // ===== Ngày trả: từ +1 → +7 =====
    const minReturn = new Date(today);
    minReturn.setDate(today.getDate() + 1);

    const maxReturn = new Date(today);
    maxReturn.setDate(today.getDate() + 7);

    const returnInput = document.getElementById('returnDate');
    returnInput.min = minReturn.toISOString().split('T')[0];
    returnInput.max = maxReturn.toISOString().split('T')[0];

    // mặc định chọn +7 ngày
    returnInput.value = returnInput.max;
}

function closeBorrow() {
    document.getElementById('borrowModal').style.display = 'none';
}

/* ================= CLICK NGOÀI MODAL ================= */
window.onclick = function (e) {
    if (e.target.classList.contains('modal')) {
        e.target.style.display = 'none';
    }
}

/* ================= REVIEW ================= */
function openReview(bookId, title) {
    document.getElementById('reviewModal').style.display = 'flex';
    document.getElementById('reviewBookTitle').innerText = 'Đánh giá: ' + title;
    document.getElementById('reviewBookId').value = bookId;

    document.querySelectorAll('.reviews')
        .forEach(r => r.style.display = 'none');

    const reviewBox = document.getElementById('reviews-' + bookId);
    if (reviewBox) reviewBox.style.display = 'block';

    document.getElementById('reviewForm').action = `/books/${bookId}/review/`;
}

function closeReview() {
    document.getElementById('reviewModal').style.display = 'none';
}
