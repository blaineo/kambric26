/**
 * Header interactivity. Progressive enhancement: without JS, desktop
 * dropdowns still open on hover and every top-level link still navigates.
 *
 * <kg-header-menu>  Desktop disclosure dropdowns (toggle buttons, Escape,
 *                   outside click, focus leaving the item).
 * <kg-mobile-menu>  Opens the native <dialog> menu (focus trap, Escape and
 *                   inert background come from the platform).
 */

class KgHeaderMenu extends HTMLElement {
  connectedCallback() {
    this.items = [...this.querySelectorAll('.site-nav__item--dropdown')];

    this.addEventListener('click', this.onClick);
    this.addEventListener('keydown', this.onKeydown);
    this.addEventListener('focusout', this.onFocusOut);
    this.addEventListener('mouseleave', this.onMouseLeave, true);
    document.addEventListener('click', this.onDocumentClick);
  }

  disconnectedCallback() {
    document.removeEventListener('click', this.onDocumentClick);
  }

  /** @param {HTMLElement} item @param {boolean} open */
  setOpen(item, open) {
    const toggle = item.querySelector('.site-nav__toggle');
    item.toggleAttribute('data-open', open);
    item.removeAttribute('data-closed');
    toggle?.setAttribute('aria-expanded', String(open));
  }

  closeAll(except) {
    for (const item of this.items) {
      if (item !== except && item.hasAttribute('data-open')) this.setOpen(item, false);
    }
  }

  onClick = (event) => {
    const toggle = event.target.closest('.site-nav__toggle');
    if (!toggle) return;
    const item = toggle.closest('.site-nav__item--dropdown');
    const open = !item.hasAttribute('data-open');
    this.closeAll(item);
    this.setOpen(item, open);
  };

  onKeydown = (event) => {
    if (event.key !== 'Escape') return;
    const item = event.target.closest('.site-nav__item--dropdown');
    if (!item) return;
    this.setOpen(item, false);
    // Also hide a hover-opened dropdown until the pointer leaves.
    item.setAttribute('data-closed', '');
    item.querySelector('.site-nav__toggle')?.focus();
  };

  onFocusOut = (event) => {
    const item = event.target.closest('.site-nav__item--dropdown');
    if (item && !item.contains(event.relatedTarget)) this.setOpen(item, false);
  };

  onMouseLeave = (event) => {
    if (event.target.matches?.('.site-nav__item--dropdown')) {
      event.target.removeAttribute('data-closed');
    }
  };

  onDocumentClick = (event) => {
    if (!this.contains(event.target)) this.closeAll();
  };
}

class KgMobileMenu extends HTMLElement {
  connectedCallback() {
    this.dialog = this.querySelector('dialog');
    this.openButton = this.querySelector('[data-mobile-menu-open]');
    this.desktop = window.matchMedia('(min-width: 48rem)');

    this.openButton.addEventListener('click', this.open);
    this.querySelector('[data-mobile-menu-close]').addEventListener('click', this.close);
    this.dialog.addEventListener('close', this.onClose);
    this.desktop.addEventListener('change', this.onBreakpoint);
  }

  disconnectedCallback() {
    this.desktop.removeEventListener('change', this.onBreakpoint);
  }

  open = () => {
    this.dialog.showModal();
    this.openButton.setAttribute('aria-expanded', 'true');
  };

  close = () => this.dialog.close();

  onClose = () => {
    this.openButton.setAttribute('aria-expanded', 'false');
    this.openButton.focus();
  };

  onBreakpoint = (event) => {
    if (event.matches && this.dialog.open) this.close();
  };
}

if (!customElements.get('kg-header-menu')) customElements.define('kg-header-menu', KgHeaderMenu);
if (!customElements.get('kg-mobile-menu')) customElements.define('kg-mobile-menu', KgMobileMenu);
