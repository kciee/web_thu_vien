let currentSlide = 0;

document.addEventListener("DOMContentLoaded", () => {
    const slides = document.querySelectorAll(".slide");
    const dots = document.querySelectorAll(".dot");

    function showSlide(index) {
        slides.forEach(slide => slide.classList.remove("active"));
        dots.forEach(dot => dot.classList.remove("active"));

        slides[index].classList.add("active");
        dots[index].classList.add("active");
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }

    // Tự động chạy mỗi 4 giây
    setInterval(nextSlide, 4000);

    // Click dot
    dots.forEach((dot, index) => {
        dot.addEventListener("click", () => {
            currentSlide = index;
            showSlide(currentSlide);
        });
    });
});

const newsGrid = document.getElementById('news-grid');

async function loadNews() {
    try {
        const response = await fetch('/api/news/');
        const data = await response.json();

        newsGrid.innerHTML = '';

        if (!data.articles || data.articles.length === 0) {
            newsGrid.innerHTML = '<p>Không có tin tức mới.</p>';
            return;
        }

        data.articles.forEach(news => {
            const div = document.createElement('div');
            div.className = 'news-row';

            div.innerHTML = `
                <a href="${news.url}" target="_blank" class="news-link">
                    <img class="news-image" 
                         src="${news.image || 'https://via.placeholder.com/120'}" 
                         alt="">
                    <div class="news-text">
                        <h4>${news.title}</h4>
                    </div>
                </a>
            `;

            newsGrid.appendChild(div);
        });

    } catch (e) {
        console.error("JS ERROR:", e);
        newsGrid.innerHTML = '<p>Không thể tải tin tức.</p>';
    }
}

document.addEventListener("DOMContentLoaded", loadNews);


document.querySelectorAll('.book-card').forEach(card => {
    card.addEventListener('click', () => {

        // Lấy dữ liệu từ data-*
        const title = card.dataset.title;
        const image = card.dataset.image;
        const authors = card.dataset.authors;
        const status = card.dataset.status;
        const description = card.dataset.description;

        // Gán vào modal
        document.getElementById('modalTitle').innerText = title;
        document.getElementById('modalImage').src = image;
        document.getElementById('modalAuthors').innerText = authors;
        document.getElementById('modalStatus').innerText = status;
        document.getElementById('modalDescription').innerText = description;

        // Hiện modal
        document.getElementById('bookModal').style.display = 'flex';
    });
});

// Đóng modal
document.getElementById('closeModal').addEventListener('click', () => {
    document.getElementById('bookModal').style.display = 'none';
});

// Click ra ngoài để đóng
document.getElementById('bookModal').addEventListener('click', (e) => {
    if (e.target.id === 'bookModal') {
        document.getElementById('bookModal').style.display = 'none';
    }
});

