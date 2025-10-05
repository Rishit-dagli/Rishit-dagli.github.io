// Collapsible Table of Contents functionality
(function() {
  // Wait for DOM to be ready
  document.addEventListener('DOMContentLoaded', function() {
    const tocToggle = document.getElementById('toc-toggle');
    const tocContent = document.getElementById('toc-content');
    
    // Only proceed if TOC elements exist
    if (!tocToggle || !tocContent) {
      return;
    }
    
    // Toggle TOC visibility
    function toggleTOC() {
      const isExpanded = tocToggle.getAttribute('aria-expanded') === 'true';
      const newState = !isExpanded;

      tocToggle.setAttribute('aria-expanded', newState.toString());
      tocContent.setAttribute('aria-hidden', (!newState).toString());

      // If expanding, set height to fit content; if collapsing, set to 0
      if (newState) {
        // Temporarily set height to 'auto' to measure, then set explicit height for transition if needed
        tocContent.style.maxHeight = 'none';
      } else {
        tocContent.style.maxHeight = '0px';
      }

      const icon = tocToggle.querySelector('.toc-toggle-icon');
      if (icon) {
        icon.style.transform = newState ? 'rotate(180deg)' : 'rotate(0deg)';
      }

      localStorage.setItem('toc-expanded', newState.toString());
    }
    
    // Restore TOC state from localStorage
    function restoreTOCState() {
      const savedState = localStorage.getItem('toc-expanded');
      if (savedState === 'true') {
        tocToggle.setAttribute('aria-expanded', 'true');
        tocContent.setAttribute('aria-hidden', 'false');
        tocContent.style.maxHeight = 'none';
        const icon = tocToggle.querySelector('.toc-toggle-icon');
        if (icon) {
          icon.style.transform = 'rotate(180deg)';
        }
      } else {
        tocContent.style.maxHeight = '0px';
      }
    }
    
    // Add click event listener
    tocToggle.addEventListener('click', toggleTOC);
    
    // Add keyboard support
    tocToggle.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        toggleTOC();
      }
    });
    
    // Restore state on page load
    restoreTOCState();
    
    // Smooth scroll for TOC links
    const tocLinks = tocContent.querySelectorAll('a[href^="#"]');
    tocLinks.forEach(link => {
      link.addEventListener('click', function(e) {
        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        
        if (targetElement) {
          e.preventDefault();
          targetElement.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
          
          // Close TOC after clicking a link (optional)
          // toggleTOC();
        }
      });
    });
  });
})();
