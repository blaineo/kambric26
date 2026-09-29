/**
 * <kg-promo-popup> — site-wide newsletter pop-up (Phase 5, D-11).
 *
 * Opens the native <dialog> N seconds after load, unless
 * `localStorage.kambric_promo_dismissed` is set or another <dialog> is
 * open (mobile menu, search, notify-me). Storage access is best-effort:
 * if it throws, the pop-up still shows, it just can't remember dismissal.
 *
 * Submits via fetch with the same captcha/network fallback as
 * <kg-back-in-stock> (component-back-in-stock.js).
 *
 * In the editor (`data-design-mode="true"`) the delay timer never starts;
 * the dialog only opens while this section is selected in the sidebar
 * (`shopify:section:select` / `:deselect`), so it never interrupts editing
 * elsewhere. Select/deselect never counts as a dismissal — only Esc, the
 * backdrop, the close button or a successful sign-up do.
 */
const DISMISS_KEY = 'kambric_promo_dismissed';

class KgPromoPopup extends HTMLElement {
  connectedCallback() {
    this.dialog = this.querySelector('dialog');
    this.form = this.querySelector('form');
    if (!this.dialog || !this.form) return;

    this.errorEl = this.querySelector('[data-promo-popup-error]');
    this.formView = this.querySelector('[data-promo-popup-view="form"]');
    this.successView = this.querySelector('[data-promo-popup-view="success"]');
    this.submitButton = this.form.querySelector('[type="submit"]');
    this.emailInput = this.form.querySelector('input[name="contact[email]"]');
    this.mediaEl = this.querySelector('[data-promo-popup-media]');
    this.imageTemplate = this.querySelector('[data-promo-popup-image-template]');

    this.delaySeconds = Number(this.dataset.delaySeconds) || 0;
    this.designMode = this.dataset.designMode === 'true';
    this.sectionId = this.dataset.sectionId || '';
    this.returnFocusEl = null;
    this.openTimer = null;
    this.retryTimer = null;
    this.suppressDismissOnClose = false;

    this.form.addEventListener('submit', this.onSubmit);
    this.addEventListener('click', this.onClick);
    this.dialog.addEventListener('click', this.onDialogClick);
    this.dialog.addEventListener('close', this.onClose);

    if (this.designMode) {
      document.addEventListener('shopify:section:select', this.onSectionSelect);
      document.addEventListener('shopify:section:deselect', this.onSectionDeselect);
    } else {
      this.scheduleOpen();
    }
  }

  disconnectedCallback() {
    if (this.openTimer) window.clearTimeout(this.openTimer);
    if (this.retryTimer) window.clearTimeout(this.retryTimer);
    document.removeEventListener('shopify:section:select', this.onSectionSelect);
    document.removeEventListener('shopify:section:deselect', this.onSectionDeselect);
  }

  isDismissed() {
    try {
      return window.localStorage.getItem(DISMISS_KEY) === '1';
    } catch {
      return false; // storage unavailable — show anyway, just can't remember it
    }
  }

  persistDismissed() {
    try {
      window.localStorage.setItem(DISMISS_KEY, '1');
    } catch {
      // best effort only
    }
  }

  scheduleOpen() {
    if (this.isDismissed()) return;
    this.openTimer = window.setTimeout(this.tryOpen, Math.max(0, this.delaySeconds) * 1000);
  }

  // Native <dialog> only supports one modal at a time in practice (a second
  // showModal() would still work, but stacking two is bad UX); defer to
  // whichever dialog is already open and retry shortly after.
  tryOpen = () => {
    if (this.dialog.open || this.isDismissed()) return;
    const otherDialogOpen = [...document.querySelectorAll('dialog[open]')].some(
      (dialog) => dialog !== this.dialog
    );
    if (otherDialogOpen) {
      this.retryTimer = window.setTimeout(this.tryOpen, 1000);
      return;
    }
    this.open();
  };

  open() {
    this.mountImage();
    this.returnFocusEl = document.activeElement;
    this.dialog.showModal();
    this.emailInput?.focus();
  }

  // The <picture> lives in a <template> (inert, no request) until the
  // pop-up actually opens, so a visitor who never sees it never pays for
  // the image download, and it never competes with the page's LCP image.
  mountImage() {
    if (!this.imageTemplate || !this.mediaEl || this.mediaEl.childElementCount > 0) return;
    this.mediaEl.appendChild(this.imageTemplate.content.cloneNode(true));
    this.mediaEl.hidden = false;
  }

  onSectionSelect = (event) => {
    if (event.detail?.sectionId !== this.sectionId) return;
    if (this.openTimer) window.clearTimeout(this.openTimer);
    if (this.retryTimer) window.clearTimeout(this.retryTimer);
    if (!this.dialog.open) this.open();
  };

  onSectionDeselect = (event) => {
    if (event.detail?.sectionId !== this.sectionId) return;
    if (this.dialog.open) {
      this.suppressDismissOnClose = true;
      this.dialog.close();
    }
  };

  onClick = (event) => {
    if (event.target.closest('[data-promo-popup-close]')) this.dialog.close();
  };

  // Native <dialog> doesn't close on a backdrop click by default; a click
  // that lands on the dialog element itself (not its content) is a click
  // on the backdrop area.
  onDialogClick = (event) => {
    if (event.target === this.dialog) this.dialog.close();
  };

  onClose = () => {
    if (this.suppressDismissOnClose) {
      this.suppressDismissOnClose = false;
    } else {
      this.persistDismissed();
    }
    this.returnFocusEl?.focus();
  };

  onSubmit = async (event) => {
    event.preventDefault();
    if (this.form.getAttribute('aria-busy') === 'true') return;

    this.form.setAttribute('aria-busy', 'true');
    if (this.submitButton) this.submitButton.disabled = true;
    if (this.errorEl) this.errorEl.setAttribute('hidden', '');

    const formData = new FormData(this.form);

    try {
      const response = await fetch(this.form.action, {
        method: 'POST',
        body: formData,
      });

      if (response.redirected && /\/challenge(\/|$|\?)/.test(new URL(response.url).pathname + '/')) {
        // Shopify wants the shopper to clear a captcha challenge; only a
        // real, top-level submission can render/solve it.
        this.form.submit();
        return;
      }

      if (!response.ok) throw new Error(`Newsletter signup failed: ${response.status}`);

      this.formView?.setAttribute('hidden', '');
      this.successView?.removeAttribute('hidden');
      this.form.removeAttribute('aria-busy');
      if (this.emailInput) this.emailInput.value = '';
      this.persistDismissed();
      this.successView?.focus();
    } catch (error) {
      if (error instanceof TypeError) {
        // Network failure: fall back to a real submission so the shopper
        // can still complete it.
        this.form.submit();
        return;
      }
      this.form.removeAttribute('aria-busy');
      if (this.submitButton) this.submitButton.disabled = false;
      if (this.errorEl) this.errorEl.removeAttribute('hidden');
    }
  };
}

if (!customElements.get('kg-promo-popup')) customElements.define('kg-promo-popup', KgPromoPopup);
