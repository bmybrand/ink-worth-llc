def heading(kicker, title, description=''):
    return f'<div class="section-heading"><div><span class="eyebrow">{kicker}</span><h2>{title}</h2></div>' + (f'<p>{description}</p>' if description else '') + '</div>'

def faq(items, title='A few questions, answered.'):
    return '<section class="section container faq-section">'+heading('GOOD TO KNOW', title)+'<div class="faq-list">'+''.join(f'<details><summary>{q}<span aria-hidden="true">+</span></summary><div class="faq-answer"><p>{a}</p></div></details>' for q,a in items)+'</div></section>'

journey = '''<section class="journey section"><div class="container">'''+heading('FROM FIRST THOUGHT TO FINAL PAGE', 'Your vision. A thoughtful process.', 'Each project has its own starting point. We build the next steps around yours.')+'''<div class="journey-grid">'''+''.join(f'<article class="journey-step"><span class="step-index">0{i+1}</span><h3>{t}</h3><p>{d}</p></article>' for i,(t,d) in enumerate([
('Discover the story', 'We begin with your purpose, audience, and ambitions. Share your manuscript, outline, or idea so we can understand the work ahead.'),
('Shape the direction', 'Together, we define the scope: the services you need, the materials to prepare, and the milestones that will guide the project.'),
('Create & refine', 'Words and design come together through considered drafts and feedback. You help steer the details that make the project feel like yours.'),
('Prepare the next chapter', 'We review the agreed deliverables and prepare the final materials, with clear guidance on how to use them and what comes next.')]))+'''</div></div></section>'''

audiences = '''<section class="section container">'''+heading('WHO WE WORK WITH', 'Different ambitions.<br>The same attention to detail.', 'A personal story, a professional perspective, or a publication with a business purpose. There is room for all three.')+'''<div class="audience-grid">'''+''.join(f'<article class="audience-card"><span class="eyebrow">{k}</span><h3>{t}</h3><p>{d}</p><ul class="check-list">'+''.join(f'<li>{x}</li>' for x in points)+'</ul></article>' for k,t,d,points in [
('THE PERSONAL CHAPTER','Authors & storytellers','Turn the story you have been carrying into a reading experience that feels complete.', ['Fiction and personal narratives','Memoirs and reflective writing','First manuscripts and revised drafts']),
('THE PROFESSIONAL CHAPTER','Experts & entrepreneurs','Give your knowledge a clear structure and turn your experience into a useful resource.', ['Business and thought leadership books','Practical guides and workbooks','Educational and specialist content']),
('THE BUSINESS CHAPTER','Brands & organisations','Create publications that express your identity and make complex ideas easier to understand.', ['Company stories and brand publications','Customer guides and editorial content','Internal resources and training materials'])])+'''</div></section>'''

showcase = '''<section class="showcase section"><div class="container">'''+heading('POSSIBILITIES IN PRINT', 'One idea.<br>So many ways to tell it.', 'Illustrative formats to spark a direction for your project.')+'''<div class="format-grid"><article><div class="format-art art-story" aria-hidden="true"><div class="mini-cover"><small>A PERSONAL JOURNEY</small><strong>Between<br>the <i>lines.</i></strong><span>STORIES THAT STAY WITH US</span></div></div><h3>The story that stays.</h3><p>A memoir or novel shaped around voice, rhythm, and an immersive reading experience.</p></article><article><div class="format-art art-guide" aria-hidden="true"><div class="mini-cover"><small>IDEAS INTO ACTION</small><strong>A different<br>kind of<br><i>thinking.</i></strong><span>A PRACTICAL PERSPECTIVE</span></div></div><h3>The idea that leads.</h3><p>A business book or expert guide that makes your perspective clear and your knowledge useful.</p></article><article><div class="format-art art-workbook" aria-hidden="true"><div class="mini-cover"><small>SPACE TO EXPLORE</small><strong>Make<br>room for<br><i>more.</i></strong><span>NOTES · IDEAS · POSSIBILITIES</span></div></div><h3>The page that inspires.</h3><p>A workbook or branded publication designed to invite participation, reflection, and discovery.</p></article></div><p class="sample-note">Concept designs shown for illustration; these are not client projects.</p></div></section>'''

home_faq = faq([
('I only have an idea. Can I still get started?', 'Yes. A short outline, a few notes, or a description of your audience is a useful starting point. The first step is to clarify what you want to create and identify the support that would help you move forward.'),
('Can I choose just one service?', 'You can discuss a focused piece of work, such as editing an existing draft or designing a cover, as well as support across several stages. The scope is agreed around your project.'),
('What affects the timeline and cost?', 'Manuscript length, its current condition, design complexity, required formats, and the amount of revision all affect the scope. Share these details and any target date so the work can be planned realistically.'),
('Do you work on business publications as well as books?', 'The same care for words and design applies to business guides, workbooks, brand stories, and educational materials. Tell us the purpose and who will read it so we can discuss the right approach.')])

home_extra = audiences + journey + showcase + '''<section class="editorial-band"><div class="container split"><span class="large-quote" aria-hidden="true">“</span><div><span class="eyebrow">THE INK WORTH PHILOSOPHY</span><h2>The best version of your story<br>still sounds like you.</h2><p>Our role is to bring clarity to your words and intention to your design. From a small editorial detail to the feeling of a finished cover, every decision should help your idea connect with its reader.</p><a class="text-link" href="about.html">Discover our approach <span aria-hidden="true">↗</span></a></div></div></section>''' + home_faq

service_notes = {
'writing': [('Where we begin', 'Share your manuscript or a representative sample, its approximate word count, and the audience you want to reach. Let us know whether you need help with the overall structure, sentence-level clarity, or a final proofread.'), ('What we work on', 'Depending on the agreed scope, we can address organisation, consistency, flow, tone, grammar, and readability. Structural editing and final proofreading serve different purposes; we clarify the level of attention your draft needs.'), ('What you take forward', 'The agreed edited material and editorial guidance give you a clearer next draft. Revision rounds, file formats, and the boundaries of the edit are defined before work starts.')],
'design': [('Where we begin', 'Your manuscript, intended format, audience, and visual references establish the direction. If you have brand guidelines or a preferred printing platform, include those requirements in the brief.'), ('What we work on', 'Cover concepts establish the visual tone while interior design considers hierarchy, typography, spacing, and page flow. The format and reading experience guide the design rather than decoration alone.'), ('What you take forward', 'Final design files are prepared to the formats and specifications agreed for the project. Print layouts, ebook requirements, and editable source files are discussed individually so the handover is clear.')],
'publishing': [('Where we begin', 'We review where your project stands, the formats you are considering, and your intended route to readers. A finished manuscript and a target publication date help identify the remaining preparation.'), ('What we work on', 'Support can include a publication checklist, file preparation, and launch materials. Platform choices, production requirements, and the sequence of tasks are considered as part of your plan.'), ('What you take forward', 'You receive the agreed prepared materials and a practical outline of next steps. Printing, platform accounts, distribution arrangements, and third-party charges are scoped separately when relevant.')]
}

services_extra = '''<section class="section container">'''+heading('BUILD THE RIGHT BRIEF', 'Choose your starting point.', 'You do not need every service. Start with the stage that matches your project today.')+'''<div class="comparison-wrap"><table><caption>Support by project stage</caption><thead><tr><th scope="col">Where you are</th><th scope="col">A useful next step</th><th scope="col">What to bring</th></tr></thead><tbody><tr><th scope="row">An idea or early outline</th><td>Writing and structure guidance</td><td>Your concept, audience, and key messages</td></tr><tr><th scope="row">A complete draft</th><td>Editorial review and refinement</td><td>Your manuscript and approximate word count</td></tr><tr><th scope="row">A polished manuscript</th><td>Cover design and interior layout</td><td>The edited text, format, and design references</td></tr><tr><th scope="row">Ready for publication</th><td>File preparation and publishing guidance</td><td>Final materials and platform requirements</td></tr></tbody></table></div></section>'''+faq([
('How is a project scoped?', 'The scope describes the work, deliverables, review stages, and responsibilities. It should also identify anything outside the project, such as printing fees or additional formats, before work begins.'),
('Are revisions included?', 'The number and type of review rounds are agreed for each project. Feedback works best when it is gathered into a clear set of comments at each milestone. New requirements may change the scope.'),
('Can you work with an existing cover or brand identity?', 'Share the original files, usage permissions, brand guidelines, and the changes you need. These help establish whether existing materials can be adapted or whether a new design is appropriate.'),
('Does publishing support guarantee sales or distribution?', 'No. Preparing a publication does not guarantee platform acceptance, retail placement, or sales. Those outcomes depend on external requirements, distribution decisions, marketing, and reader demand.')], 'Before we begin.')

about_extra = '''<section class="editorial-band"><div class="container split"><div><span class="eyebrow">WHY INK WORTH</span><h2>Because the story<br>is only the beginning.</h2></div><div><p>An idea has potential. Bringing it to a reader takes another kind of care: finding the structure, sharpening the language, and creating a design that makes the content inviting.</p><p>We bring these disciplines into one conversation. Editorial choices inform the layout. The audience shapes the cover. The intended format guides how the final materials are prepared.</p><p>The aim is a coherent publication, with each part working toward the same purpose.</p></div></div></section>'''+'''<section class="section container">'''+heading('WHAT COLLABORATION LOOKS LIKE', 'A shared direction.<br>Room for your perspective.')+'''<div class="principle-grid">'''+''.join(f'<article><span class="card-number">0{i+1} /</span><h3>{t}</h3><p>{d}</p></article>' for i,(t,d) in enumerate([
('Listening before creating', 'Your goals, references, and concerns form the starting point. We want to understand what success means for this particular project before proposing a direction.'),
('Making decisions clear', 'A useful recommendation explains its purpose. We connect choices about language, structure, and design to your intended audience and reading experience.'),
('Feedback with a purpose', 'Review stages create space to ask questions and refine the work. A shared brief helps keep feedback focused while allowing the strongest ideas to develop.'),
('A considered handover', 'The final stage is about usability as well as appearance. Agreed files, formats, and next steps should be understandable when the project moves into your hands.')]))+'''</div></section>'''+audiences+'''<section class="mission-note container"><span class="eyebrow">OUR GUIDING IDEA</span><h2>Words carry your perspective.<br>Design helps the world see it.</h2><p>We believe a successful collaboration respects both. That is the thinking we bring to every Ink Worth project.</p></section>'''

contact_extra = '''<section class="process section"><div class="container">'''+heading('MAKE A USEFUL FIRST BRIEF', 'A little context goes a long way.', 'Share what you know. Leave room for the questions we can work through together.')+'''<div class="cards">'''+''.join(f'<article><span class="card-number">0{i+1} /</span><h3>{t}</h3><p>{d}</p></article>' for i,(t,d) in enumerate([
('Your project', 'Describe what you are making, who it is for, and what you want readers to take away. Mention whether you have an idea, outline, first draft, or finished manuscript.'),
('Your priorities', 'Tell us where you most need help: the words, the design, or the next steps toward publication. Include an approximate word count and any required formats.'),
('Your practical details', 'Add a target date, a budget range if you have one, and anything that is already fixed. If you have visual references or brand guidelines, mention them in your message.')]))+'''</div></div></section>'''+faq([
('Do I need a finished manuscript to make an enquiry?', 'No. Describe your idea and its current stage. An early conversation can focus on structure and direction, while a completed manuscript makes it easier to discuss editing or design requirements.'),
('Should I include my whole manuscript in the form?', 'A short description is enough for the initial brief. Include the genre or topic, approximate length, and the kind of support you need. There is no manuscript upload on this form.'),
('What if I am unsure which service to choose?', 'Select “A little of everything / Not sure yet” and describe what you want to achieve. Your current materials and priorities will help determine the most useful starting point.'),
('What happens when I prepare an email enquiry?', 'The form opens your email app with your project details addressed to contact@inkworthllc.com. Review the message and send it from your email app. You can also email us directly or call (321) 332-0682.'),
('Can I include a deadline or budget?', 'Yes. Include these in your project description. They help frame a realistic scope; sending an enquiry does not confirm availability, pricing, or a delivery date.')], 'Before you reach out.')

def policy_section(number, title, *blocks, prefix='section'):
    body = ''.join(blocks)
    return f'<article class="policy-section" id="{prefix}-{number}"><h2><span>{number}.</span> {title}</h2>{body}</article>'

def policy_p(text):
    return f'<p>{text}</p>'

def policy_list(items):
    return '<ul>' + ''.join(f'<li>{item}</li>' for item in items) + '</ul>'

def policy_contact_block():
    return '''<div class="policy-contact"><p><strong>Ink Worth LLC</strong></p><p>Email: <a href="mailto:contact@inkworthllc.com">contact@inkworthllc.com</a></p><p>Phone: <a href="tel:+13213320682">(321) 332-0682</a></p><p>Mailing Address: PO Box 680585, Orlando, FL 32868</p></div>'''

privacy_policy = '''<section class="page-intro container"><span class="eyebrow">LEGAL</span><h1>Privacy Policy</h1><p>How Ink Worth LLC collects, uses, stores, protects, and discloses information when you visit our website or use our services.</p><p class="policy-meta">Effective Date: October 14, 2026</p></section><section class="container policy-doc" aria-label="Privacy Policy">''' + ''.join([
policy_section('1', 'Introduction',
    policy_p('Ink Worth LLC (“Ink Worth,” “we,” “our,” or “us”) is committed to respecting your privacy and protecting the personal information you share with us. This Privacy Policy explains how we collect, use, store, protect, and disclose information when you visit our website, contact our team, purchase our services, or communicate with us through telephone calls, SMS text messages, or email.'),
    policy_p('Ink Worth LLC provides professional services related to book publishing, book writing, editing, proofreading, book cover design, and book marketing programs.'),
    policy_p('By using our website or services, you acknowledge that you have had the opportunity to review this Privacy Policy. Where consent is required by law, we will request it separately.')),
policy_section('2', 'Information We Collect',
    policy_p('Depending on how you interact with us, we may collect the following categories of information:'),
    policy_list([
        '<strong>Personal and Contact Information:</strong> Your name, email address, telephone number, mailing address, business information, and other details you voluntarily provide.',
        '<strong>Account and Transaction Information:</strong> Information relating to service inquiries, project proposals, contracts, invoices, payments, purchases, and customer support requests. Payment information may be processed by third-party payment providers.',
        '<strong>Manuscripts and Project Materials:</strong> Book manuscripts, outlines, drafts, research materials, author biographies, photographs, cover concepts, marketing content, publishing preferences, and other materials you provide to us to complete your project.',
        '<strong>Website and Technical Information:</strong> Information such as your IP address, browser type, device information, pages visited, referral sources, and website usage data. Cookies and similar technologies may be used where applicable.',
        '<strong>Communication Information:</strong> Records of communications between you and Ink Worth LLC, including emails, text messages, customer service requests, and relevant project correspondence.'
    ])),
policy_section('3', 'How We Use Your Information',
    policy_p('We may use the information we collect to:'),
    policy_list([
        'Provide and manage book publishing, book writing, editing, proofreading, book cover design, and book marketing services.',
        'Review manuscripts, develop project plans, prepare proposals, and communicate about project progress.',
        'Process transactions, maintain customer accounts, issue invoices, and provide customer support.',
        'Send service-related messages, appointment reminders, project updates, and administrative notifications.',
        'Send promotional emails or text messages where permitted by law and where any required consent has been obtained.',
        'Improve our website, service quality, customer experience, and business operations.',
        'Protect against fraud, unauthorized activity, misuse, and security threats.',
        'Maintain business records and comply with applicable legal obligations.'
    ]),
    policy_p('We will not knowingly use your personal information for purposes materially different from those described here without providing any notice or obtaining any consent required by applicable law.')),
policy_section('4', 'Manuscript Confidentiality and Intellectual Property',
    policy_p('Ink Worth LLC recognizes that unpublished manuscripts, original writing, and creative materials may be highly confidential and valuable to their authors.'),
    policy_p('We use manuscripts and other project materials for legitimate business purposes associated with the services requested by the customer, including writing, editing, proofreading, formatting, design, publishing coordination, and marketing.'),
    policy_p('We do not sell customers’ unpublished manuscripts or intentionally disclose confidential project materials to the public for unrelated commercial purposes.'),
    policy_p('Access to project materials may be provided to authorized employees, contractors, editors, designers, publishing partners, or other service providers when reasonably necessary to perform the requested services, subject to appropriate confidentiality obligations where applicable.'),
    policy_p('Ink Worth LLC does not claim ownership of a customer’s manuscript merely because the customer submits it to us. Ownership, copyright, licensing rights, work-for-hire arrangements, and rights to deliverables will be governed by the applicable written service agreement and relevant law.'),
    policy_p('Customers should review their individual service agreements for specific provisions regarding confidentiality, ownership, copyright transfers, licensing, and the use of completed work in portfolios or promotional materials.')),
policy_section('5', 'Sharing and Disclosure of Information',
    policy_p('Ink Worth LLC does not sell personal information in exchange for money. We may disclose information in the following circumstances:'),
    policy_list([
        '<strong>Service Providers:</strong> We may share necessary information with trusted vendors who support our operations, including website hosting providers, communication platforms, payment processors, cloud storage providers, editors, designers, publishing partners, and marketing service providers.',
        '<strong>Customer Authorization:</strong> We may share information when you expressly authorize us to do so, including when you request assistance with publishing, distribution, advertising, or other third-party services.',
        '<strong>Legal Requirements:</strong> We may disclose information when reasonably necessary to comply with applicable law, legal process, or a lawful request from an authorized government authority.',
        '<strong>Business Protection:</strong> We may use or disclose information when reasonably necessary to investigate suspected fraud, enforce our agreements, protect our legal rights, or safeguard customers, employees, and the public.',
        '<strong>Business Transactions:</strong> Information may be transferred as part of a merger, acquisition, restructuring, or sale of business assets, subject to applicable legal requirements.'
    ]),
    policy_p('We do not authorize service providers to use customer information for purposes unrelated to the services they perform on our behalf, except as otherwise permitted by law.')),
policy_section('6', 'SMS and Email Communications',
    policy_p('Ink Worth LLC may communicate with customers and prospective customers through SMS text messages and email.'),
    policy_p('Service-related communications may include project updates, appointment confirmations, requests for information, billing notices, and customer support responses.'),
    policy_p('Marketing communications may include information about our publishing services, writing and editing packages, book marketing programs, promotional offers, and other relevant services. We will send marketing communications only where permitted by applicable law and subject to any required consent.'),
    policy_p('<strong>SMS consent:</strong> Where applicable, customers will be asked to provide the required consent before receiving marketing text messages. Consent to receive marketing messages is not a condition of purchasing our services.'),
    policy_p('<strong>Message frequency and charges:</strong> Message frequency may vary. Message and data rates may apply depending on your mobile carrier and service plan.'),
    policy_p('<strong>Opting out of text messages:</strong> You may opt out of SMS marketing messages at any time by replying STOP. Other supported opt-out instructions may also be provided in the message. We may send a final confirmation of your opt-out request where permitted.'),
    policy_p('<strong>Email opt-out:</strong> You may unsubscribe from promotional emails using the unsubscribe link included in the message or by contacting us at <a href="mailto:contact@inkworthllc.com">contact@inkworthllc.com</a>. You may continue to receive essential transactional or service-related communications when necessary.'),
    policy_p('<strong>Help:</strong> For assistance with text communications, reply HELP where supported or contact us using the details listed in the Contact Us section.'),
    policy_p('<strong>Mobile information privacy:</strong> Mobile phone numbers and SMS consent information will not be sold or shared with third parties or affiliates for their own marketing or promotional purposes. Information may be shared with service providers that help us deliver messaging services, where necessary for those services, and with other parties when legally permitted or required.')),
policy_section('7', 'Cookies and Website Technologies',
    policy_p('Our website may use cookies, analytics tools, pixels, or similar technologies to support website functionality, understand visitor activity, improve performance, and measure marketing effectiveness.'),
    policy_p('You may be able to manage cookies through your browser settings or any cookie preference tool available on our website. Disabling certain cookies may affect website functionality.'),
    policy_p('Where required by law, we will obtain consent before using non-essential cookies or similar tracking technologies.')),
policy_section('8', 'Data Security',
    policy_p('Ink Worth LLC takes reasonable administrative, technical, and organizational measures designed to protect personal information and project materials against unauthorized access, misuse, loss, alteration, or disclosure.'),
    policy_p('These measures may include access restrictions, secure accounts, confidentiality practices, and the use of reputable service providers.'),
    policy_p('However, no electronic transmission, storage system, or online service can be guaranteed to be completely secure. We therefore cannot promise absolute security, although we will take reasonable steps to protect the information entrusted to us.')),
policy_section('9', 'Data Retention',
    policy_p('We retain personal information, customer records, and project materials for as long as reasonably necessary to provide our services, administer agreements, resolve disputes, maintain business records, comply with legal obligations, and protect our legitimate business interests.'),
    policy_p('Retention periods may vary depending on the type of information, the nature of the project, contractual obligations, and applicable law.'),
    policy_p('When information is no longer reasonably required, we will take appropriate steps to delete, destroy, or de-identify it, subject to applicable legal and operational requirements.')),
policy_section('10', 'Your Privacy Rights',
    policy_p('Depending on your location and applicable law, you may have the right to:'),
    policy_list([
        'Request access to certain personal information we hold about you.',
        'Request correction of inaccurate personal information.',
        'Request deletion of personal information, subject to applicable exceptions.',
        'Withdraw consent where processing is based on consent.',
        'Object to or request restrictions on certain processing activities.',
        'Opt out of marketing communications.',
        'Request information about certain categories of information we collect, use, or disclose.'
    ]),
    policy_p('To exercise an applicable privacy right, contact us at <a href="mailto:contact@inkworthllc.com">contact@inkworthllc.com</a>. We may need to verify your identity before processing a request.'),
    policy_p('We will respond to valid requests in accordance with applicable legal requirements. Certain records may need to be retained for legal, contractual, accounting, security, or dispute-resolution purposes.')),
policy_section('11', 'Third-Party Websites and Services',
    policy_p('Our website or communications may contain links to third-party websites, publishing platforms, payment processors, advertising platforms, or other external services.'),
    policy_p('These third parties may maintain their own privacy policies and terms of use. Ink Worth LLC does not control the privacy practices of independent third parties, and we encourage you to review their policies before submitting information to them.')),
policy_section('12', "Children's Privacy",
    policy_p('Our services are intended for adults and are not knowingly directed to children under 13. We do not knowingly collect personal information online from children under 13 without the parental consent or other authorization required by applicable law.'),
    policy_p('If you believe a child has provided personal information to us inappropriately, please contact us so that we can review the matter and take appropriate action.')),
policy_section('13', 'International Customers',
    policy_p('If you access our website or services from outside the United States, your information may be processed or stored in the United States or other locations where we or our service providers operate.'),
    policy_p('Where applicable law requires specific disclosures, safeguards, or additional rights for international data transfers, we will address those requirements as applicable to our business and the relevant customer relationship.')),
policy_section('14', 'Pseudonym and Customer Communication Policy',
    policy_p('Ink Worth LLC may allow employees, representatives, or customer service personnel to use professional display names or pseudonyms when communicating with customers.'),
    policy_p('This practice may help provide consistent customer service, simplify communication, and maintain a uniform professional experience across teams and regions.'),
    policy_p('A pseudonym is a professional name used for communication purposes and is not intended to misrepresent contractual obligations, conceal legally required business information, or mislead customers about material facts.'),
    policy_p('Where legally required or reasonably necessary for a contract, billing matter, complaint, or formal business transaction, Ink Worth LLC will provide appropriate business or representative information.')),
policy_section('15', 'Changes to This Privacy Policy',
    policy_p('Ink Worth LLC may revise this Privacy Policy periodically to reflect changes in our services, information practices, technology, or legal obligations.'),
    policy_p('The revised version will be posted on our website with an updated “Last Updated” date. Where required by law, we will provide additional notice or seek consent before implementing material changes.'),
    policy_p('We encourage customers to review this policy periodically.')),
policy_section('16', 'Contact Us',
    policy_p('If you have questions, concerns, or requests relating to this Privacy Policy or our information-handling practices, please contact us:'),
    policy_contact_block())
]) + '</section>'

disclaimer = '''<section class="container policy-doc policy-doc--disclaimer" id="disclaimer" aria-label="Disclaimer"><div class="policy-divider"><span class="eyebrow">DISCLAIMER</span><h2>Service Disclaimer</h2><p class="policy-meta">Effective Date: October 14, 2026</p></div>''' + ''.join([
policy_section('1', 'General Disclaimer',
    policy_p('Ink Worth LLC provides book publishing, book writing, editing, proofreading, book cover design, and book marketing services. Information provided on our website, in consultations, through email, or in other business communications is intended for general informational and service-related purposes.'),
    policy_p('Although we make reasonable efforts to provide professional services, we do not guarantee that every service, recommendation, manuscript, design, marketing campaign, or publishing outcome will meet every customer’s expectations or produce a particular result.'),
    prefix='disclaimer'),
policy_section('2', 'Publishing and Distribution Disclaimer',
    policy_p('Publishing and distribution opportunities may depend on third-party platforms, publishers, distributors, retailers, printers, and other organizations.'),
    policy_p('Ink Worth LLC does not guarantee acceptance by any publisher, bookstore, literary agent, retailer, distribution platform, or other third party unless a specific written agreement expressly provides otherwise.'),
    policy_p('Publishing timelines, availability, platform requirements, pricing, distribution coverage, and other third-party conditions may change without our control.'),
    prefix='disclaimer'),
policy_section('3', 'Book Marketing and Sales Disclaimer',
    policy_p('Ink Worth LLC may offer book marketing programs, promotional services, advertising assistance, campaign planning, and related services.'),
    policy_p('We do not guarantee a specific number of book sales, downloads, reviews, followers, readers, rankings, media placements, royalties, revenue, profits, or return on investment.'),
    policy_p('Marketing results depend on multiple factors, including the book’s subject matter, audience demand, pricing, competition, author participation, advertising budgets, platform policies, and market conditions.'),
    policy_p('Any estimates, projections, examples, testimonials, or historical results are illustrative or reflect the circumstances described and should not be interpreted as a promise of future performance.'),
    prefix='disclaimer'),
policy_section('4', 'Writing, Editing, and Proofreading Disclaimer',
    policy_p('Writing, editing, and proofreading services are intended to improve the clarity, structure, presentation, readability, and overall quality of written materials within the scope of the agreed services.'),
    policy_p('Although reasonable care will be taken, no editing or proofreading process can guarantee the complete elimination of all errors, inconsistencies, or inaccuracies.'),
    policy_p('The customer remains responsible for reviewing and approving final manuscripts, factual statements, citations, permissions, and other content before publication.'),
    prefix='disclaimer'),
policy_section('5', 'Copyright and Content Responsibility',
    policy_p('Customers are responsible for ensuring that materials they provide or request us to use do not unlawfully infringe the copyright, trademark, privacy, publicity, or other legal rights of third parties.'),
    policy_p('Customers should obtain appropriate permissions for third-party text, images, photographs, illustrations, quotations, and other protected materials where required.'),
    policy_p('Unless otherwise agreed in a written contract, providing materials to Ink Worth LLC does not automatically transfer ownership of those materials to Ink Worth LLC or transfer ownership of deliverables to the customer. Applicable ownership and licensing terms will be governed by the relevant agreement and law.'),
    prefix='disclaimer'),
policy_section('6', 'Third-Party Platforms and Services',
    policy_p('Ink Worth LLC may coordinate with or refer customers to independent publishers, retailers, printers, advertising platforms, distributors, payment providers, and other third-party services.'),
    policy_p('We are not responsible for independent third-party policies, decisions, platform outages, account suspensions, distribution changes, advertising approvals, or other matters outside our reasonable control, subject to applicable law and any express contractual obligations.'),
    prefix='disclaimer'),
policy_section('7', 'No Legal, Tax, or Financial Advice',
    policy_p('Information provided by Ink Worth LLC is not a substitute for individualized legal, tax, accounting, or financial advice.'),
    policy_p('Customers should consult an appropriately qualified professional regarding copyright ownership, publishing contracts, tax treatment of royalties, business arrangements, intellectual property disputes, and other matters requiring professional advice.'),
    prefix='disclaimer'),
policy_section('8', 'Limitation of Liability',
    policy_p('To the maximum extent permitted by applicable law, Ink Worth LLC will not be liable for indirect, incidental, special, consequential, or punitive damages arising from the use of our website or services, including loss of anticipated profits, sales, or business opportunities.'),
    policy_p('Nothing in this disclaimer excludes or limits liability that cannot legally be excluded or limited. Any additional limitation of liability, refund terms, warranties, or remedies will be governed by the applicable service agreement and relevant law.'),
    prefix='disclaimer'),
policy_section('9', 'Acceptance of Terms',
    policy_p('Use of our website and services is subject to applicable service agreements, project terms, and other policies provided by Ink Worth LLC.'),
    policy_p('If any provision of this disclaimer conflicts with a signed service agreement, the applicable agreement will govern to the extent provided by its terms and permitted by law.'),
    prefix='disclaimer'),
policy_section('10', 'Contact Information',
    policy_p('For questions regarding this disclaimer or our services, contact:'),
    policy_contact_block(),
    prefix='disclaimer')
]) + '</section>'

privacy = privacy_policy + disclaimer
