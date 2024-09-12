document.addEventListener('DOMContentLoaded', function() {
    const toolboxItems = document.querySelectorAll('.toolbox-item');
    const canvas = document.getElementById('garden-canvas');
    let elementCounter = 0;
    const gridSize = 40;  // Match the grid size defined in CSS

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

    // Handle drop event (with grid snapping and resizing for garden beds)
    function dropElement(e) {
        e.preventDefault();
        const elementType = e.dataTransfer.getData('text/plain');
        const newElement = document.createElement('div');
        newElement.classList.add('canvas-element', elementType);

        if (elementType === 'garden-bed') {
            newElement.classList.add('garden-bed');
        }

        newElement.style.position = 'absolute';

        // Calculate the nearest grid position
        const offsetX = e.clientX - canvas.offsetLeft;
        const offsetY = e.clientY - canvas.offsetTop;
        const snapX = Math.round(offsetX / gridSize) * gridSize;
        const snapY = Math.round(offsetY / gridSize) * gridSize;

        newElement.style.left = `${snapX}px`;
        newElement.style.top = `${snapY}px`;
        newElement.textContent = `${elementType.charAt(0).toUpperCase() + elementType.slice(1)} ${++elementCounter}`;

        // Add resizing for the garden bed
        if (elementType === 'garden-bed') {
            newElement.style.width = `${gridSize * 2}px`;  // Default size of 2x2 grid
            newElement.style.height = `${gridSize * 2}px`; // Default size of 2x2 grid
            newElement.addEventListener('mousedown', startResizing);
        }

        canvas.appendChild(newElement);
    }

    // Function to enable dragging of elements on the canvas
    function dragElement(e) {
        e.preventDefault();
        const element = e.target;
        let startX = e.clientX;
        let startY = e.clientY;
        let initialLeft = parseInt(element.style.left);
        let initialTop = parseInt(element.style.top);

        function moveElement(e) {
            const deltaX = e.clientX - startX;
            const deltaY = e.clientY - startY;
            const newLeft = Math.round((initialLeft + deltaX) / gridSize) * gridSize;
            const newTop = Math.round((initialTop + deltaY) / gridSize) * gridSize;
            element.style.left = `${newLeft}px`;
            element.style.top = `${newTop}px`;
        }

        function stopDragging() {
            window.removeEventListener('mousemove', moveElement);
            window.removeEventListener('mouseup', stopDragging);

            // Save the move action for undo
            undoStack.push({
                action: 'move',
                element: element,
                oldLeft: initialLeft,
                oldTop: initialTop,
                newLeft: element.style.left,
                newTop: element.style.top
            });
            redoStack.length = 0;  // Clear the redo stack
        }

        window.addEventListener('mousemove', moveElement);
        window.addEventListener('mouseup', stopDragging);
    }

    // Function to handle resizing
    function startResizing(e) {
        const element = e.target;
        let initialX = e.clientX;
        let initialY = e.clientY;
        let initialWidth = element.offsetWidth;
        let initialHeight = element.offsetHeight;

        function resizeElement(e) {
            const newWidth = Math.round((initialWidth + (e.clientX - initialX)) / gridSize) * gridSize;
            const newHeight = Math.round((initialHeight + (e.clientY - initialY)) / gridSize) * gridSize;
            element.style.width = `${newWidth}px`;
            element.style.height = `${newHeight}px`;
        }

        function stopResizing() {
            window.removeEventListener('mousemove', resizeElement);
            window.removeEventListener('mouseup', stopResizing);
        }

        window.addEventListener('mousemove', resizeElement);
        window.addEventListener('mouseup', stopResizing);
    }

    // Function to delete an element from the canvas
    function deleteElement(e) {
        e.preventDefault();
        const element = e.target;

        // Save the delete action for undo
        undoStack.push({
            action: 'delete',
            element: element,
            left: element.style.left,
            top: element.style.top,
            width: element.style.width,
            height: element.style.height
        });
        redoStack.length = 0;  // Clear the redo stack

        element.remove();  // Delete the element from the canvas
    }

    // Undo the last action
    document.getElementById('undo').addEventListener('click', function() {
        if (undoStack.length > 0) {
            const lastAction = undoStack.pop();
            redoStack.push(lastAction);

            switch (lastAction.action) {
                case 'add':
                    lastAction.element.remove();
                    break;
                case 'move':
                    lastAction.element.style.left = lastAction.oldLeft + 'px';
                    lastAction.element.style.top = lastAction.oldTop + 'px';
                    break;
                case 'resize':
                    lastAction.element.style.width = lastAction.oldWidth + 'px';
                    lastAction.element.style.height = lastAction.oldHeight + 'px';
                    break;
                case 'delete':
                    canvas.appendChild(lastAction.element);
                    lastAction.element.style.left = lastAction.left;
                    lastAction.element.style.top = lastAction.top;
                    lastAction.element.style.width = lastAction.width;
                    lastAction.element.style.height = lastAction.height;
                    break;
            }
        }
    });

    // Redo the last undone action
    document.getElementById('redo').addEventListener('click', function() {
        if (redoStack.length > 0) {
            const lastUndo = redoStack.pop();
            undoStack.push(lastUndo);

            switch (lastUndo.action) {
                case 'add':
                    canvas.appendChild(lastUndo.element);
                    break;
                case 'move':
                    lastUndo.element.style.left = lastUndo.newLeft;
                    lastUndo.element.style.top = lastUndo.newTop;
                    break;
                case 'resize':
                    lastUndo.element.style.width = lastUndo.newWidth;
                    lastUndo.element.style.height = lastUndo.newHeight;
                    break;
                case 'delete':
                    lastUndo.element.remove();
                    break;
            }
        }
    });

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