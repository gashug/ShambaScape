// Placeholder for any interactivity on the design list page
document.addEventListener('DOMContentLoaded', function() {
    // Example: Handle hover effects or interactivity here
    const designItems = document.querySelectorAll('.design-list li');

    designItems.forEach(item => {
        item.addEventListener('mouseover', function() {
            item.style.backgroundColor = '#e0f7fa';  // Highlight item on hover
        });

        item.addEventListener('mouseout', function() {
            item.style.backgroundColor = '';  // Reset background color
        });
    });
});