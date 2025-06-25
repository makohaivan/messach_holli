document.addEventListener('DOMContentLoaded', function() {
    // Get all elements
    const filterButtons = document.querySelectorAll('.portfolio-filters li');
    const portfolioItems = document.querySelectorAll('.portfolio-item');
    
    // Filter function
    function filterPortfolio(filterValue) {
        portfolioItems.forEach(item => {
            if (filterValue === '*' || item.classList.contains(filterValue.replace('.', ''))) {
                item.style.display = 'block';
                setTimeout(() => {
                    item.style.opacity = '1';
                    item.style.transform = 'scale(1)';
                }, 50);
            } else {
                item.style.opacity = '0';
                item.style.transform = 'scale(0.95)';
                setTimeout(() => {
                    item.style.display = 'none';
                }, 300);
            }
        });
    }
    
    // Add click events to buttons
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Update active button
            document.querySelector('.portfolio-filters .filter-active').classList.remove('filter-active');
            this.classList.add('filter-active');
            
            // Filter items
            const filterValue = this.getAttribute('data-filter');
            filterPortfolio(filterValue);
            
            // Update URL
            window.history.pushState(null, null, 
                filterValue === '*' ? '#' : `#${filterValue.replace('.filter-', '')}`);
        });
    });
    
    // Check URL hash on load
    const hash = window.location.hash.substring(1);
    if (hash) {
        const initialButton = document.querySelector(`[data-filter=".filter-${hash}"]`);
        if (initialButton) initialButton.click();
    } else {
        // Initialize with all items visible
        filterPortfolio('*');
    }
});