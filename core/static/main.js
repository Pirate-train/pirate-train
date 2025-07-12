document.addEventListener('DOMContentLoaded', function() {
    // Table row hover effects
    const tableRows = document.querySelectorAll('.data-table tr');
    tableRows.forEach(row => {
        row.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#333';
        });
        row.addEventListener('mouseleave', function() {
            if (this.rowIndex % 2 === 0) {
                this.style.backgroundColor = '#222';
            } else {
                this.style.backgroundColor = '#1a1a1a';
            }
        });
    });
    
    // Game link hover effects
    const gameLinks = document.querySelectorAll('.game-link');
    gameLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#333';
            this.style.paddingLeft = '15px';
        });
        link.addEventListener('mouseleave', function() {
            this.style.backgroundColor = 'transparent';
            this.style.paddingLeft = '8px';
        });
    });
});