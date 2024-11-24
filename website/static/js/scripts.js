// Initialize all dropdowns
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all dropdowns
    const dropdownButtons = document.querySelectorAll('[data-dropdown-toggle]');
    dropdownButtons.forEach(button => {
        const targetId = button.getAttribute('data-dropdown-toggle');
        const target = document.getElementById(targetId);
        
        if (button && target) {
            const dropdown = new Dropdown(target, button);
            
            // Close dropdown when clicking outside
            document.addEventListener('click', function(event) {
                if (!button.contains(event.target) && !target.contains(event.target)) {
                    dropdown.hide();
                }
            });
        }
    });
});
