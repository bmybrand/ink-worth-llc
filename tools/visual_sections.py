import re
import json
from pathlib import Path

dimensions = json.loads((Path(__file__).resolve().parent.parent/'assets/photos/generated-dimensions.json').read_text())

def photo(name, alt, cls='', eager=False):
    width, height = dimensions[name]
    return f'<img class="{cls}" src="assets/photos/{name}.webp" alt="{alt}" width="{width}" height="{height}" loading="{"eager" if eager else "lazy"}" decoding="async"'+(' fetchpriority="high"' if eager else '')+'>'

def feature(kicker, title, text, image, alt, link, label, reverse=False):
    return f'<section class="photo-feature {"reverse" if reverse else ""}"><div class="feature-photo">{photo(image,alt)}</div><div class="feature-copy"><span class="eyebrow">{kicker}</span><h2>{title}</h2><p>{text}</p><a class="button" href="{link}">{label}<span aria-hidden="true">↗</span></a></div></section>'

features = '<section class="section container feature-collection"><div class="section-heading"><div><span class="eyebrow">MAKE YOUR NEXT CHAPTER POSSIBLE</span><h2>From a promising idea<br>to a publication with purpose.</h2></div><p>The right support at the right stage, with your reader at the heart of every decision.</p></div>'
features += feature('01 / WORDS THAT CONNECT', 'Your voice.<br>A clearer story.', 'Turn a rough idea or an existing draft into writing with direction. We help you shape the structure, refine the language, and bring your perspective into focus.', 'manuscript-editing', 'An editor reviewing a manuscript with a pencil', 'services.html#writing', 'Explore writing & editing')
features += feature('02 / DESIGNED TO BE READ', 'Make every page<br>an invitation.', 'A compelling cover opens the conversation. Considered typography, space, and page flow keep it going. Bring the outside and inside of your book together in one coherent design.', 'cover-design', 'Navy and teal cover concepts arranged with paper and color samples', 'services.html#design', 'Explore book design', True)
features += feature('03 / READY FOR WHAT COMES NEXT', 'A finished manuscript.<br>A fresh beginning.', 'Understand the steps between your final draft and publication. Plan the formats, prepare the agreed files, and give your book a clear path toward its next chapter.', 'publishing-proof', 'An open hardcover book and publication proofs on a navy workbench', 'services.html#publishing', 'Explore publishing support')
features += '</section>'

resources = '''<section class="resource-section section"><div class="container"><div class="section-heading"><div><span class="eyebrow">A LITTLE DIRECTION GOES A LONG WAY</span><h2>Start with a clearer picture.</h2></div><p>Practical guidance for the decisions that come before the first draft, design, or enquiry.</p></div><div class="resource-grid">'''
for image,alt,kicker,title,desc,link in [
('draft-planning','Index cards arranged into a book outline','PLAN YOUR MANUSCRIPT','What does your draft need?','Understand the difference between developing an idea, refining a manuscript, and preparing a final proof.','services.html#writing'),
('design-direction','Paper and binding cloth samples for book design','FIND YOUR DIRECTION','Words, design, or both?','Match your current project stage to a useful next step and the materials you need to bring.','services.html#project-stage'),
('project-brief','A project brief, reading glasses, and a teal notebook','PREPARE YOUR BRIEF','Make the first conversation count.','Gather your audience, goals, timeline, and priorities into a brief that gives your project direction.','contact.html#prepare-brief')]:
    resources += f'<a class="resource-card" href="{link}"><div class="resource-image">{photo(image,alt)}</div><div class="resource-copy"><span class="eyebrow">{kicker}</span><h3>{title}</h3><p>{desc}</p><span class="text-link">Explore the guidance <span aria-hidden="true">↗</span></span></div></a>'
resources += '</div></div></section>'

def enhance(home, services, about, contact):
    hero_photo = '<div class="hero-photograph">'+photo('banner-branded','Navy, teal, and ivory clothbound books bearing the Ink Worth LLC logo',eager=True)+'<div class="photo-caption"><span class="eyebrow">FOR THE STORIES STILL TO COME</span><p>Something worth writing.<br>Something worth holding.</p><span class="photo-caption-rule"></span></div></div>'
    home = re.sub(r'<div class="book-scene".*?</div></div></section>', hero_photo+'</div></section>', home, count=1, flags=re.S)
    home = re.sub(r'<section class="showcase section">.*?</section>', features, home, count=1, flags=re.S)
    home = home.replace('<section class="section container faq-section">', resources+'<section class="section container faq-section">',1)
    home = re.sub(r'<div class="brand-panel">.*?</div>', '<div class="editorial-photo">'+photo('editorial-craft','An open stitched book and fountain pen on pale stone')+'<span class="image-label">THE CRAFT BEHIND THE WORDS</span></div>', home, count=1, flags=re.S)
    about = re.sub(r'<div class="brand-panel">.*?</div>', '<div class="editorial-photo">'+photo('editorial-craft','An open stitched book and fountain pen on pale stone')+'<span class="image-label">THOUGHTFUL WORK STARTS WITH A LITTLE INK</span></div>', about, count=1, flags=re.S)
    photo_banner = '''<section class="container collaboration-section" id="collaboration" aria-labelledby="collaboration-title"><div class="collaboration-layout"><div class="collaboration-image">'''+photo('studio-conversation','Books and notebooks arranged in a bright, welcoming publishing studio')+'''<span class="collaboration-image-note">A SHARED DIRECTION. A PERSONAL APPROACH.</span></div><div class="collaboration-copy"><span class="eyebrow">CREATED WITH YOU</span><h2 id="collaboration-title">Your perspective.<br>Our craft.<br><em>A better story.</em></h2><p>The strongest work starts with a conversation. Bring your ideas, your questions, and the details that matter to you. We’ll help give them shape.</p><div class="collaboration-points"><div><span aria-hidden="true">01</span><p><strong>Space for your ideas.</strong>Your voice guides the creative direction.</p></div><div><span aria-hidden="true">02</span><p><strong>Care at every step.</strong>Thoughtful feedback keeps the work moving.</p></div></div><a class="button" href="contact.html">Talk through your idea <span aria-hidden="true">↗</span></a></div></div><div class="collaboration-principle"><span class="eyebrow">OUR GUIDING IDEA</span><p>Words carry your perspective.<br><em>Design helps the world see it.</em></p></div></section>'''
    about = re.sub(r'<section class="mission-note container">.*?</section>',photo_banner,about,count=1,flags=re.S)
    for title,name,alt in [('Writing & editing','manuscript-editing','An editor refining a printed manuscript'),('Book design','cover-design','Book cover concepts, color swatches, and layout materials'),('Publishing support','publishing-proof','An open bound book beside print proofs')]:
        services = services.replace(f'<h2>{title}</h2>',f'<h2>{title}</h2><div class="service-photograph">{photo(name,alt)}</div>',1)
    services = services.replace('<div class="comparison-wrap">','<div class="comparison-wrap" id="project-stage">')
    contact = contact.replace('<section class="process section">','<section class="process section" id="prepare-brief">')
    contact = contact.replace('<div class="contact-note">','<div class="contact-photograph">'+photo('contact-notebook','An open notebook, navy pen, and ivory envelope')+'</div><div class="contact-note">')
    for image,alt,kicker in [('author-desk','A quiet author workspace beside a sunlit window','THE PERSONAL CHAPTER'),('expert-workbook','A structured workbook with teal tabs and a laptop','THE PROFESSIONAL CHAPTER'),('brand-publication','An editorial brochure and presentation folder on a meeting table','THE BUSINESS CHAPTER')]:
        needle=f'<article class="audience-card"><span class="eyebrow">{kicker}'
        replacement=f'<article class="audience-card"><div class="audience-photo">{photo(image,alt)}</div><span class="eyebrow">{kicker}'
        home=home.replace(needle,replacement)
        about=about.replace(needle,replacement)
    return home,services,about,contact
