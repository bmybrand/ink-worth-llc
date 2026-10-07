from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch()
    page=browser.new_page(viewport={'width':1440,'height':950})
    errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto('http://127.0.0.1:4173/services.html')
    def seek(offset):
        page.evaluate('''offset=>{const t=document.querySelector('.service-scroll-track');const inset=parseFloat(getComputedStyle(document.querySelector('.service-scroll-viewport')).top);scrollTo({top:t.getBoundingClientRect().top+scrollY-inset+offset*1.1,behavior:'instant'})}''',offset)
        page.wait_for_timeout(80)
    viewport=page.locator('.service-scroll-viewport')
    content=page.locator('.service-details')
    assert page.locator('.service-detail').count()==3
    assert page.locator('.service-notes > div').count()==9
    assert page.locator('.story-nav, .story-panels, .story-controls').count()==0
    seek(0)
    first_y=page.locator('#writing h2').bounding_box()['y']
    page.locator('#writing img').evaluate('(i)=>i.decode()')
    viewport.screenshot(path='tools/original-pinned-desktop.png')
    for offset in [240,700,1200,1800]:
        seek(offset)
        assert abs(viewport.bounding_box()['y']-page.locator('.site-header').bounding_box()['height']-20)<2
        assert abs(page.locator('#writing h2').bounding_box()['y']-(first_y-offset))<2
    seek(500)
    viewport.screenshot(path='tools/original-pinned-scrolled.png')
    seek(0)
    assert abs(page.locator('#writing h2').bounding_box()['y']-first_y)<2
    plain=browser.new_context(java_script_enabled=False,viewport={'width':1440,'height':950})
    fallback=plain.new_page()
    fallback.goto('http://127.0.0.1:4173/services.html')
    for selector in ['#writing h2','#writing img','#writing > a','#writing .service-notes']:
        original=fallback.locator(selector).bounding_box()
        pinned=page.locator(selector).bounding_box()
        assert abs(original['x']-pinned['x'])<2,selector
        assert abs(original['width']-pinned['width'])<2,selector
    page.goto('http://127.0.0.1:4173/services.html#design')
    page.wait_for_timeout(200)
    assert 133<=page.locator('#design h2').bounding_box()['y']<260
    page.locator('#publishing > a').focus()
    assert 133<=page.locator('#publishing > a').bounding_box()['y']<310
    page.locator('#publishing > a').click()
    assert page.url.endswith('contact.html?service=publishing')
    for width,height in [(390,900),(360,740),(768,850)]:
        page.set_viewport_size({'width':width,'height':height})
        page.goto('http://127.0.0.1:4173/services.html')
        seek(300)
        assert abs(viewport.bounding_box()['y']-page.locator('.site-header').bounding_box()['height']-20)<2
        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
        if width==390:
            seek(0)
            page.locator('#writing img').evaluate('(i)=>i.decode()')
            viewport.screenshot(path='tools/original-pinned-mobile.png')
    page.evaluate('''()=>{const t=document.querySelector('.service-scroll-track');scrollTo({top:t.getBoundingClientRect().top+scrollY+t.offsetHeight,behavior:'instant'})}''')
    page.wait_for_timeout(80)
    assert viewport.bounding_box()['y']<0,'Section must release at the end'
    page.emulate_media(reduced_motion='reduce')
    page.wait_for_timeout(100)
    assert viewport.count()==0 and content.is_visible()
    page.emulate_media(reduced_motion='no-preference')
    page.set_viewport_size({'width':320,'height':550})
    page.reload()
    assert viewport.count()==0 and content.is_visible()
    assert fallback.locator('.service-detail').last.is_visible()
    assert not errors,errors
    print('PASS: previous layout preserved; section pins while original content moves; reverse scroll, end release, direct links, focus/CTA, mobile, reduced motion and no-JS fallback.')
    browser.close()
