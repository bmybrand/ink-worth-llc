from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width':1440,'height':950})
    page.goto('http://127.0.0.1:4173/index.html')
    image = page.locator('.hero-photograph img')
    image.evaluate('(img) => img.decode()')
    assert 'banner-branded.webp' in image.get_attribute('src')
    card = page.locator('.audience-card').first
    assert card.get_attribute('data-scroll-state') == 'waiting'
    assert card.evaluate('(e) => getComputedStyle(e).opacity') == '0'
    card.evaluate('(e) => e.scrollIntoView({behavior:"instant", block:"center"})')
    page.wait_for_function('document.querySelector(".audience-card").dataset.scrollState === "revealed"')
    page.wait_for_timeout(1300)
    assert card.evaluate('(e) => getComputedStyle(e).opacity') == '1'
    photo = page.locator('.feature-photo').first
    assert photo.get_attribute('data-scroll-state') == 'waiting'
    photo.evaluate('(e) => e.scrollIntoView({behavior:"instant", block:"center"})')
    page.wait_for_function('document.querySelector(".feature-photo").dataset.scrollState === "revealed"')
    page.wait_for_timeout(1200)
    assert photo.evaluate('(e) => e.getAnimations().length') == 0
    page.emulate_media(reduced_motion='reduce')
    page.wait_for_function('getComputedStyle(document.querySelector(".resource-card")).opacity === "1"')
    assert page.locator('.resource-card').first.evaluate('(e) => getComputedStyle(e).opacity') == '1'
    assert page.locator('.resource-card').first.evaluate('(e) => e.getAnimations().length') == 0
    for width in [1440,390,320]:
        page.set_viewport_size({'width':width,'height':1000})
        page.goto('http://127.0.0.1:4173/index.html')
        page.locator('.hero-photograph img').evaluate('(img) => img.decode()')
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
        page.screenshot(path=f'tools/studio-hero-{width}.png')
    page.emulate_media(reduced_motion='no-preference')
    page.set_viewport_size({'width':320,'height':850})
    page.goto('http://127.0.0.1:4173/services.html')
    first_note = page.locator('#writing .service-notes > div').first
    next_service = page.locator('#design .service-photograph')
    assert first_note.get_attribute('data-scroll-state') == 'waiting'
    assert next_service.get_attribute('data-scroll-state') == 'waiting'
    first_note.evaluate('(e) => e.scrollIntoView({behavior:"instant", block:"center"})')
    page.wait_for_function('document.querySelector("#writing .service-notes > div").dataset.scrollState === "revealed"')
    page.wait_for_timeout(1400)
    assert first_note.evaluate('(e) => getComputedStyle(e).opacity') == '1'
    assert next_service.get_attribute('data-scroll-state') == 'waiting'
    for step in page.locator('.service-detail [data-scroll-state]').all():
        step.evaluate('(e) => e.scrollIntoView({behavior:"instant", block:"center"})')
        page.wait_for_function('(e) => e.dataset.scrollState === "revealed"', arg=step.element_handle())
    page.emulate_media(reduced_motion='reduce')
    page.wait_for_timeout(100)
    assert page.locator('.service-detail [data-scroll-state]').evaluate_all('(items)=>items.every(e=>getComputedStyle(e).opacity === "1")')
    print('PASS: branded hero loads; cards/images/service headings, paragraphs, bullets and notes reveal as reached; reduced motion; desktop/mobile layouts.')
    browser.close()
