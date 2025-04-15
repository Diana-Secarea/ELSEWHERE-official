/**
 * ELSEWHERE Website - Main JavaScript
 */

document.addEventListener('DOMContentLoaded', function() {
    // Add classes to character cards for hover effects
    const characterCards = document.querySelectorAll('.group > a > div');
    characterCards.forEach(card => {
        card.classList.add('character-card');
    });

    // Add animation class to buttons
    const buttons = document.querySelectorAll('button, .btn');
    buttons.forEach(button => {
        button.classList.add('btn-hover-expand');
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Form submission handling (prevent default and show success message)
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // In a real application, you would handle form submission via AJAX
            // For this demo, we'll just show a success message
            const submitButton = form.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;
            
            submitButton.textContent = 'Submitting...';
            submitButton.disabled = true;
            
            // Simulate API call
            setTimeout(() => {
                const formContainer = form.parentElement;
                form.style.display = 'none';
                
                // Create success message
                const successMessage = document.createElement('div');
                successMessage.className = 'text-center py-8';
                successMessage.innerHTML = `
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 mx-auto text-green-500 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <h3 class="text-2xl font-bold mb-2">Thank You!</h3>
                    <p class="text-gray-600">Your message has been received. We'll get back to you shortly.</p>
                    <button class="mt-6 px-6 py-2 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 transition-colors">
                        Close
                    </button>
                `;
                
                formContainer.appendChild(successMessage);
                
                // Add event listener to close button
                const closeButton = successMessage.querySelector('button');
                closeButton.addEventListener('click', () => {
                    successMessage.remove();
                    form.style.display = 'block';
                    submitButton.textContent = originalText;
                    submitButton.disabled = false;
                    form.reset();
                });
            }, 1500);
        });
    });
}); 