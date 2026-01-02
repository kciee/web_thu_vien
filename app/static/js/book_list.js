 function toggleMenu(id) {
        document.querySelectorAll('.action-menu')
            .forEach(m => m.style.display = 'none');
        const menu = document.getElementById('menu-' + id);
        menu.style.display = 'block';
    }

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

    function openBorrow(id) {
        document.getElementById('borrowBookId').value = id;
        document.getElementById('borrowModal').style.display = 'flex';
    }

    function closeBorrow() {
        document.getElementById('borrowModal').style.display = 'none';
    }

    window.onclick = function (e) {
        if (e.target.classList.contains('modal')) {
            e.target.style.display = 'none';
        }
    }
    function openReview(bookId, title) {
    document.getElementById('reviewModal').style.display = 'flex';
    document.getElementById('reviewBookTitle').innerText = 'Đánh giá: ' + title;
    document.getElementById('reviewBookId').value = bookId;

    // Ẩn tất cả review
    document.querySelectorAll('.reviews').forEach(r => r.style.display = 'none');

    // Hiện review đúng sách
    const reviewBox = document.getElementById('reviews-' + bookId);
    if (reviewBox) reviewBox.style.display = 'block';

    // Set action form
    document.getElementById('reviewForm').action = `/books/${bookId}/review/`;
}

function closeReview() {
    document.getElementById('reviewModal').style.display = 'none';
}
