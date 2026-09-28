// Turns Kramdown footnotes into sidenotes. On wide screens each note sits in
// the right margin beside its reference; on narrow screens the reference
// number expands the note inline. The footnote list stays as the fallback.
(() => {
  // Must match the sidenote breakpoint in main.css.
  const wideLayout = window.matchMedia('(min-width: 1280px)');
  // Citations of one footnote closer than this many characters of text share
  // a single margin note.
  const repeatDistance = 400;

  function buildNote(footnote, number, id) {
    const note = document.createElement('span');
    note.className = 'sidenote';
    note.id = id;
    note.setAttribute('role', 'note');

    const label = document.createElement('span');
    label.className = 'sidenote-number';
    label.setAttribute('aria-hidden', 'true');
    label.textContent = number;
    note.append(label);

    const copy = footnote.cloneNode(true);
    copy.querySelectorAll('.reversefootnote').forEach((backlink) => backlink.remove());
    copy.querySelectorAll('[id]').forEach((element) => element.removeAttribute('id'));

    // Notes sit inside paragraphs, so paragraphs become spans that run on
    // from the number.
    Array.from(copy.childNodes).forEach((node) => {
      if (node.nodeName === 'P') {
        const paragraph = document.createElement('span');
        paragraph.className = 'sidenote-paragraph';
        paragraph.append(...node.childNodes);
        note.append(paragraph);
      } else if (node.nodeType === Node.ELEMENT_NODE || node.textContent.trim()) {
        note.append(node);
      }
    });

    return note;
  }

  function initializeSidenotes() {
    const content = document.querySelector('.post-content');
    if (!content) return;

    const entries = [];
    const latestEntries = new Map();
    content.querySelectorAll('sup[id^="fnref:"] > a[href^="#fn:"]').forEach((link) => {
      const footnote = document.getElementById(link.getAttribute('href').slice(1));
      if (!footnote || link.closest('.footnotes')) return;

      const entry = { link, footnote };
      entry.marginEntry = entry;
      const previous = latestEntries.get(footnote);
      if (previous) {
        const between = document.createRange();
        between.setStartAfter(previous.marginEntry.link);
        between.setEndBefore(link);
        if (between.toString().length < repeatDistance) entry.marginEntry = previous.marginEntry;
      }
      latestEntries.set(footnote, entry);
      entries.push(entry);
    });
    if (!entries.length) return;

    entries.forEach((entry, index) => {
      const { link } = entry;
      entry.note = buildNote(entry.footnote, link.textContent.trim(), `sidenote-${index + 1}`);
      entry.note.classList.toggle('is-repeat', entry.marginEntry !== entry);
      link.parentElement.after(entry.note);
      link.setAttribute('aria-controls', entry.note.id);
    });

    entries.forEach(({ link, note, marginEntry }) => {
      const marginNote = marginEntry.note;
      const highlight = (on) => {
        const active = on && wideLayout.matches;
        link.classList.toggle('is-highlighted', active);
        marginNote.classList.toggle('is-highlighted', active);
      };

      [link, marginNote].forEach((element) => {
        element.addEventListener('mouseenter', () => highlight(true));
        element.addEventListener('mouseleave', () => highlight(false));
      });
      link.addEventListener('focus', () => highlight(true));
      link.addEventListener('blur', () => highlight(false));

      link.addEventListener('click', (event) => {
        event.preventDefault();
        if (wideLayout.matches) {
          marginNote.scrollIntoView({ block: 'nearest' });
          return;
        }
        note.classList.toggle('is-open');
        syncLayout();
      });
    });

    // A note floats against its paragraph's right edge; notes inside padded
    // boxes (theorems, remarks) need that padding added to reach the margin.
    function alignToColumn() {
      const columnRight = content.getBoundingClientRect().right;
      entries.forEach(({ note }) => {
        let block = note.parentElement;
        while (block !== content && getComputedStyle(block).display === 'inline') {
          block = block.parentElement;
        }
        const style = getComputedStyle(block);
        const inset = columnRight - block.getBoundingClientRect().right
          + parseFloat(style.paddingRight) + parseFloat(style.borderRightWidth);
        if (inset > 0.5) {
          note.style.setProperty('--sidenote-inset', `${inset}px`);
        } else {
          note.style.removeProperty('--sidenote-inset');
        }
      });
    }

    function syncLayout() {
      entries.forEach(({ link, note }) => {
        if (wideLayout.matches) {
          link.removeAttribute('aria-expanded');
        } else {
          link.setAttribute('aria-expanded', String(note.classList.contains('is-open')));
        }
      });
      if (wideLayout.matches) alignToColumn();
    }

    syncLayout();
    wideLayout.addEventListener('change', syncLayout);

    // MathJax may already be mid-typeset; make sure the copied math renders.
    const { MathJax } = window;
    if (MathJax && MathJax.startup && MathJax.startup.promise && MathJax.typesetPromise) {
      MathJax.startup.promise = MathJax.startup.promise
        .then(() => MathJax.typesetPromise(entries.map(({ note }) => note)))
        .catch((error) => console.warn('Sidenote typesetting failed:', error));
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeSidenotes, { once: true });
  } else {
    initializeSidenotes();
  }
})();
