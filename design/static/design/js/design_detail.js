document.addEventListener('DOMContentLoaded', function() {
    const toolboxItems = document.querySelectorAll('.toolbox-item');
    const canvas = document.getElementById('garden-canvas');
    let elementCounter = 0;

    // Enable dragging of toolbox items
    toolboxItems.forEach(item => {
        item.addEventListener('dragstart', dragStart);
    });

    // Allow dropping on the canvas
    canvas.addEventListener('dragover', dragOver);
    canvas.addEventListener('drop', dropElement);

    // Handle drag start event
    function dragStart(e) {
        e.dataTransfer.setData('text/plain', e.target.dataset.element);
    }

    // Prevent default behavior to allow drop
    function dragOver(e) {
        e.preventDefault();
    }

    // Handle drop event
    function dropElement(e) {
        e.preventDefault();
        const elementType = e.dataTransfer.getData('text/plain');
        const newElement = document.createElement('div');
        newElement.classList.add('canvas-element', elementType);
        newElement.style.position = 'absolute';
        newElement.style.left = `${e.clientX - canvas.offsetLeft}px`;
        newElement.style.top = `${e.clientY - canvas.offsetTop}px`;
        newElement.textContent = `${elementType} ${++elementCounter}`;

        canvas.appendChild(newElement);
    }

    // Reset canvas
    document.getElementById('reset-canvas').addEventListener('click', function() {
        canvas.innerHTML = '';  // Clear all elements on the canvas
        elementCounter = 0;  // Reset counter
    });

    // Save design (In this example, just alert the user)
    document.getElementById('save-design').addEventListener('click', function() {
        alert('Design saved!');  // Expand to actually save the layout data
    });
});