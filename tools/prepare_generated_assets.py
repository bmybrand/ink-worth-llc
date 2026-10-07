"""Encode generated originals for the web without cropping or resizing."""
import json
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent.parent
manifest = json.loads((root/'assets/photos/generated-image-prompts.json').read_text())
dimensions = {}
for asset in manifest['assets']:
    original = root/asset['path']
    with Image.open(original) as image:
        dimensions[original.stem] = image.size
        image.save(original.with_suffix('.webp'), 'WEBP', quality=88, method=6)
(root/'assets/photos/generated-dimensions.json').write_text(json.dumps(dimensions,indent=2))
with sync_playwright() as p:
    browser=p.chromium.launch()
    page=browser.new_page(viewport={'width':1440,'height':1200})
    page.goto('http://127.0.0.1:4173/')
    cards=''.join(f'<figure><img src="/assets/photos/{key}.webp"><figcaption>{key}</figcaption></figure>' for key in dimensions)
    page.set_content('<style>body{margin:20px;background:#eff3f0;font:15px Arial;display:grid;grid-template-columns:repeat(4,1fr);gap:16px}figure{margin:0}img{width:100%;height:220px;object-fit:contain;background:white}figcaption{padding:10px}</style>'+cards)
    page.locator('img').evaluate_all('(images)=>Promise.all(images.map(i=>i.decode()))')
    page.screenshot(path=str(root/'tools/generated-image-review.png'),full_page=True)
    browser.close()
print('Encoded 13 generated assets and prepared visual review.')
