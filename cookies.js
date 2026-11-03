/* Banner de cookies de CapitalZero (Google Consent Mode v2).
   GTM se carga siempre, pero Analytics no guarda cookies hasta que el visitante acepta. */
(function () {
  var KEY = 'cz_consent';
  var d = document;

  function save(granted) {
    var v = granted ? 'granted' : 'denied';
    try { localStorage.setItem(KEY, v); } catch (e) {}
    window.gtag && gtag('consent', 'update', { analytics_storage: v });
    window.dataLayer && dataLayer.push({ event: 'cz_consent_update', cz_consent: v });
  }

  function show() {
    if (d.getElementById('cz-cookies')) return;
    var css = d.createElement('style');
    css.textContent =
      '#cz-cookies{position:fixed;left:16px;right:16px;bottom:16px;z-index:2147483000;max-width:560px;margin:0 auto;' +
      'background:#06182a;color:#f4e3d1;border:1px solid rgba(244,227,209,.2);border-radius:14px;padding:18px 20px;' +
      'font:15px/1.5 Archivo,system-ui,sans-serif;box-shadow:0 12px 40px rgba(0,0,0,.35)}' +
      '#cz-cookies p{margin:0 0 14px}#cz-cookies div{display:flex;gap:10px;flex-wrap:wrap;justify-content:flex-end}' +
      '#cz-cookies button{font:inherit;font-weight:600;cursor:pointer;border-radius:999px;padding:9px 18px;border:1px solid #f4e3d1}' +
      '#cz-cookies .no{background:transparent;color:#f4e3d1}#cz-cookies .yes{background:#17a2b8;border-color:#17a2b8;color:#06182a}';
    var box = d.createElement('div');
    box.id = 'cz-cookies';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-label', 'Preferencias de cookies');
    box.innerHTML =
      '<p>Usamos cookies de analítica (Google Analytics) para saber cómo se usa la web y mejorarla. ' +
      'Solo se activan si las aceptas.</p>' +
      '<div><button type="button" class="no">Rechazar</button><button type="button" class="yes">Aceptar</button></div>';
    box.querySelector('.yes').onclick = function () { save(true); close(); };
    box.querySelector('.no').onclick = function () { save(false); close(); };
    function close() { box.remove(); css.remove(); }
    d.head.appendChild(css);
    d.body.appendChild(box);
  }

  // Cualquier enlace o botón con data-cookie-settings vuelve a abrir el banner.
  window.czCookieSettings = show;
  d.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('[data-cookie-settings]');
    if (t) {
      e.preventDefault();
      d.querySelectorAll('dialog[open]').forEach(function (x) { x.close(); });
      show();
    }
  });

  var stored = null;
  try { stored = localStorage.getItem(KEY); } catch (e) {}
  if (!stored) {
    if (d.body) show(); else d.addEventListener('DOMContentLoaded', show);
  }
})();
