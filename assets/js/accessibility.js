(() => {
  const managedTabIndex = 'data-scroll-focus-managed';

  function updateScrollableCodeBlocks() {
    document.querySelectorAll('pre').forEach((block) => {
      const isHorizontallyScrollable = block.scrollWidth > block.clientWidth + 1;

      if (isHorizontallyScrollable && !block.hasAttribute('tabindex')) {
        block.setAttribute('tabindex', '0');
        block.setAttribute(managedTabIndex, 'true');
      } else if (!isHorizontallyScrollable && block.hasAttribute(managedTabIndex)) {
        block.removeAttribute('tabindex');
        block.removeAttribute(managedTabIndex);
      }
    });
  }

  function makeMathReferencesAccessible(root = document) {
    const containers = [];

    if (root.nodeType === Node.ELEMENT_NODE && root.matches('mjx-container')) {
      containers.push(root);
    }

    if (root.querySelectorAll) {
      containers.push(...root.querySelectorAll('mjx-container'));
    }

    containers.forEach((container) => {
      if (container.dataset.referenceAccessible === 'true') return;

      const reference = container.querySelector(
        'mjx-math[aria-hidden="true"] a[href]'
      );
      if (!reference) return;

      reference.setAttribute('tabindex', '-1');

      const referenceText =
        container.querySelector('mjx-assistive-mml mtext')?.textContent?.trim();
      container.setAttribute('role', 'link');
      container.setAttribute(
        'aria-label',
        referenceText ? `Equation ${referenceText}` : 'Equation reference'
      );
      container.dataset.referenceAccessible = 'true';

      container.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          reference.click();
        }
      });
    });
  }

  function normalizeFootnoteRoles() {
    document.querySelectorAll('sup[role="doc-noteref"]').forEach((reference) => {
      reference.removeAttribute('role');
      reference.querySelector('a[href]')?.setAttribute('role', 'doc-noteref');
    });

    document.querySelectorAll('[role="doc-endnote"]').forEach((footnote) => {
      footnote.removeAttribute('role');
    });
  }

  function initializeAccessibilityEnhancements() {
    updateScrollableCodeBlocks();
    makeMathReferencesAccessible();
    normalizeFootnoteRoles();

    const observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        mutation.addedNodes.forEach((node) => {
          if (node.nodeType === Node.ELEMENT_NODE) {
            makeMathReferencesAccessible(node);
          }
        });
      });
    });

    observer.observe(document.body, { childList: true, subtree: true });
    window.addEventListener('load', updateScrollableCodeBlocks, { once: true });
    window.addEventListener('resize', updateScrollableCodeBlocks);
  }

  if (document.readyState === 'loading') {
    document.addEventListener(
      'DOMContentLoaded',
      initializeAccessibilityEnhancements,
      { once: true }
    );
  } else {
    initializeAccessibilityEnhancements();
  }
})();
