// Smooth scroll for internal links (e.g., navigation links)
document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('a[href^="#"]');  // Select all internal links with href starting with '#'

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();  // Prevent default anchor click behavior
            const targetId = this.getAttribute('href').substring(1);  // Get the target ID
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Add hover animation to CTA button
const ctaButton = document.querySelector('.cta-btn');
if (ctaButton) {
    ctaButton.addEventListener('mouseover', function() {
        this.style.transform = 'scale(1.1)';
    });
    ctaButton.addEventListener('mouseout', function() {
        this.style.transform = 'scale(1)';
    });
}