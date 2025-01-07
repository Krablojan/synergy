let currentIndex = 0;
const slides = document.querySelectorAll('.slider-slide');
const totalSlides = slides.length;
const currentSlideText = document.getElementById('current-slide');
const totalSlidesText = document.getElementById('total-slides');

function updateSlider() {
    const slider = document.querySelector('.slider');
    slider.style.transform = `translateX(-${currentIndex * 100}%)`;
    currentSlideText.textContent = currentIndex + 1;
}

function moveSlide(direction) {
    currentIndex += direction;
    
    if (currentIndex >= totalSlides) {
        currentIndex = 0;
    } else if (currentIndex < 0) {
        currentIndex = totalSlides - 1;
    }

    updateSlider();
}

updateSlider();
