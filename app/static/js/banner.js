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
        const response = await fetch('/api/news/'); // gọi Django view
        const data = await response.json();

        newsGrid.innerHTML = '';

        if (data.articles.length === 0) {
            newsGrid.innerHTML = '<p>Không có tin tức mới.</p>';
            return;
        }

        data.articles.forEach(news => {
            const card = document.createElement('div');
            card.classList.add('news-card');
            card.innerHTML = `
                <a href="${news.url}" target="_blank">
                    <h4>${news.title}</h4>
                    <p>${news.description || ''}</p>
                </a>
            `;
            newsGrid.appendChild(card);
        });
    } catch (err) {
        console.error(err);
        newsGrid.innerHTML = '<p>Không thể tải tin tức.</p>';
    }
}

loadNews();
