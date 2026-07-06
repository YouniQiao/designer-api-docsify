# OH API Reference

HarmonyOS API Reference Documentation — powered by [Docsify](https://docsify.js.org).

## Structure

- `docs/en/` — English documentation
- `docs/zh-CN/` — Chinese documentation
- `docs/interface_sdk-js-md/` — JS/ArkTS API source (markdown)
- `docs/interface_sdk_c-md/` — C API source (markdown)
- `gen-sidebar.py` — Regenerate sidebar HTML from Readme files

## Local Development

```bash
# Install docsify CLI
npm install

# Serve locally
npx docsify serve docs
```

Visit http://localhost:3000

## Regenerate Sidebars

```bash
python3 gen-sidebar.py
```

## Deploy

This is a static site. Point any static host (Netlify, Vercel, GitHub Pages) at the `docs/` directory.

### Netlify

Publish directory: `docs/`
No build command needed.
