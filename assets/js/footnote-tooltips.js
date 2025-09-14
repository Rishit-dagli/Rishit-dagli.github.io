document.addEventListener('DOMContentLoaded', function() {
    // Create tooltip element
    const tooltip = document.createElement('div');
    tooltip.className = 'footnote-tooltip';
    document.body.appendChild(tooltip);

    // Find all footnote reference links
    const footnoteRefs = document.querySelectorAll('a[href^="#fn:"]');
    
    footnoteRefs.forEach(function(ref) {
        const footnoteId = ref.getAttribute('href').substring(1); // Remove the '#'
        const footnoteElement = document.getElementById(footnoteId);
        
        if (footnoteElement) {
            // Get the footnote text (exclude the back-reference link)
            let footnoteText = footnoteElement.innerHTML;
            // Remove the back-reference link at the end
            footnoteText = footnoteText.replace(/<a href="#fnref:[^"]*"[^>]*>.*?<\/a>\s*$/, '');
            
            // Add hover event listeners
            ref.addEventListener('mouseenter', function(e) {
                tooltip.innerHTML = footnoteText;
                tooltip.style.display = 'block';
                
                // Store current mouse position for repositioning after MathJax
                const currentEvent = {
                    pageX: e.pageX,
                    pageY: e.pageY
                };
                
                positionTooltip(e, tooltip);
                
                // Render MathJax in tooltip if MathJax is available
                if (window.MathJax && window.MathJax.typesetPromise) {
                    window.MathJax.typesetPromise([tooltip]).then(function () {
                        // Reposition tooltip after MathJax rendering in case size changed
                        positionTooltip(currentEvent, tooltip);
                    }).catch(function (err) {
                        console.log('MathJax typeset failed: ' + err.message);
                    });
                }
            });

            ref.addEventListener('mousemove', function(e) {
                positionTooltip(e, tooltip);
            });

            ref.addEventListener('mouseleave', function() {
                tooltip.style.display = 'none';
            });
        }
    });

    function positionTooltip(event, tooltip) {
        const tooltipRect = tooltip.getBoundingClientRect();
        const windowWidth = window.innerWidth;
        const windowHeight = window.innerHeight;
        
        let left = event.pageX + 10;
        let top = event.pageY + 10;

        // Adjust position if tooltip would go off-screen
        if (left + tooltipRect.width > windowWidth) {
            left = event.pageX - tooltipRect.width - 10;
        }
        
        if (top + tooltipRect.height > windowHeight) {
            top = event.pageY - tooltipRect.height - 10;
        }

        tooltip.style.left = left + 'px';
        tooltip.style.top = top + 'px';
    }
}); 