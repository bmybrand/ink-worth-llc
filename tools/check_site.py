from pathlib import Path
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent.parent
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width':1440,'height':1000}, device_scale_factor=1)
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    for width in [1440, 390, 320]:
        page.set_viewport_size({'width':width,'height':900})
        for name in ['index','services','about','contact']:
            page.emulate_media(reduced_motion='reduce' if name=='services' else 'no-preference')
            response = page.goto(f'http://127.0.0.1:4173/{name}.html')
            assert response.status == 200
            page.wait_for_function('document.fonts.status === "loaded"')
            assert page.locator('h1').count() == 1
            sources = page.locator('img[src*="assets/photos/"]').evaluate_all('(items)=>items.map(e=>e.getAttribute("src"))')
            assert len(sources) == len(set(sources)), f'Repeated section images: {name}'
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), f'Overflow: {name} at {width}'
            for image in page.locator('img').all():
                if image.is_visible():
                    image.evaluate('(img) => img.scrollIntoView({behavior: "instant", block: "center"})')
                image.evaluate('(img) => img.decode()')
            assert page.locator('img').evaluate_all('(images) => images.every(img => img.complete && img.naturalWidth > 0)')
            for detail in page.locator('details').all():
                detail.locator('summary').click()
                assert detail.get_attribute('open') is not None
                assert detail.locator('.faq-answer').is_visible()
                detail.locator('summary').click()
            page.evaluate('window.scrollTo(0, 0)')
            page.wait_for_timeout(800)
            if width == 1440 and name == 'index':
                page.screenshot(path=str(root/'tools/home-desktop.png'), full_page=True)
            if width == 390 and name == 'index':
                page.screenshot(path=str(root/'tools/home-mobile.png'), full_page=True)
                page.get_by_role('button', name='Menu').click()
                assert page.locator('#main-nav').is_visible()
                page.locator('#main-nav').get_by_role('link', name='Services').click()
                assert page.url.endswith('services.html')
    page.goto('http://127.0.0.1:4173/contact.html?service=design')
    assert page.locator('select').input_value() == 'design'
    page.get_by_label('Your name').fill('Test Client')
    page.get_by_label('Email address').fill('client@example.com')
    page.get_by_label('Tell us about your project').fill('A business book design project.')
    with page.expect_download() as info:
        page.get_by_role('button', name='Save project brief').click()
    assert info.value.suggested_filename == 'ink-worth-project-brief.txt'
    assert 'has not been sent' in page.locator('#form-status').inner_text()
    page.emulate_media(reduced_motion='reduce')
    page.goto('http://127.0.0.1:4173/index.html')
    assert page.locator('.hero-photograph > img').evaluate('(e) => getComputedStyle(e).animationName') == 'none'
    page.locator('.journey').scroll_into_view_if_needed()
    assert page.locator('.journey-step').first.evaluate('(e) => e.getAnimations().length') == 0
    plain = browser.new_context(java_script_enabled=False)
    plain_page = plain.new_page()
    plain_page.goto('http://127.0.0.1:4173/index.html')
    assert plain_page.locator('.journey-step').first.is_visible()
    plain_page.locator('details summary').first.click()
    assert plain_page.locator('.faq-answer').first.is_visible()
    plain.close()
    assert not errors, errors
    print('PASS: all four pages at 1440, 390, and 320px; image loading; mobile navigation; service preselection; project brief download; no JavaScript errors.')
    print('PASS: FAQs on every page, reduced motion, and content/FAQs without JavaScript.')
    browser.close()
