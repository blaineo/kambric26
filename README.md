# Kambric Goods theme

Custom Shopify Online Store 2.0 theme for [kambricgoods.com](https://kambricgoods.com), replacing the React/Vite storefront on Replit. Built on Shopify's [Skeleton theme](https://github.com/Shopify/skeleton-theme), using hand-written CSS on design tokens and vanilla-JS custom elements. There is no build step.

- Store: `kambric-goods-2.myshopify.com`
- Status: **not live.** The published Online Store theme only changes at cutover (see `docs/MIGRATION_PLAN.md`).
- Guardrails and conventions for humans and agents: [`CLAUDE.md`](./CLAUDE.md)

## Prerequisites

| Tool | Check | Install |
| --- | --- | --- |
| Shopify CLI ≥ 3.60 (4.x recommended) | `shopify version` | `brew tap shopify/shopify && brew install shopify-cli` |
| Node.js ≥ 20 (for the CLI) | `node -v` | `brew install node@22` |
| Git | `git --version` | `xcode-select --install` |
| Theme Check | `shopify theme check --version` | Bundled with Shopify CLI; nothing extra to install |

Optional: the [Shopify Liquid VS Code extension](https://shopify.dev/docs/storefronts/themes/tools/shopify-liquid-vscode) (Theme Check and Liquid language server in the editor).

## Development workflow

```bash
cd ~/Code/kambric/theme

# 1. Local preview against a *development* theme (hot reload). The first run
#    opens a browser login; do that yourself. Store comes from shopify.theme.toml.
shopify theme dev -e development
#   → http://127.0.0.1:9292 (local preview), plus theme-editor and share links

# 2. Lint (must be clean before every commit)
shopify theme check

# 3. Only when explicitly asked: upload as a new *unpublished* theme for review
shopify theme push --unpublished -e development
```

**Never** run `shopify theme publish`, `theme push --live`/`--allow-live`, or `theme delete`, and never push to the published theme. `.claude/settings.json` denies these for Claude Code as a backstop, but the rule itself lives in `CLAUDE.md`.

### Editor changes vs. the repo

`config/settings_data.json`, `templates/*.json` and `sections/*-group.json` are also written by the theme editor. `theme dev` uploads local files but doesn't pull editor edits back, unless you run it with `--theme-editor-sync`. If you customise something in the editor on the dev theme, pull or port it back into git deliberately, or it will be overwritten on the next sync.

## Project layout

```
assets/      critical.css (tokens + base), fonts (*.woff2), component-*.js custom elements
blocks/      theme blocks (reusable, nestable)
config/      settings_schema.json (theme settings), settings_data.json (values)
docs/        migration plan and decisions (not uploaded)
layout/      theme.liquid, password.liquid
licenses/    third-party licences (fonts: SIL OFL 1.1) (not uploaded)
locales/     storefront strings (en.default.json) and editor strings (*.schema.json)
sections/    sections and section groups (header-group.json, footer-group.json)
snippets/    render-only partials (meta-tags, css-variables, icon, …)
templates/   JSON templates
```

Reference export (read-only): `../replit site/`. See `CLAUDE.md` for what's in it.

## Commits

Small, logical commits with a conventional-style prefix (`feat:`, `fix:`, `chore:`, `docs:`, `refactor:`). Run `shopify theme check` before committing. There's no remote yet; one will be added later.

## Licences

- Theme code: based on Shopify Skeleton, see `LICENSE.md`.
- Fonts: Fraunces and Jost, SIL Open Font License 1.1, see `licenses/`.
