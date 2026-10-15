(function () {
  'use strict';

  const root = document.documentElement;
  const desktop = window.matchMedia('(min-width: 925px)'); // Matches $large.
  const navigationDesktop = window.matchMedia('(min-width: 1280px)'); // Matches $x-large; reserves the original logo width.
  const disclosures = [];

  function listenToMedia(query, callback) {
    if (query.addEventListener) query.addEventListener('change', callback);
    else query.addListener(callback);
  }

  function disclosure(container, toggleSelector, desktopQuery = desktop) {
    if (!container) return null;
    const toggle = container.querySelector(toggleSelector);
    const panel = document.getElementById(toggle.getAttribute('aria-controls'));
    let expanded = false;

    function setOpen(open, restoreFocus) {
      expanded = open && !desktopQuery.matches;
      panel.hidden = !desktopQuery.matches && !expanded;
      toggle.hidden = desktopQuery.matches;
      toggle.setAttribute('aria-expanded', String(expanded));
      if (toggle.dataset.openLabel) {
        toggle.setAttribute('aria-label', expanded ? toggle.dataset.closeLabel : toggle.dataset.openLabel);
      }
      if (restoreFocus && !toggle.hidden) toggle.focus({ preventScroll: true });
    }

    const control = { container, toggle, panel, setOpen, isOpen: () => expanded };
    disclosures.push(control);
    container.dataset.enhanced = 'true';
    toggle.addEventListener('click', function () {
      disclosures.forEach(other => { if (other !== control) other.setOpen(false); });
      setOpen(!expanded);
    });
    container.addEventListener('click', function (event) {
      const link = event.target.closest('a');
      if (link && !link.hasAttribute('data-dialog-open')) setOpen(false);
    });
    listenToMedia(desktopQuery, function () {
      const active = document.activeElement;
      if (!desktopQuery.matches && panel.contains(active)) toggle.focus({ preventScroll: true });
      if (desktopQuery.matches && active === toggle) panel.querySelector('a')?.focus({ preventScroll: true });
      setOpen(false);
    });
    setOpen(false);
    return control;
  }

  const navigation = disclosure(document.getElementById('site-nav'), '.site-nav__toggle', navigationDesktop);
  const contacts = disclosure(document.querySelector('.author__urls-wrapper'), '.author__contact-toggle');

  document.addEventListener('click', function (event) {
    if (event.target.closest('dialog')) return;
    disclosures.forEach(control => {
      if (!control.container.contains(event.target)) control.setOpen(false);
    });
  });

  document.addEventListener('keydown', function (event) {
    if (event.key !== 'Escape' || document.querySelector('dialog[open]')) return;
    disclosures.forEach(control => {
      if (control.isOpen()) {
        event.preventDefault();
        control.setOpen(false, true);
      }
    });
  });

  const masthead = document.querySelector('.masthead');
  function measureMasthead() {
    if (masthead) root.style.setProperty('--masthead-height', Math.ceil(masthead.getBoundingClientRect().height) + 'px');
  }
  if (window.ResizeObserver && masthead) new ResizeObserver(measureMasthead).observe(masthead);
  else window.addEventListener('resize', measureMasthead);
  measureMasthead();

  const themeToggle = document.getElementById('theme-toggle');
  const themeIcon = document.getElementById('theme-icon');
  const preferredTheme = window.matchMedia('(prefers-color-scheme: dark)');

  function savedTheme() {
    try { return localStorage.getItem('theme'); } catch (error) { return null; }
  }

  function applyTheme(theme) {
    const dark = theme === 'dark';
    root.setAttribute('data-theme', dark ? 'dark' : 'light');
    if (themeToggle) {
      themeToggle.setAttribute('aria-pressed', String(dark));
      themeToggle.setAttribute('aria-label', dark ? themeToggle.dataset.lightLabel : themeToggle.dataset.darkLabel);
      themeToggle.title = themeToggle.getAttribute('aria-label');
    }
    if (themeIcon) {
      themeIcon.classList.toggle('fa-sun', dark);
      themeIcon.classList.toggle('fa-moon', !dark);
    }
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.content = getComputedStyle(root).getPropertyValue('--global-bg-color').trim();
  }

  applyTheme(root.getAttribute('data-theme'));
  themeToggle?.addEventListener('click', function () {
    const theme = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('theme', theme); } catch (error) {}
    applyTheme(theme);
    disclosures.forEach(control => control.setOpen(false));
  });
  listenToMedia(preferredTheme, function () {
    const saved = savedTheme();
    if (saved !== 'light' && saved !== 'dark') applyTheme(preferredTheme.matches ? 'dark' : 'light');
  });

  function markCurrentLink() {
    document.querySelectorAll('#site-nav a[href]').forEach(link => {
      const url = new URL(link.href);
      link.removeAttribute('aria-current');
      if (url.origin !== location.origin || url.pathname !== location.pathname) return;
      if (url.hash && url.hash === location.hash) link.setAttribute('aria-current', 'location');
      else if (!url.hash && !location.hash) link.setAttribute('aria-current', 'page');
    });
  }
  markCurrentLink();
  window.addEventListener('hashchange', markCurrentLink);
  navigation?.container.addEventListener('click', function (event) {
    const link = event.target.closest('a[href]');
    if (!link) return;
    const url = new URL(link.href);
    if (url.origin !== location.origin || url.pathname !== location.pathname || !url.hash) return;
    const target = document.getElementById(decodeURIComponent(url.hash.slice(1)));
    if (target) {
      if (!target.hasAttribute('tabindex')) target.setAttribute('tabindex', '-1');
      requestAnimationFrame(() => target.focus({ preventScroll: true }));
    }
  });

  const returnFocus = new WeakMap();
  function openDialog(dialog, trigger) {
    if (!dialog || !dialog.showModal || dialog.open) return false;
    returnFocus.set(dialog, trigger);
    dialog.showModal();
    document.body.classList.add('modal-open');
    return true;
  }

  document.querySelectorAll('dialog').forEach(dialog => {
    dialog.querySelectorAll('[data-dialog-close]').forEach(button => {
      button.addEventListener('click', () => dialog.close());
    });
    dialog.addEventListener('click', function (event) {
      const box = dialog.getBoundingClientRect();
      if (event.target === dialog && (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom)) {
        dialog.close();
      }
    });
    dialog.addEventListener('keydown', function (event) {
      if (event.key !== 'Tab') return;
      const focusable = Array.from(dialog.querySelectorAll('a[href], button:not([disabled]), [tabindex="0"]'))
        .filter(element => !element.hidden && element.getClientRects().length);
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (!first) return;
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    });
    dialog.addEventListener('close', function () {
      if (!document.querySelector('dialog[open]')) document.body.classList.remove('modal-open');
      const trigger = returnFocus.get(dialog);
      if (trigger?.getClientRects().length) trigger.focus({ preventScroll: true });
      else if (trigger && contacts?.panel.contains(trigger)) contacts.toggle.focus({ preventScroll: true });
      returnFocus.delete(dialog);
    });
  });

  document.querySelectorAll('[data-dialog-open]').forEach(trigger => {
    trigger.addEventListener('click', function (event) {
      if (event.button || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      if (openDialog(document.getElementById(trigger.dataset.dialogOpen), trigger)) event.preventDefault();
    });
  });

  const preview = document.getElementById('media-preview');
  if (preview) {
    const viewport = preview.querySelector('.media-preview__viewport');
    const image = preview.querySelector('.media-preview__image');
    const zoom = preview.querySelector('.media-preview__zoom');

    function setZoom(enlarged) {
      preview.classList.toggle('is-zoomed', enlarged);
      zoom.setAttribute('aria-pressed', String(enlarged));
      zoom.textContent = enlarged ? zoom.dataset.fitLabel : zoom.dataset.zoomLabel;
      viewport.scrollTo(0, 0);
    }
    zoom.addEventListener('click', function () {
      const enlarged = !preview.classList.contains('is-zoomed');
      setZoom(enlarged);
      if (enlarged) viewport.focus({ preventScroll: true });
    });
    document.querySelectorAll('.project-media a').forEach(link => {
      const thumbnail = link.querySelector('img');
      if (!thumbnail) return;
      link.setAttribute('aria-haspopup', 'dialog');
      link.setAttribute('aria-controls', 'media-preview');
      link.setAttribute('aria-label', preview.dataset.previewLabel + ': ' + thumbnail.alt);
      link.title = preview.dataset.previewLabel;
      link.addEventListener('click', function (event) {
        if (event.button || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || !preview.showModal) return;
        image.src = link.href;
        image.alt = thumbnail.alt;
        preview.querySelector('#media-preview-title').textContent = link.closest('figure').querySelector('figcaption')?.textContent || preview.dataset.previewLabel;
        preview.querySelector('.media-preview__original').href = link.href;
        setZoom(false);
        if (openDialog(preview, link)) event.preventDefault();
      });
    });
  }

  document.querySelectorAll('.page__content table').forEach(table => {
    const wrapper = document.createElement('div');
    wrapper.className = 'table-scroll';
    wrapper.setAttribute('role', 'region');
    wrapper.setAttribute('aria-label', root.lang === 'zh-CN' ? '可横向滚动的表格' : 'Scrollable table');
    table.before(wrapper);
    wrapper.append(table);
    function updateTableFocus() { wrapper.tabIndex = wrapper.scrollWidth > wrapper.clientWidth ? 0 : -1; }
    updateTableFocus();
    if (window.ResizeObserver) new ResizeObserver(updateTableFocus).observe(wrapper);
    else window.addEventListener('resize', updateTableFocus);
  });

  // Preserve existing video fitting and non-project image previews.
  if (window.fitvids) window.fitvids();
  if (window.jQuery && window.jQuery.fn.magnificPopup) {
    window.jQuery('a[href$=".jpg"], a[href$=".jpeg"], a[href$=".JPG"], a[href$=".png"], a[href$=".gif"]')
      .filter(function () { return !this.closest('.project-media') && !this.hasAttribute('data-dialog-open'); })
      .magnificPopup({
        type: 'image',
        gallery: { enabled: true, navigateByImgClick: true },
        image: { tError: '<a href="%url%">Image</a> could not be loaded.' },
        closeOnContentClick: true,
        midClick: true
      });
  }
}());
