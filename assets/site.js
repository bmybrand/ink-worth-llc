const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('#main-nav');
function closeMenu() { menu.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open'); }
menu.addEventListener('click', () => {
  const open = menu.getAttribute('aria-expanded') !== 'true';
  menu.setAttribute('aria-expanded', String(open));
  nav.classList.toggle('is-open', open);
});
document.addEventListener('keydown', event => { if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') { closeMenu(); menu.focus(); } });
document.addEventListener('click', event => { if (!event.target.closest('.site-header')) closeMenu(); });

// Set this to the confirmed business email to enable email enquiries.
const enquiryEmail = '';
const form = document.querySelector('#enquiry-form');
if (form) {
  const chosen = new URLSearchParams(location.search).get('service');
  if (['writing', 'design', 'publishing'].includes(chosen)) form.elements.service.value = chosen;
  if (enquiryEmail) {
    document.querySelector('#submit-enquiry').firstChild.textContent = 'Prepare email enquiry ';
    document.querySelector('#form-hint').textContent = 'Opens your email app with your project details. Review and send your enquiry there.';
  }
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const data = new FormData(form);
    const service = form.elements.service.selectedOptions[0].textContent;
    const brief = `Ink Worth LLC — Project enquiry\n\nName: ${data.get('name')}\nEmail: ${data.get('email')}\nCompany / book: ${data.get('company') || 'Not specified'}\nService: ${service}\n\n${data.get('message')}\n`;
    const status = document.querySelector('#form-status');
    if (enquiryEmail) {
      location.href = `mailto:${enquiryEmail}?subject=${encodeURIComponent('Project enquiry: ' + service)}&body=${encodeURIComponent(brief)}`;
      status.textContent = 'Your enquiry is ready in your email app. Please send it there to complete your request.';
    } else {
      const url = URL.createObjectURL(new Blob([brief], {type: 'text/plain;charset=utf-8'}));
      const link = document.createElement('a');
      link.href = url; link.download = 'ink-worth-project-brief.txt'; link.click();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
      status.textContent = 'Your project brief has been downloaded. It has not been sent to Ink Worth.';
    }
    status.focus();
  });
}

// Content remains readable without JavaScript or animation support.
const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
const sectionAnimations = new Map();
let revealObserver;
function setupMotion() {
  revealObserver?.disconnect();
  sectionAnimations.forEach(animation => animation.cancel());
  sectionAnimations.clear();
  if (motionPreference.matches || !('IntersectionObserver' in window) || !Element.prototype.animate) return;
  revealObserver = new IntersectionObserver(entries => {
    const serviceSequence = new Map();
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const element = entry.target;
      const animation = sectionAnimations.get(element);
      const service = element.closest('.service-detail');
      if (service && animation) {
        const step = serviceSequence.get(service) || 0;
        animation.effect.updateTiming({ delay: Math.min(step, 4) * 140 });
        serviceSequence.set(service, step + 1);
      }
      element.dataset.scrollState = 'revealed';
      animation?.play();
      revealObserver.unobserve(element);
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -45px 0px' });
  const selector = '.section-heading, .service-card, .journey-step, .audience-card, .feature-copy, .feature-photo, .resource-card, .service-photograph, .collaboration-image, .collaboration-copy > *, .collaboration-principle, .mission-note, .service-detail > .detail-number, .service-detail > div > h2, .service-detail > div > p, .service-detail .check-list > li, .service-notes > div, .service-detail > .button';
  document.querySelectorAll(selector).forEach(element => {
    if (element.closest('[hidden], .service-scroll-viewport')) return;
    const isServiceStep = Boolean(element.closest('.service-detail'));
    if (element.dataset.scrollState === 'revealed' || (!isServiceStep && element.getBoundingClientRect().top < innerHeight - 45)) return;
    const isImage = element.matches('.feature-photo, .service-photograph, .collaboration-image');
    const isCard = element.matches('.service-card, .journey-step, .audience-card, .resource-card');
    const index = [...element.parentElement.children].indexOf(element);
    const from = isImage
      ? { opacity: 0, transform: 'scale(.97)', clipPath: 'inset(0 0 12% 0)' }
      : { opacity: 0, transform: 'translateY(38px)', clipPath: 'inset(0)' };
    const animation = element.animate([from, { opacity: 1, transform: 'none', clipPath: 'inset(0)' }], {
      duration: isImage ? 1000 : (isServiceStep ? 700 : 800),
      delay: isCard ? Math.min(index, 3) * 110 : 0,
      easing: 'cubic-bezier(.16,1,.3,1)', fill: 'both'
    });
    animation.pause();
    animation.currentTime = 0;
    animation.onfinish = () => { animation.cancel(); sectionAnimations.delete(element); };
    sectionAnimations.set(element, animation);
    element.dataset.scrollState = 'waiting';
    revealObserver.observe(element);
  });
}
setupMotion();
motionPreference.addEventListener('change', setupMotion);
document.addEventListener('services-scroll-mode', setupMotion);
document.addEventListener('focusin', event => {
  sectionAnimations.forEach((animation, element) => {
    if (element.contains(event.target)) {
      element.dataset.scrollState = 'revealed';
      animation.finish();
      revealObserver?.unobserve(element);
    }
  });
});
