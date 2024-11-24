// Initialize Flowbite dropdowns
document.addEventListener('DOMContentLoaded', function() {
    const initDropdown = (button, options = {}) => {
        const targetId = button.getAttribute('data-dropdown-toggle');
        const target = document.getElementById(targetId);
        if (target) {
            new Dropdown(target, button, {
                placement: button.getAttribute('data-dropdown-placement') || 'bottom',
                offsetSkidding: 0,
                offsetDistance: 10,
                delay: 0,
                onShow: () => {
                    target.classList.remove('opacity-0', 'translate-y-1');
                    target.classList.add('opacity-100', 'translate-y-0');
                    button.setAttribute('aria-expanded', 'true');
                },
                onHide: () => {
                    target.classList.add('opacity-0', 'translate-y-1');
                    target.classList.remove('opacity-100', 'translate-y-0');
                    button.setAttribute('aria-expanded', 'false');
                },
                ...options
            });
        }
    };

    // Add transition classes to all dropdown menus
    document.querySelectorAll('[data-dropdown-toggle]').forEach(button => {
        const targetId = button.getAttribute('data-dropdown-toggle');
        const target = document.getElementById(targetId);
        if (target) {
            target.classList.add('transition-all', 'duration-200', 'ease-out', 'transform', 'opacity-0', 'translate-y-1');
        }
    });

    // Initialize all dropdowns
    document.querySelectorAll('[data-dropdown-toggle]').forEach(button => {
        initDropdown(button);
    });
});
