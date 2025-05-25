---
layout: page
title: SIGGRAPH Theme Demo
permalink: /theme-demo/
---

Welcome to the SIGGRAPH-inspired theme for your blog! This page demonstrates the beautiful typography and design elements inspired by academic papers.

## Typography Showcase

This theme uses the authentic SIGGRAPH fonts that mirror the professional appearance of academic papers:

- **Headers** use Linux Biolinum for a clean, professional look
- **Body text** uses Linux Libertine for excellent readability
- **Code** uses Fira Code with ligatures for better code presentation

### Text Elements

Here's how different text elements appear:

Regular paragraph text flows beautifully with justified alignment and proper hyphenation, creating a professional academic paper appearance. The line height and spacing have been carefully tuned for optimal readability. The Linux Libertine font provides the classic serif typography that's characteristic of SIGGRAPH papers.

**Bold text** stands out clearly, while *italic text* provides subtle emphasis. You can also use ***bold italic*** for maximum emphasis.

> Blockquotes are styled with a distinctive left border and italic text, perfect for highlighting important quotes or key insights from your research. The Linux Libertine italic variant adds elegance to quoted material.

### Code Examples

Inline code like `const theme = 'siggraph'` blends seamlessly with text.

```javascript
// Code blocks feature syntax highlighting
function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
}
```

### Lists and Structure

Ordered lists:
1. First item with proper spacing
2. Second item maintains consistency
3. Third item completes the set

Unordered lists:
- Clean bullet points
- Consistent spacing
- Professional appearance

### Mathematical Expressions

The theme supports LaTeX math rendering:

Inline math: $E = mc^2$

Display math:
$$
\frac{\partial u}{\partial t} = \alpha \nabla^2 u
$$

### Tables

| Feature | Light Mode | Dark Mode |
|---------|------------|-----------|
| Background | Clean white | Deep black |
| Text | SIGGRAPH blue | Soft white |
| Accents | Deep blue | Bright blue |

### Figures with Automatic Numbering

The theme includes SIGGRAPH-style figure captions with automatic numbering. Here are some examples:

<figure>
  <img src="https://via.placeholder.com/600x400/f9f9f9/000730?text=Example+Figure+1" alt="Example figure">
  <figcaption>This is an example figure with automatic numbering. The caption appears in a subtle gray color, positioned close to the image.</figcaption>
</figure>

You can also use the figure include for more control:

{% include figure.html 
   src="https://via.placeholder.com/600x400/000730/ffffff?text=Example+Figure+2" 
   caption="Another example showing the automatic numbering system. Long captions wrap nicely and maintain proper spacing."
   alt="Second example figure" 
%}

For side-by-side figures, use the `figure-row` class:

<div class="figure-row">
  <figure>
    <img src="https://via.placeholder.com/300x200/f9f9f9/000730?text=Left+Figure" alt="Left figure">
    <figcaption>Left figure in a row</figcaption>
  </figure>
  <figure>
    <img src="https://via.placeholder.com/300x200/f9f9f9/000730?text=Right+Figure" alt="Right figure">
    <figcaption>Right figure in a row</figcaption>
  </figure>
</div>

To reference figures in your text, you can say "as shown in Figure 1" or use a link like <a href="#figure-1" class="fig-ref">Figure 1</a>.

If you need custom numbering or no numbering, add the `no-auto-number` class:

<figure class="no-auto-number">
  <img src="https://via.placeholder.com/600x300/000730/ffffff?text=Unnumbered+Figure" alt="Unnumbered figure">
  <figcaption>This figure has no automatic number prefix.</figcaption>
</figure>

## Theme Features

### 🌓 Dark/Light Mode Toggle

Click the theme toggle button in the navigation bar to switch between light and dark modes. Your preference is saved automatically.

### 📱 Responsive Design

The theme adapts beautifully to all screen sizes, from mobile phones to large desktop displays.

### 🎨 SIGGRAPH-Inspired Design

The color palette and typography are carefully chosen to reflect the professional aesthetic of SIGGRAPH academic publications while maintaining excellent readability.

### ⚡ Performance Optimized

- Fast loading times with local font files
- Minimal JavaScript
- Efficient CSS with custom properties
- Print-friendly styles

## Getting Started

To customize this theme further:

1. Edit the CSS variables in `/assets/css/main.css`
2. Modify the layouts in `/_layouts/`
3. Adjust the navigation in `/_includes/header.html`

Enjoy your new SIGGRAPH-inspired blog theme with authentic Linux Libertine and Biolinum fonts! 