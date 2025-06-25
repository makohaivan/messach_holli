document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    const submitBtn = form.querySelector('button[type="submit"]');
    const loading = form.querySelector('.loading');
    const errorMessage = form.querySelector('.error-message');
    const sentMessage = form.querySelector('.sent-message');
    
    // Show loading, hide other messages
    loading.classList.remove('d-none');
    errorMessage.classList.add('d-none');
    sentMessage.classList.add('d-none');
    submitBtn.disabled = true;
    
    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            sentMessage.classList.remove('d-none');
            form.reset();
        } else {
            errorMessage.textContent = data.message;
            errorMessage.classList.remove('d-none');
        }
    })
    .catch(error => {
        errorMessage.textContent = 'An error occurred. Please try again.';
        errorMessage.classList.remove('d-none');
    })
    .finally(() => {
        loading.classList.add('d-none');
        submitBtn.disabled = false;
    });
});