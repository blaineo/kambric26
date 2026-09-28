/**
 * <kg-back-in-stock> — the "Notify me when it's back" dialog.
 *
 * Listens on `document` for `kg:notify-request` (dispatched by the product
 * page when a sold-out size/colorway is chosen), fills the contact form's
 * hidden fields and visible summary, and opens the native <dialog>
 * (focus trap, Escape and the inert background all come from
 * `showModal()`).
 *
 * Submits via fetch so the page doesn't reload. Falls back to a real form
 * submission when the request fails outright (network error) or when
 * Shopify serves a captcha challenge page, so the shopper can still
 * complete it.
 */
class KgBackInStock extends HTMLElement {
  connectedCallback() {
    this.dialog = this.querySelector('dialog');
    this.form = this.querySelector('form');
    if (!this.dialog || !this.form) return;

    this.formView = this.querySelector('[data-back-in-stock-view="form"]');
    this.successView = this.querySelector('[data-back-in-stock-view="success"]');
    this.summaryEls = this.querySelectorAll(
      '[data-back-in-stock-summary], [data-back-in-stock-summary-success]'
    );
    this.errorEl = this.querySelector('[data-back-in-stock-error]');
    this.submitButton = this.form.querySelector('[type="submit"]');
    this.emailInput = this.form.querySelector('input[name="contact[email]"]');
    this.defaultProductTitle = this.dataset.productTitle || '';
    this.defaultProductUrl = this.dataset.productUrl || '';
    this.returnFocusEl = null;

    document.addEventListener('kg:notify-request', this.onRequest);
    this.form.addEventListener('submit', this.onSubmit);
    this.addEventListener('click', this.onClick);
    this.dialog.addEventListener('click', this.onDialogClick);
    this.dialog.addEventListener('close', this.onClose);

    // Graceful no-JS-network-failure fallback: a real (non-fetch) form
    // submission just reloaded this page. If it landed us in the success
    // view or with a field marked invalid, surface that result.
    const hasResult =
      (this.successView && !this.successView.hasAttribute('hidden')) ||
      this.form.querySelector('[aria-invalid="true"]');
    if (hasResult) this.dialog.showModal();
  }

  disconnectedCallback() {
    document.removeEventListener('kg:notify-request', this.onRequest);
  }

  onRequest = (event) => {
    const detail = event.detail || {};
    const productTitle = detail.productTitle || this.defaultProductTitle;
    const productUrl = detail.productUrl || this.defaultProductUrl;
    const { print, size, variantId } = detail;

    this.setField('product', productTitle);
    this.setField('print', print || '');
    this.setField('size', size || '');
    this.setField('variant-id', variantId || '');
    this.setField('product-url', productUrl || '');
    this.setField('body', this.composeBody({ productTitle, productUrl, print, size, variantId }));

    const summary = this.composeSummary({ productTitle, print, size });
    this.summaryEls.forEach((el) => {
      el.textContent = summary;
    });

    this.resetState();
    this.returnFocusEl = document.activeElement;
    this.dialog.showModal();
    this.emailInput?.focus();
  };

  setField(name, value) {
    const field = this.form.querySelector(`[data-back-in-stock-field="${name}"]`);
    if (field) field.value = value;
  }

  composeSummary({ productTitle, print, size }) {
    let summary = productTitle || '';
    if (print) summary += ` — ${print}`;
    if (size) summary += `, size ${size}`;
    return summary;
  }

  composeBody({ productTitle, productUrl, print, size, variantId }) {
    const lines = [`Please notify me when ${productTitle} is back in stock.`];
    if (print) lines.push(`Print: ${print}`);
    if (size) lines.push(`Size: ${size}`);
    if (variantId) lines.push(`Variant ID: ${variantId}`);
    if (productUrl) lines.push(`Product URL: ${productUrl}`);
    return lines.join('\n');
  }

  resetState() {
    this.form.removeAttribute('aria-busy');
    this.formView?.removeAttribute('hidden');
    this.successView?.setAttribute('hidden', '');
    if (this.errorEl) this.errorEl.setAttribute('hidden', '');
    if (this.submitButton) this.submitButton.disabled = false;
    if (this.emailInput) this.emailInput.value = '';
  }

  onClick = (event) => {
    if (event.target.closest('[data-back-in-stock-close]')) this.dialog.close();
  };

  // Native <dialog> doesn't close on a backdrop click by default; a click
  // that lands on the dialog element itself (not its content) is a click
  // on the backdrop area.
  onDialogClick = (event) => {
    if (event.target === this.dialog) this.dialog.close();
  };

  onClose = () => {
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

      if (!response.ok) throw new Error(`Contact form request failed: ${response.status}`);

      this.formView?.setAttribute('hidden', '');
      this.successView?.removeAttribute('hidden');
      this.form.removeAttribute('aria-busy');
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

if (!customElements.get('kg-back-in-stock')) customElements.define('kg-back-in-stock', KgBackInStock);
