document.addEventListener('submit', function (e) {
  var f = e.target;
  if (f && f.classList && f.classList.contains('signup-form') && typeof gtag === 'function') {
    gtag('event', 'generate_lead', {form: 'newsletter', transport_type: 'beacon'});
  }
}, true);
