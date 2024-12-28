let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;
const counterCurrent = document.getElementById('current');
const counterTotal = document.getElementById('total');

counterTotal.textContent = totalSlides;

function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.style.transform = `translateX(${(i - index) * 100}%)`;
    });
    currentSlide = index;
    counterCurrent.textContent = currentSlide + 1;
}

function changeSlide(n) {
    currentSlide = (currentSlide + n + totalSlides) % totalSlides;
    showSlide(currentSlide);
}

// Инициализация слайдера
showSlide(currentSlide);
