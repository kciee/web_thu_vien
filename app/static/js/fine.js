
function toggleMenu(id) {
    document.querySelectorAll('.action-menu')
        .forEach(m => m.style.display = 'none');

    const menu = document.getElementById('menu-' + id);
    if (menu) {
        menu.style.display = 'block';
    }
}

window.onclick = function(e) {
    if (!e.target.classList.contains('action-btn')) {
        document.querySelectorAll('.action-menu')
            .forEach(m => m.style.display = 'none');
    }
}