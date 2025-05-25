// Theme toggle functionality
(function() {
  // Check for saved theme preference or default to 'light'
  const currentTheme = localStorage.getItem('theme') || 'light';
  
  // Apply the saved theme on page load
  document.documentElement.setAttribute('data-theme', currentTheme);
  
  // Wait for DOM to be ready
  document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const sunIcon = document.getElementById('sun-icon');
    const moonIcon = document.getElementById('moon-icon');
    
    // Update icon visibility based on current theme
    function updateIcons(theme) {
      if (theme === 'dark') {
        sunIcon.style.display = 'block';
        moonIcon.style.display = 'none';
      } else {
        sunIcon.style.display = 'none';
        moonIcon.style.display = 'block';
      }
    }
    
    // Set initial icon state
    updateIcons(currentTheme);
    
    // Toggle theme on button click
    themeToggle.addEventListener('click', function() {
      const currentTheme = document.documentElement.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      
      // Update theme
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      
      // Update icons
      updateIcons(newTheme);
      
      // Add transition class for smooth color changes
      document.body.style.transition = 'background-color 0.3s ease, color 0.3s ease';
    });
    
    // Listen for system theme changes
    if (window.matchMedia) {
      const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
      
      // Check if user hasn't set a preference
      if (!localStorage.getItem('theme')) {
        const systemTheme = mediaQuery.matches ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', systemTheme);
        updateIcons(systemTheme);
      }
      
      // Listen for changes
      mediaQuery.addEventListener('change', function(e) {
        // Only update if user hasn't set a preference
        if (!localStorage.getItem('theme')) {
          const systemTheme = e.matches ? 'dark' : 'light';
          document.documentElement.setAttribute('data-theme', systemTheme);
          updateIcons(systemTheme);
        }
      });
    }
  });
})(); 