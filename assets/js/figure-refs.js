// Automatic figure reference numbering
// This script populates figure references with the actual figure numbers from CSS counters

document.addEventListener('DOMContentLoaded', function() {
    // Create a mapping of figure IDs to their numbers
    const figureNumbers = {};
    
    // Get ALL figures (with or without IDs) to match CSS counter behavior
    const allFigures = document.querySelectorAll('figure');
    
    allFigures.forEach((figure, index) => {
        // The CSS counter starts at 1, so figure number is index + 1
        const figureNumber = index + 1;
        const figureId = figure.getAttribute('id');
        
        // Only store figures that have IDs
        if (figureId) {
            figureNumbers[figureId] = figureNumber;
        }
    });
    
    // Update all figure references
    const figRefs = document.querySelectorAll('a.fig-ref[data-figref]');
    
    figRefs.forEach(ref => {
        const targetId = ref.getAttribute('data-figref');
        const figureNumber = figureNumbers[targetId];
        
        if (figureNumber) {
            ref.textContent = 'Figure ' + figureNumber;
        } else {
            // If figure not found, show a placeholder
            ref.textContent = 'Figure ?';
            console.warn('Figure reference not found:', targetId);
        }
    });
});

