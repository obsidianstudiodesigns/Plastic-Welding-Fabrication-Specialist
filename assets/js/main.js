(function () {
  'use strict';

  var WHATSAPP = '27734688916';
  var header = document.querySelector('[data-header]');
  var hero = document.querySelector('.hero');
  var dock = document.querySelector('[data-dock]');
  var contact = document.getElementById('contact');

  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Header turns solid once the hero photo has scrolled under it; the phone dock shows between hero and contact.
  if ('IntersectionObserver' in window && hero) {
    var heroVisible = true;
    var contactVisible = false;
    var sync = function () {
      if (dock) dock.classList.toggle('is-shown', !heroVisible && !contactVisible);
    };
    new IntersectionObserver(function (entries) {
      header.classList.toggle('is-solid', !entries[0].isIntersecting);
    }, { rootMargin: '-72px 0px 0px 0px', threshold: 0 }).observe(document.querySelector('.hero-inner'));
    new IntersectionObserver(function (entries) {
      heroVisible = entries[0].isIntersecting;
      sync();
    }, { threshold: 0.15 }).observe(hero);
    if (contact) {
      new IntersectionObserver(function (entries) {
        contactVisible = entries[0].isIntersecting;
        sync();
      }, { threshold: 0 }).observe(contact);
    }
  } else if (header) {
    header.classList.add('is-solid');
  }

  // Mobile menu
  var menuBtn = document.querySelector('[data-menu]');
  var nav = document.getElementById('nav');
  function closeMenu() {
    header.classList.remove('menu-open');
    if (menuBtn) menuBtn.setAttribute('aria-expanded', 'false');
  }
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      var open = header.classList.toggle('menu-open');
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) closeMenu(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeMenu(); });
  }

  // Welding methods: one open at a time; on desktop the photo beside the list follows the open method.
  var list = document.querySelector('[data-methods]');
  if (list) {
    var items = Array.prototype.slice.call(list.querySelectorAll('.method'));
    var stage = document.querySelectorAll('[data-stage]');
    var canHover = window.matchMedia('(hover: hover) and (min-width: 901px)');
    var activate = function (item) {
      items.forEach(function (it) {
        var on = it === item;
        it.classList.toggle('is-active', on);
        it.querySelector('.method-head').setAttribute('aria-expanded', on ? 'true' : 'false');
      });
      stage.forEach(function (img) { img.classList.toggle('is-active', img.getAttribute('data-stage') === item.getAttribute('data-method')); });
    };
    items.forEach(function (item) {
      var head = item.querySelector('.method-head');
      head.addEventListener('click', function () { activate(item); });
      head.addEventListener('mouseenter', function () { if (canHover.matches) activate(item); });
    });
  }

  // Enquiry form: writes the job details into a WhatsApp message. Nothing is sent to or stored on the website.
  var form = document.querySelector('[data-enquiry]');
  if (form) {
    var showError = function (field, show) {
      var err = document.getElementById(field.id + '-err');
      field.setAttribute('aria-invalid', show ? 'true' : 'false');
      if (err) {
        err.hidden = !show;
        if (show) field.setAttribute('aria-describedby', err.id); else field.removeAttribute('aria-describedby');
      }
    };
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = form.elements.name;
      var work = form.elements.work;
      var bad = [];
      showError(name, !name.value.trim());
      if (!name.value.trim()) bad.push(name);
      showError(work, !work.value);
      if (!work.value) bad.push(work);
      if (bad.length) { bad[0].focus(); return; }

      var date = form.elements.date.value;
      if (date) {
        var d = new Date(date + 'T00:00:00');
        date = d.toLocaleDateString('en-ZA', { day: 'numeric', month: 'long', year: 'numeric' });
      }
      var lines = ['Hi Lloyd, I found your website and have a job enquiry.', ''];
      lines.push('Name: ' + name.value.trim());
      if (form.elements.company.value.trim()) lines.push('Company: ' + form.elements.company.value.trim());
      lines.push('Work: ' + work.value);
      if (form.elements.site.value.trim()) lines.push('Site: ' + form.elements.site.value.trim());
      if (date) lines.push('Start date: ' + date);
      if (form.elements.details.value.trim()) lines.push('', form.elements.details.value.trim());
      window.open('https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(lines.join('\n')), '_blank', 'noopener');
    });
    ['name', 'work'].forEach(function (n) {
      var f = form.elements[n];
      f.addEventListener(n === 'work' ? 'change' : 'input', function () {
        if (f.getAttribute('aria-invalid') === 'true' && f.value.trim()) showError(f, false);
      });
    });
  }
})();
