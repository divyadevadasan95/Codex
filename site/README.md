# Glo Melanin Web Mock

A minimal, neutral-toned landing page inspired by the provided lip balm reference.

## Preview locally

From the repo root:

```bash
python -m http.server 8000 --directory site
```

Then open `http://localhost:8000`.

## Framework & hosting suggestion

The page is static HTML/CSS, so it will port cleanly to **Astro** for componentized layouts and partial hydration if you want light interactivity. Astro works well with static assets and keeps bundle sizes low, matching the minimal aesthetic.

For hosting, **Vercel** or **Netlify** will auto-build and deploy the Astro project (or the current static version) from Git, provide preview environments, and handle CDN caching and HTTPS out of the box.
