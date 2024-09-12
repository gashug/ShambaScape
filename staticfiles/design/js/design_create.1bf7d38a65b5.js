// design_create.js

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {

    // Get form elements
    const designForm = document.querySelector('form');
    const designNameInput = document.getElementById('name');
    const descriptionInput = document.getElementById('description');

    // Handle form submission
    designForm.addEventListener('submit', function(event) {
        // Simple form validation to check if the design name is entered
        if (designNameInput.value.trim() === '') {
            alert('Please enter a design name.');
            event.preventDefault();  // Prevent form submission
        }
    });

    // Example of dynamic features you can add
    designNameInput.addEventListener('input', function() {
        if (designNameInput.value.length > 50) {
            alert('Design name should be less than 50 characters');
        }
    });

    descriptionInput.addEventListener('input', function() {
        if (descriptionInput.value.length > 300) {
            alert('Description should be less than 300 characters.');
        }
    });

});