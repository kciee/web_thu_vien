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