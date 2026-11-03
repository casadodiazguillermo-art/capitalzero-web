# CapitalZero · web

Sitio estático de CapitalZero (Escuela de Inversión). Se publica en Netlify: cada cambio en la rama `main` se despliega solo.

| URL | Archivo |
|---|---|
| `/` | `index.html` (home 3D) |
| `/blog/balance/` | `blog/balance/index.html` |
| `/blog/diversificacion/` | `blog/diversificacion/index.html` |
| `/blog/buffett/` | `blog/buffett/index.html` |
| `/leccion/` | `leccion/index.html` |
| `/quienes-somos/` | `quienes-somos/index.html` |

No hay paso de compilación: Netlify publica la carpeta raíz tal cual (ver `netlify.toml`).

Si cambia el dominio, actualiza la URL en `canonical`, `og:url`, el JSON-LD, `sitemap.xml` y `robots.txt`.
