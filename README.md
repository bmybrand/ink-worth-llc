# Ink Worth LLC

A responsive four-page business website for writing, book design, and publishing services.

## Preview

Run from the project root, then open http://localhost:4173:

```sh
python -m http.server 4173 --bind 127.0.0.1
```

The checked-in HTML files can also be served by any static web host. No frontend build is needed to view the site.

## Edit and rebuild

- `tools/build_site.py`: page templates, shared navigation and footer.
- `tools/page_content.py`: detailed page content.
- `tools/visual_sections.py`: photography and visual section layouts.
- `assets/`: styles, JavaScript, original logos, and locally hosted images.

After changing a page template, regenerate the HTML:

```sh
python tools/build_site.py
```

The services page preserves its original full-width layout inside a scroll-controlled sticky section. Smaller viewports, reduced-motion preferences, and browsers without JavaScript receive the standard article layout.

## Contact form

The form currently downloads a project brief; it does not send messages. Set `enquiryEmail` in `assets/site.js` to a confirmed business address to prepare enquiries in the visitor's email app. There is no email-delivery backend.

## Browser checks

Install development dependencies and the browser, then run the checks while the preview server is running:

```sh
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
python tools/check_site.py
python tools/check_motion.py
python tools/check_service_scroll.py
```

Generated screenshots are ignored by Git. Original generated images and their prompts are retained in `assets/photos/`; the live pages use optimized WebP assets. The images illustrate publishing work and are not presented as actual client projects or company premises.
