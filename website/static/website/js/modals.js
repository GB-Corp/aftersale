class ModalManager {
    constructor() {
        this.modals = {
            auth: document.getElementById('auth-modal'),
            booking: document.getElementById('book-service-modal'),
            notification: document.getElementById('notification-modal'),
            terms: document.getElementById('terms-modal')
        };
        
        this.setupEventListeners();
    }

    setupEventListeners() {
        // Setup close buttons for all modals
        document.querySelectorAll('.modal-close').forEach(button => {
            button.addEventListener('click', (e) => {
                const modal = e.target.closest('[id$="-modal"]');
                if (modal) {
                    this.hideModal(modal.id);
                }
            });
        });

        // Close modals when clicking outside
        Object.values(this.modals).forEach(modal => {
            if (modal) {
                modal.addEventListener('click', (e) => {
                    if (e.target === modal) {
                        this.hideModal(modal.id);
                    }
                });
            }
        });

        // Handle ESC key to close modals
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.hideAllModals();
            }
        });
    }

    showModal(modalId) {
        const modal = this.modals[modalId] || document.getElementById(modalId);
        if (modal) {
            // Hide all other modals first
            this.hideAllModals();
            
            // Show the requested modal
            modal.classList.remove('hidden');
            
            // Add body class to prevent scrolling
            document.body.classList.add('overflow-hidden');
            
            // Trigger custom event
            const event = new CustomEvent('modalOpened', { detail: { modalId } });
            document.dispatchEvent(event);
        }
    }

    hideModal(modalId) {
        const modal = this.modals[modalId] || document.getElementById(modalId);
        if (modal) {
            modal.classList.add('hidden');
            
            // Remove body class if no other modals are visible
            if (!this.isAnyModalVisible()) {
                document.body.classList.remove('overflow-hidden');
            }
            
            // Trigger custom event
            const event = new CustomEvent('modalClosed', { detail: { modalId } });
            document.dispatchEvent(event);
        }
    }

    hideAllModals() {
        Object.values(this.modals).forEach(modal => {
            if (modal) {
                modal.classList.add('hidden');
            }
        });
        document.body.classList.remove('overflow-hidden');
    }

    isAnyModalVisible() {
        return Object.values(this.modals).some(modal => 
            modal && !modal.classList.contains('hidden')
        );
    }

    // Utility function to check if a specific modal is visible
    isModalVisible(modalId) {
        const modal = this.modals[modalId] || document.getElementById(modalId);
        return modal && !modal.classList.contains('hidden');
    }
}

// Initialize modal manager when the DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    window.modalManager = new ModalManager();
});

// Example usage:
// window.modalManager.showModal('auth');
// window.modalManager.hideModal('auth');
// window.modalManager.hideAllModals();
