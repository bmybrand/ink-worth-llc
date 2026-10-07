// Preserve the full-width articles; scroll moves them through a sticky window.
(() => {
  const content = document.querySelector('.service-details');
  if (!content) return;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const room = matchMedia('(min-width: 360px) and (min-height: 600px)');
  const scrollRate = 1.1;
  const inset = () => parseFloat(getComputedStyle(viewport).top) || 0;
  let track, viewport, distance = 0, queued = false;
  const clamp = (value, max) => Math.max(0, Math.min(max, value));
  const start = () => track.getBoundingClientRect().top + scrollY - inset();

  function render() {
    queued = false;
    if (!track) return;
    const offset = clamp((scrollY - start()) / scrollRate, distance);
    content.style.transform = `translate3d(0, ${-offset}px, 0)`;
    track.dataset.contentOffset = String(offset);
  }
  function schedule() {
    if (!track || queued) return;
    queued = true;
    requestAnimationFrame(render);
  }
  function measure() {
    if (!track) return;
    distance = Math.max(0, content.offsetHeight - viewport.clientHeight);
    track.style.height = `${viewport.offsetHeight + distance * scrollRate}px`;
    render();
  }
  function showElement(element, padding = 35) {
    if (!track || !content.contains(element)) return;
    const y = element.getBoundingClientRect().top - content.getBoundingClientRect().top;
    scrollTo({ top: start() + clamp(y - padding, distance) * scrollRate, behavior: 'instant' });
    render();
  }
  function followHash() {
    if (!track || !location.hash) return;
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const target = document.getElementById(id);
    if (target && content.contains(target)) showElement(target, 0);
  }
  function enable() {
    track = document.createElement('div');
    track.className = 'service-scroll-track container';
    viewport = document.createElement('div');
    viewport.className = 'service-scroll-viewport';
    content.before(track);
    track.append(viewport);
    viewport.append(content);
    document.dispatchEvent(new Event('services-scroll-mode'));
    measure();
    requestAnimationFrame(followHash);
  }
  function disable() {
    if (!track) return;
    track.before(content);
    content.style.removeProperty('transform');
    track.remove();
    track = null;
    document.dispatchEvent(new Event('services-scroll-mode'));
  }
  function configure() {
    if (reduced.matches || !room.matches) disable();
    else if (!track) enable();
    else measure();
  }
  // Bring clipped keyboard targets and service links into the visible window.
  content.addEventListener('focusin', event => {
    if (!track) return;
    const rect = event.target.getBoundingClientRect();
    const bounds = viewport.getBoundingClientRect();
    if (rect.top < bounds.top + 10 || rect.bottom > bounds.bottom - 10) showElement(event.target, 60);
  });
  addEventListener('scroll', schedule, { passive: true });
  addEventListener('resize', configure);
  addEventListener('hashchange', followHash);
  addEventListener('load', () => { measure(); followHash(); }, { once: true });
  reduced.addEventListener('change', configure);
  new ResizeObserver(measure).observe(content);
  configure();
  document.fonts.ready.then(measure);
})();
