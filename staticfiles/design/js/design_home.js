document.addEventListener('DOMContentLoaded', function() {
    let slideIndex = 0;
    const slides = document.querySelectorAll('.carousel-slide');
    const nextButton = document.getElementById('nextSlide');
    const prevButton = document.getElementById('prevSlide');
    const slideInterval = 5000;

    // Show the current slide
    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.style.display = i === index ? 'block' : 'none';
        });
    }

    // Show next slide
    function nextSlide() {
        slideIndex = (slideIndex + 1) % slides.length;
        showSlide(slideIndex);
    }

    // Show previous slide
    function prevSlide() {
        slideIndex = (slideIndex - 1 + slides.length) % slides.length;
        showSlide(slideIndex);
    }

    const autoSlide = setInterval(nextSlide, slideInterval);

    // Initial display
    showSlide(slideIndex);

    // Event listeners for next/previous buttons (allow user control)
    nextButton.addEventListener('click', () => {
        clearInterval(autoSlide);  // Stop auto-slideshow when user interacts
        nextSlide();
    });

    prevButton.addEventListener('click', () => {
        clearInterval(autoSlide);  // Stop auto-slideshow when user interacts
        prevSlide();
    });
});