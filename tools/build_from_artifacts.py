import re, os, sys
SRC="/mnt/project-files/web"; OUT=sys.argv[1]; SITE=sys.argv[2].rstrip("/")
pages = {  # artifact id: (source file, site path)
 "3gM9mg26EmeKmGeDHQgUyQ": ("home-3d.html", "/"),
 "2zjUyQswDQKE1qTtixobHq": ("blog-balance.html", "/blog/balance/"),
 "VhAGGSnLxXwyP2Yuy5hVUG": ("blog-diversificacion.html", "/blog/diversificacion/"),
 "DDSwgJRSGwUu7ohFXy547g": ("blog-buffett.html", "/blog/buffett/"),
 "J8PZRajXv1EKYyFtKAAVT4": ("leccion.html", "/leccion/"),
 "L2M1kTg8fszpcpUsK77tgV": ("quienes-somos.html", "/quienes-somos/"),
}
HEAD = '<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">\n'
for aid,(src,path) in pages.items():
    h=open(os.path.join(SRC,src),encoding="utf-8").read()
    # internal links: same tab, site-relative
    def link(m):
        p=pages[m.group(1)][1]; frag=m.group(2) or ""
        if p=="/" and frag and m.group(1)==aid: return f'href="{frag}"'
        return f'href="{p}{frag}"'
    h=re.sub(r'href="https://claude\.ai/artifact/([A-Za-z0-9]{22})(#[^"]*)?"(?: target="_blank" rel="noopener")?', link, h)
    # remaining absolute refs (canonical, og:url, JSON-LD, share links)
    h=re.sub(r'https://claude\.ai/artifact/([A-Za-z0-9]{22})', lambda m: SITE+pages[m.group(1)][1], h)
    h=h.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
    if not h.lstrip().lower().startswith("<!doctype"):
        h=HEAD+h.lstrip()+"\n</body>\n</html>\n" if "</body>" not in h else HEAD+h
    left=re.findall(r'claude\.ai/artifact/\w+',h)
    assert not left,(src,left)
    d=os.path.join(OUT,path.strip("/")); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,"index.html"),"w",encoding="utf-8").write(h)
    print(path, len(h))
urls="".join(f"  <url><loc>{SITE}{p}</loc></url>\n" for _,p in pages.values())
open(os.path.join(OUT,"sitemap.xml"),"w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
