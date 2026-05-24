(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    var sidebar  = document.querySelector('.sidebar-toc');
    if (!sidebar) return;

    var header   = document.querySelector('.site-header');
    var footer   = document.querySelector('.site-footer');
    var postBody = document.querySelector('.post-content');
    var headings = postBody
      ? Array.from(postBody.querySelectorAll('h2,h3,h4,h5,h6'))
      : [];
    var tocLinks = Array.from(sidebar.querySelectorAll('a[href^="#"]'));
    var rafPending = false;

    // Track the previous active state so we can clear it cheaply
    var prevActiveLink  = null;
    var prevActiveLis   = [];   // all <li>s that had toc-section-active

    // ── Geometry: clamp sidebar between header bottom and footer top ────────

    function repositionSidebar() {
      if (window.innerWidth < 1200) return;
      var headerBottom = header ? header.getBoundingClientRect().bottom : 0;
      var footerTop    = footer ? footer.getBoundingClientRect().top : window.innerHeight;
      var gap = 20;
      sidebar.style.top       = (headerBottom + gap) + 'px';
      sidebar.style.maxHeight = Math.max(60, footerTop - headerBottom - gap * 2) + 'px';
    }

    // ── Find the heading we are currently inside ────────────────────────────

    function getCurrentHeading() {
      var headerH     = header ? header.offsetHeight : 0;
      var triggerLine = window.scrollY + headerH + 32;
      var active      = null;
      for (var i = 0; i < headings.length; i++) {
        if (headings[i].getBoundingClientRect().top + window.scrollY <= triggerLine) {
          active = headings[i];
        } else {
          break;
        }
      }
      return active;
    }

    // ── Collect every <li> ancestor of an element inside the toc-list ───────

    function ancestorLis(el) {
      var lis = [];
      var node = el ? el.parentElement : null;
      while (node && !node.classList.contains('toc-list')) {
        if (node.tagName === 'LI') lis.push(node);
        node = node.parentElement;
      }
      // Include the root <li> when the toc-list itself is reached
      if (node && node.classList.contains('toc-list') && node.parentElement) {
        var rootLi = node.parentElement;
        if (rootLi && rootLi.tagName === 'LI') lis.push(rootLi);
      }
      return lis;
    }

    // ── Update active link highlight + recursive section expansion ──────────

    function updateActive() {
      var heading = getCurrentHeading();
      var newLink = (heading && heading.id)
        ? sidebar.querySelector('a[href="#' + heading.id + '"]')
        : null;

      // Nothing changed — skip DOM work
      if (newLink === prevActiveLink) return;

      // --- Clear previous state ---
      if (prevActiveLink) prevActiveLink.classList.remove('toc-active');
      prevActiveLis.forEach(function (li) { li.classList.remove('toc-section-active'); });

      prevActiveLink = newLink;
      prevActiveLis  = [];

      if (!newLink) return;

      // --- Apply new state ---
      newLink.classList.add('toc-active');

      // Walk up from the active link and mark every ancestor <li>; this
      // recursively expands the correct sub-list at every nesting level.
      var node = newLink.parentElement;
      while (node && node !== sidebar) {
        if (node.tagName === 'LI') {
          node.classList.add('toc-section-active');
          prevActiveLis.push(node);
        }
        node = node.parentElement;
      }

      // Scroll sidebar so the active link stays in view
      var lTop = newLink.offsetTop;
      var lBot = lTop + newLink.offsetHeight;
      var sbTop = sidebar.scrollTop;
      var sbH   = sidebar.clientHeight;
      if (lTop < sbTop + 8)            sidebar.scrollTop = lTop - 8;
      else if (lBot > sbTop + sbH - 8) sidebar.scrollTop = lBot - sbH + 8;
    }

    // ── Smooth scroll on TOC link click ────────────────────────────────────

    tocLinks.forEach(function (link) {
      link.addEventListener('click', function (e) {
        var target = document.getElementById(link.getAttribute('href').slice(1));
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });

    // ── Event wiring ────────────────────────────────────────────────────────

    function onFrame() {
      repositionSidebar();
      updateActive();
      rafPending = false;
    }

    function onScroll() {
      if (!rafPending) {
        rafPending = true;
        requestAnimationFrame(onFrame);
      }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', repositionSidebar);

    repositionSidebar();
    updateActive();
  });
})();
