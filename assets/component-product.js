/**
 * Product page (sections/main-product.liquid).
 *
 * <kg-gallery>  scroll-snap gallery: prev/next wrap, thumbnails track the slide.
 * <kg-product>  print swap (Section Rendering API + ?variant=, D-7), legacy
 *               ?print= links, size selection, monogram (D-9), add to cart
 *               with linked fee line, back-in-stock hand-off (D-12).
 *
 * Everything enhances server-rendered HTML; the page works without it.
 */

const reducedMotion = () => matchMedia('(prefers-reduced-motion: reduce)').matches;

class KgGallery extends HTMLElement {
  connectedCallback() {
    this.track = this.querySelector('[data-gallery-track]');
    if (!this.track) return;
    this.slides = [...this.track.querySelectorAll('[data-gallery-slide]')];
    this.thumbs = [...this.querySelectorAll('[data-gallery-thumb]')];
    this.index = 0;
    this.addEventListener('click', this);
    this.observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) this.setCurrent(this.slides.indexOf(entry.target));
        }
      },
      { root: this.track, threshold: 0.6 }
    );
    this.slides.forEach((slide) => this.observer.observe(slide));
  }

  disconnectedCallback() {
    this.observer?.disconnect();
  }

  handleEvent(event) {
    const target = event.target.closest('[data-gallery-prev], [data-gallery-next], [data-gallery-thumb]');
    if (!target) return;
    event.preventDefault();
    const count = this.slides.length;
    if (target.hasAttribute('data-gallery-thumb')) this.go(Number(target.dataset.galleryThumb));
    else this.go((this.index + (target.hasAttribute('data-gallery-next') ? 1 : -1) + count) % count);
  }

  go(index) {
    const slide = this.slides[index];
    if (!slide) return;
    this.track.scrollTo({ left: slide.offsetLeft - this.track.offsetLeft, behavior: reducedMotion() ? 'auto' : 'smooth' });
    this.setCurrent(index);
  }

  setCurrent(index) {
    if (index < 0) return;
    this.index = index;
    this.thumbs.forEach((thumb, i) => {
      if (i === index) thumb.setAttribute('aria-current', 'true');
      else thumb.removeAttribute('aria-current');
    });
  }
}

/** Pure helpers (exported for tests). */
export const MONOGRAM_MAX = 10;

export function monogramGroupId() {
  const rnd = crypto.randomUUID?.() ?? Date.now().toString(36) + Math.random().toString(36).slice(2, 10);
  return `mg_${rnd}`;
}

/** Button state from the current selection. */
export function buyState({ printAvailable, fixed, selected, selectedAvailable, monogramOn, monogramValid }) {
  if (!printAvailable) return 'notify';
  if (!fixed && !selected) return 'select';
  if (!selectedAvailable) return 'notify';
  if (monogramOn && !monogramValid) return 'monogram';
  return 'ready';
}

/** Cart items for one add: the garment, plus the linked fee line when monogrammed. */
export function cartItems({ variantId, monogram, feeVariantId, forLabel, groupId }) {
  const garment = { id: Number(variantId), quantity: 1 };
  if (!monogram) return [garment];
  const shared = { Monogram: monogram.text, 'Thread color': monogram.color };
  garment.properties = { ...shared, _monogramGroup: groupId };
  return [
    garment,
    {
      id: Number(feeVariantId),
      quantity: 1,
      properties: { ...shared, For: forLabel, _monogramGroup: groupId, _fee: '1' },
    },
  ];
}

/** Resolve a legacy ?print= value: one exact match among the print values, else null. */
export function resolveLegacyPrint(search, values) {
  const params = new URLSearchParams(search);
  if (params.has('variant')) return null;
  const all = params.getAll('print');
  if (all.length !== 1) return null;
  return values.includes(all[0]) ? all[0] : null;
}

let legacyHandled = false;

class KgProduct extends HTMLElement {
  connectedCallback() {
    this.button = this.querySelector('[data-buy-button]');
    this.monogram = this.querySelector('[data-monogram]');
    this.addEventListener('click', this);
    this.addEventListener('change', this);
    this.addEventListener('input', this);
    this.addEventListener('submit', this);
    // Sold-out sizes are disabled for no-JS posts; with JS they open back-in-stock.
    this.querySelectorAll('[data-sold-out]').forEach((input) => (input.disabled = false));
    if (this.monogram) this.monogram.disabled = false;
    // JS owns validation (button states); native `required` stays for no-JS posts.
    if (this.form) this.form.noValidate = true;
    this.update();

    if (!legacyHandled) {
      legacyHandled = true;
      const links = [...this.querySelectorAll('a[data-print-value]')];
      const print = resolveLegacyPrint(location.search, links.map((a) => a.dataset.printValue));
      const link = links.find((a) => a.dataset.printValue === print);
      if (link) {
        if (link.getAttribute('aria-current') === 'true') this.setUrl(link.dataset.variantId);
        else this.swap(link);
      }
    }
  }

  get form() {
    return document.getElementById(this.dataset.formId);
  }

  get selected() {
    return this.querySelector('input[name="id"][type="radio"]:checked');
  }

  handleEvent(event) {
    const { type, target } = event;
    if (type === 'submit') return this.onSubmit(event);
    if (type === 'click') {
      const link = target.closest('a[data-print-value]');
      if (link && !event.metaKey && !event.ctrlKey && !event.shiftKey) {
        event.preventDefault();
        if (link.getAttribute('aria-current') !== 'true') this.swap(link);
        return;
      }
      // Pointer clicks on a sold-out size (not the forwarded input click) open back-in-stock.
      const label = target.closest('[data-size]');
      const input = label?.querySelector('[data-sold-out]');
      if (input && target !== input && event.detail > 0) {
        queueMicrotask(() => this.notify(input));
      }
      return;
    }
    if (target.name === 'id') this.setUrl(target.value);
    if (target.matches('[data-monogram-toggle]')) {
      const fields = this.querySelector('[data-monogram-fields]');
      fields.hidden = !target.checked;
      target.setAttribute('aria-expanded', String(target.checked));
    }
    this.update();
  }

  monogramValues() {
    if (!this.monogram) return null;
    const on = this.monogram.querySelector('[data-monogram-toggle]').checked;
    const text = this.monogram.querySelector('[data-monogram-text]').value.trim();
    const color = this.monogram.querySelector('[data-monogram-colour]:checked')?.value || '';
    return { on, text, color, valid: text.length > 0 && text.length <= MONOGRAM_MAX && !!color };
  }

  update() {
    const selected = this.selected;
    const fixed = this.querySelector('[data-fixed-variant]');
    const mono = this.monogramValues();

    if (mono) {
      const count = this.monogram.querySelector('[data-monogram-count]');
      count.textContent = `${mono.text.length}/${MONOGRAM_MAX}`;
      this.monogram.querySelector('[data-monogram-colour-name]').textContent = mono.color;
    }

    const selectedLabel = this.querySelector('[data-size-selected]');
    if (selectedLabel && selected) {
      const value = Object.assign(document.createElement('span'), { textContent: selected.dataset.sizeValue });
      selectedLabel.replaceChildren(`${selectedLabel.dataset.word} `, value);
    }

    const price = this.querySelector('[data-product-price]');
    const tpl = this.querySelector(`template[data-price-for="${selected?.value || 'default'}"]`);
    if (price && tpl) price.replaceChildren(tpl.content.cloneNode(true));

    if (!this.button || this.button.dataset.busy) return;
    const state = buyState({
      printAvailable: this.dataset.printAvailable === 'true',
      fixed: !!fixed,
      selected: !!selected,
      selectedAvailable: fixed ? fixed.dataset.available === 'true' : !!selected && !selected.hasAttribute('data-sold-out'),
      monogramOn: !!mono?.on,
      monogramValid: !!mono?.valid,
    });
    this.setButton(state);
  }

  setButton(state) {
    const b = this.button;
    b.dataset.state = state;
    const key = { ready: 'add', select: 'select', notify: 'notify', monogram: 'monogram', adding: 'adding', added: 'added' }[state];
    b.textContent = b.dataset[`label${key[0].toUpperCase()}${key.slice(1)}`];
    b.disabled = !['ready', 'notify'].includes(state);
  }

  notify(input) {
    document.dispatchEvent(
      new CustomEvent('kg:notify-request', {
        detail: {
          productTitle: this.dataset.productTitle,
          productUrl: new URL(this.dataset.productUrl, location.origin).href,
          print: this.dataset.print || undefined,
          size: input?.dataset.sizeValue,
          variantId: input?.value,
        },
      })
    );
  }

  setUrl(variantId) {
    if (!variantId) return;
    const url = new URL(location.href);
    url.searchParams.delete('print');
    url.searchParams.set('variant', variantId);
    history.replaceState(history.state, '', url);
  }

  async swap(link) {
    const url = new URL(link.href, location.href);
    url.searchParams.set('section_id', this.dataset.sectionId);
    this.setAttribute('aria-busy', 'true');
    try {
      const response = await fetch(url);
      if (!response.ok) throw new Error(response.status);
      const doc = new DOMParser().parseFromString(await response.text(), 'text/html');
      const fresh = doc.querySelector('kg-product');
      if (!fresh) throw new Error('No product markup');
      // A print change resets the size (source behaviour); the URL keeps the print's variant.
      fresh.querySelectorAll('input[name="id"][type="radio"]').forEach((input) => input.removeAttribute('checked'));
      fresh.querySelector('[data-size-selected]')?.replaceChildren();
      this.setUrl(link.dataset.variantId);
      const focused = this.contains(document.activeElement);
      this.replaceWith(fresh);
      if (focused) fresh.querySelector(`a[data-print-value="${CSS.escape(link.dataset.printValue)}"]`)?.focus();
    } catch {
      location.assign(link.href);
    }
  }

  async onSubmit(event) {
    const form = this.form;
    if (event.target !== form) return;
    event.preventDefault();
    const state = this.button?.dataset.state;
    if (state === 'notify') return this.notify(this.selected);
    if (state && state !== 'ready') return;

    const variantId = new FormData(form).get('id');
    if (!variantId) return;
    const mono = this.monogramValues();
    const withMonogram = mono?.on && mono.valid;
    const items = cartItems({
      variantId,
      monogram: withMonogram ? { text: mono.text, color: mono.color } : null,
      feeVariantId: this.monogram?.dataset.feeVariant,
      forLabel: this.dataset.for,
      groupId: withMonogram ? monogramGroupId() : null,
    });

    const error = this.querySelector('[data-buy-error]');
    const status = this.querySelector('[data-buy-status]');
    const headerSection = document.querySelector('.site-header')?.closest('.shopify-section')?.id.replace('shopify-section-', '');
    error.hidden = true;
    this.setButton('adding');
    this.button.dataset.busy = '1';
    try {
      const response = await fetch(`${this.dataset.cartAddUrl}.js`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({ items, ...(headerSection && { sections: headerSection }) }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.description || response.status);
      this.updateCartCount(data.sections?.[headerSection]);
      this.setButton('added');
      status.textContent = this.button.textContent;
      this.resetMonogram();
      setTimeout(() => {
        delete this.button.dataset.busy;
        status.textContent = '';
        this.update();
      }, 2500);
    } catch {
      delete this.button.dataset.busy;
      error.hidden = false;
      this.update();
    }
  }

  resetMonogram() {
    if (!this.monogram) return;
    const toggle = this.monogram.querySelector('[data-monogram-toggle]');
    toggle.checked = false;
    toggle.setAttribute('aria-expanded', 'false');
    this.monogram.querySelector('[data-monogram-fields]').hidden = true;
    this.monogram.querySelector('[data-monogram-text]').value = '';
    this.monogram.querySelectorAll('[data-monogram-colour]').forEach((input) => (input.checked = false));
  }

  /** Swap the header's cart links (icon count + label, mobile menu) with the freshly rendered ones. */
  updateCartCount(html) {
    if (!html) return;
    const selector = `.site-header a[href="${this.dataset.cartUrl}"]`;
    const fresh = new DOMParser().parseFromString(html, 'text/html').querySelectorAll(selector);
    document.querySelectorAll(selector).forEach((link, i) => {
      if (fresh[i]) link.replaceChildren(...fresh[i].childNodes);
    });
  }
}

if (typeof customElements !== 'undefined') {
  if (!customElements.get('kg-gallery')) customElements.define('kg-gallery', KgGallery);
  if (!customElements.get('kg-product')) customElements.define('kg-product', KgProduct);
}
