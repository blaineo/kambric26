/**
 * Cart page (sections/main-cart.liquid).
 *
 * <kg-cart> enhances the native cart form (which works without JS):
 * - quantity −/+ and typed changes → /cart/change.js
 * - remove → /cart/update.js with every key in `data-remove` set to 0, so a
 *   monogrammed garment and its fee line go in one atomic request (D-9)
 * - orphan fee lines (`data-orphan-fee`) are removed on load
 * Each request asks for this section and the header (Section Rendering API)
 * and swaps both, announces the result and restores focus.
 */

/** { key: 0, … } for a comma-separated key list. */
export function zeroUpdates(keys) {
  return Object.fromEntries(keys.filter(Boolean).map((key) => [key, 0]));
}

/** Clamp a typed quantity to a whole number ≥ 0 (null when not a number). */
export function parseQuantity(value) {
  const n = Number.parseInt(value, 10);
  return Number.isNaN(n) ? null : Math.max(0, n);
}

class KgCart extends HTMLElement {
  connectedCallback() {
    this.addEventListener('click', this);
    this.addEventListener('change', this);
    this.addEventListener('submit', this);
    const orphans = [...this.querySelectorAll('[data-orphan-fee]')].map((el) => el.dataset.orphanFee);
    if (orphans.length) this.request('update', { updates: zeroUpdates(orphans) }, { silent: true });
  }

  get body() {
    return this.querySelector('[data-cart-body]');
  }

  handleEvent(event) {
    const { type, target } = event;
    if (type === 'submit') {
      // Checkout posts natively. Anything else (Enter in a quantity field) is handled here.
      if (this.pending) event.preventDefault();
      else if (event.submitter?.name !== 'checkout') {
        event.preventDefault();
        if (target.matches?.('form') && document.activeElement?.matches('[data-quantity]')) {
          this.changeQuantity(document.activeElement);
        }
      }
      return;
    }
    if (type === 'change' && target.matches('[data-quantity]')) return this.changeQuantity(target);
    if (type !== 'click') return;

    const step = target.closest('[data-step]');
    if (step) {
      const input = this.querySelector(`[data-quantity][data-key="${CSS.escape(step.dataset.key)}"]`);
      const qty = Math.max(0, (parseQuantity(input.value) ?? 0) + Number(step.dataset.step));
      input.value = qty;
      return this.changeQuantity(input, `[data-step="${step.dataset.step}"][data-key="${CSS.escape(step.dataset.key)}"]`);
    }

    const remove = target.closest('[data-remove]');
    if (remove) {
      event.preventDefault();
      const keys = remove.dataset.remove.split(',');
      this.request('update', { updates: zeroUpdates(keys) }, { removedKey: keys[0] });
    }
  }

  changeQuantity(input, focusSelector) {
    const quantity = parseQuantity(input.value);
    if (quantity === null) {
      input.value = input.defaultValue;
      return;
    }
    if (String(quantity) === input.defaultValue) return;
    const key = input.dataset.key;
    this.request(
      'change',
      { id: key, quantity },
      quantity === 0
        ? { removedKey: key }
        : { focusSelector: focusSelector || `[data-quantity][data-key="${CSS.escape(key)}"]`, revert: input }
    );
  }

  async request(kind, body, { removedKey, focusSelector, revert, silent } = {}) {
    if (this.pending) return;
    this.pending = true;
    const lines = [...this.querySelectorAll('[data-line-key]')];
    const removedIndex = lines.findIndex((line) => line.dataset.lineKey === removedKey);
    const headerId = document.querySelector('.site-header')?.closest('.shopify-section')?.id.replace('shopify-section-', '');
    const sections = [this.dataset.sectionId, headerId].filter(Boolean);
    const error = this.querySelector('[data-cart-error]');
    error.hidden = true;
    const disabled = this.setBusy();

    try {
      const url = this.dataset[kind === 'change' ? 'changeUrl' : 'updateUrl'];
      const response = await fetch(`${url}.js`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({ ...body, sections, sections_url: location.pathname }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.description || data.message || '');
      if (!this.render(data.sections)) return location.reload();
      this.updateHeader(data.sections?.[headerId]);
      if (silent) return;
      this.announce(this.dataset[removedKey ? 'msgRemoved' : 'msgUpdated']);
      this.restoreFocus(removedKey ? removedIndex : -1, focusSelector);
    } catch (err) {
      disabled.forEach((el) => (el.disabled = false));
      this.body.removeAttribute('aria-busy');
      if (revert) revert.value = revert.defaultValue;
      if (silent) return;
      error.textContent = err.message || this.dataset.msgError;
      error.hidden = false;
    } finally {
      this.pending = false;
    }
  }

  /** Disable the controls while a request is in flight; returns what was disabled. */
  setBusy() {
    this.body.setAttribute('aria-busy', 'true');
    const controls = [...this.body.querySelectorAll('button:not(:disabled), input:not(:disabled)')];
    controls.forEach((el) => (el.disabled = true));
    return controls;
  }

  /** Swap the cart body with the freshly rendered section. */
  render(sections) {
    const html = sections?.[this.dataset.sectionId];
    if (!html) return false;
    const fresh = new DOMParser().parseFromString(html, 'text/html').querySelector('[data-cart-body]');
    if (!fresh) return false;
    this.body.replaceWith(fresh);
    return true;
  }

  /** Header cart links (icon count + label, mobile menu), same approach as <kg-product>. */
  updateHeader(html) {
    if (!html) return;
    const selector = `.site-header a[href="${this.dataset.cartUrl}"]`;
    const fresh = new DOMParser().parseFromString(html, 'text/html').querySelectorAll(selector);
    document.querySelectorAll(selector).forEach((link, i) => {
      if (fresh[i]) link.replaceChildren(...fresh[i].childNodes);
    });
  }

  announce(message) {
    const status = this.querySelector('[data-cart-status]');
    status.textContent = '';
    requestAnimationFrame(() => (status.textContent = message));
  }

  /** After a removal: the next line (or the previous, or the heading). Otherwise the same control. */
  restoreFocus(removedIndex, focusSelector) {
    let target = focusSelector && this.querySelector(focusSelector);
    if (!target && removedIndex >= 0) {
      const lines = this.querySelectorAll('[data-line-key]');
      const line = lines[Math.min(removedIndex, lines.length - 1)];
      target = line?.querySelector('.cart-line__title');
    }
    if (!target && removedIndex >= 0) target = this.querySelector('h1');
    target?.focus();
  }
}

if (typeof customElements !== 'undefined' && !customElements.get('kg-cart')) {
  customElements.define('kg-cart', KgCart);
}
