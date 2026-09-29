/**
 * <kg-search> — predictive search overlay (D-15).
 *
 * Opens on [data-search-open], or the header's `a[href="/search"]` inside
 * `.site-header__icons` (header.liquid stays unedited — without JS that
 * link just navigates to /search).
 *
 * Debounces input (~200ms), fetches predictive-search.liquid via the
 * Section Rendering API, aborts a stale request with AbortController.
 * Combobox pattern: input role="combobox" (aria-expanded/-controls/
 * -activedescendant); results role="listbox"/"option" (options baked into
 * the fetched markup). Arrow keys move the active option; Enter opens it,
 * or falls through to the form's native GET submit. Escape/the dialog's
 * `close` event return focus to whatever opened the overlay.
 */
const DEBOUNCE_MS = 200;
const MAX_RESULTS = 8;

class KgSearch extends HTMLElement {
  connectedCallback() {
    this.dialog = this.querySelector('dialog');
    this.form = this.querySelector('[data-search-form]');
    this.input = this.querySelector('[data-search-input]');
    this.resultsEl = this.querySelector('[data-search-results]');
    if (!this.dialog || !this.form || !this.input || !this.resultsEl) return;

    this.predictiveUrl = this.dataset.predictiveSearchUrl;
    this.noResultsTemplate = this.dataset.noResultsTemplate || '';
    this.options = [];
    this.activeIndex = -1;
    this.debounceTimer = null;
    this.controller = null;
    this.returnFocusEl = null;

    document.addEventListener('click', this.onDocumentClick);
    this.querySelector('[data-search-close]')?.addEventListener('click', () => this.close());
    this.dialog.addEventListener('click', this.onBackdropClick);
    this.dialog.addEventListener('close', this.onClose);
    this.input.addEventListener('input', this.onInput);
    this.input.addEventListener('keydown', this.onKeydown);
  }

  disconnectedCallback() {
    document.removeEventListener('click', this.onDocumentClick);
  }

  onDocumentClick = (event) => {
    const opener = event.target.closest(
      '[data-search-open], .site-header__icons a[href="/search"]'
    );
    if (!opener || this.contains(opener)) return;
    event.preventDefault();
    this.open(opener);
  };

  open(trigger) {
    this.returnFocusEl = trigger instanceof HTMLElement ? trigger : document.activeElement;
    if (!this.dialog.open) this.dialog.showModal();
    this.form.reset();
    this.clearResults();
    this.input.focus();
  }

  close() {
    if (this.dialog.open) this.dialog.close();
  }

  // A click on ::backdrop lands on the dialog element itself (no descendant hit).
  onBackdropClick = (event) => {
    if (event.target === this.dialog) this.close();
  };

  onClose = () => {
    this.controller?.abort();
    clearTimeout(this.debounceTimer);
    this.returnFocusEl?.focus();
  };

  onInput = () => {
    clearTimeout(this.debounceTimer);
    const query = this.input.value.trim();
    if (!query) {
      this.clearResults();
      return;
    }
    this.debounceTimer = setTimeout(() => this.fetchResults(query), DEBOUNCE_MS);
  };

  async fetchResults(query) {
    this.controller?.abort();
    this.controller = new AbortController();
    const url =
      `${this.predictiveUrl}?q=${encodeURIComponent(query)}` +
      `&resources[type]=product&resources[limit]=${MAX_RESULTS}&section_id=predictive-search`;

    try {
      const response = await fetch(url, { signal: this.controller.signal });
      if (!response.ok) throw new Error(`Predictive search failed: ${response.status}`);
      const html = await response.text();
      this.renderResults(html, query);
    } catch (error) {
      if (error?.name === 'AbortError') return;
      this.clearResults();
    }
  }

  renderResults(html, query) {
    this.resultsEl.innerHTML = html;

    const empty = this.resultsEl.querySelector('[data-predictive-search-empty]');
    if (empty && this.noResultsTemplate) {
      empty.textContent = this.noResultsTemplate.replace('%%QUERY%%', query);
    }

    const seeAll = this.resultsEl.querySelector('[data-search-see-all]');
    if (seeAll) seeAll.href = `${this.form.action}?q=${encodeURIComponent(query)}&type=product`;

    this.options = [...this.resultsEl.querySelectorAll('[role="option"]')];
    this.activeIndex = -1;
    this.input.setAttribute('aria-expanded', String(this.options.length > 0));
    this.input.removeAttribute('aria-activedescendant');
  }

  clearResults() {
    this.resultsEl.innerHTML = '';
    this.options = [];
    this.activeIndex = -1;
    this.input.setAttribute('aria-expanded', 'false');
    this.input.removeAttribute('aria-activedescendant');
  }

  setActive(index) {
    if (this.options.length === 0) return;
    for (const el of this.options) el.setAttribute('aria-selected', 'false');
    this.activeIndex = index;
    const active = this.options[index];
    if (!active) {
      this.input.removeAttribute('aria-activedescendant');
      return;
    }
    active.setAttribute('aria-selected', 'true');
    active.scrollIntoView({ block: 'nearest' });
    this.input.setAttribute('aria-activedescendant', active.id);
  }

  onKeydown = (event) => {
    switch (event.key) {
      case 'Escape':
        event.preventDefault();
        this.close();
        break;
      case 'ArrowDown':
        if (this.options.length === 0) return;
        event.preventDefault();
        this.setActive((this.activeIndex + 1) % this.options.length);
        break;
      case 'ArrowUp':
        if (this.options.length === 0) return;
        event.preventDefault();
        this.setActive((this.activeIndex - 1 + this.options.length) % this.options.length);
        break;
      case 'Enter':
        if (this.activeIndex >= 0 && this.options[this.activeIndex]) {
          event.preventDefault();
          window.location.href = this.options[this.activeIndex].href;
        }
        // Else: let the form's native GET submit go to /search?q=…&type=product.
        break;
    }
  };
}

if (!customElements.get('kg-search')) customElements.define('kg-search', KgSearch);
