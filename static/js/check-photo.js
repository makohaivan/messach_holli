document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.portfolio-filters li');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filterValue = this.getAttribute('data-filter');
            const filteredItems = document.querySelectorAll(filterValue !== '*' ? 
                `.portfolio-item${filterValue}` : '.portfolio-item');
            
            // Check if any items are visible
            const visibleItems = Array.from(filteredItems).filter(item => 
                item.style.display !== 'none');
                
            const noItemsMessage = document.getElementById('no-photos-message');
            if (noItemsMessage) noItemsMessage.remove();
            
            if (visibleItems.length === 0) {
                const container = document.querySelector('.isotope-container');
                const message = document.createElement('div');
                message.id = 'no-photos-message';
                message.className = 'col-12 text-center py-5';
                message.innerHTML = `<p class="text-muted">No photos yet in this category.</p>`;
                container.appendChild(message);
            }
        });
    });
});