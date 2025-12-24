const btnAdd = document.getElementById('btnAdd');
const modal = document.getElementById('addModal');
const btnClose = document.getElementById('btnClose');

btnAdd.onclick = () => {
    modal.style.display = 'flex';
};

btnClose.onclick = () => {
    modal.style.display = 'none';
};

window.onclick = (e) => {
    if (e.target === modal) {
        modal.style.display = 'none';
    }
};
