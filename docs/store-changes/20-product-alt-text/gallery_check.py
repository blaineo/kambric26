#!/usr/bin/env python3
"""Batch 20: which photos (and alts) each print's gallery shows, per product page.
  gallery_check.py snapshot <out.json> [base]   (base defaults to https://kambricgoods.com)
  gallery_check.py diff <a.json> <b.json>       photo lists must match; alts are listed for review"""
import json, os, re, sys, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
def gallery(html):
    i = html.find('data-gallery-track'); j = html.find('product-gallery__thumbs', i)
    seg = re.sub(r'<noscript>.*?</noscript>', '', html[i:j if j > 0 else None], flags=re.S)
    out = []
    for tag in re.findall(r'<img[^>]*product-gallery__image[^>]*>', seg):
        src = re.search(r'(?:data-defer-)?src="([^"]+)"', tag).group(1)
        alt = re.search(r'alt="([^"]*)"', tag)
        out.append([src.split('/')[-1].split('?')[0], alt.group(1) if alt else None])
    return out
if sys.argv[1] == 'snapshot':
    base = sys.argv[3] if len(sys.argv) > 3 else 'https://kambricgoods.com'
    res = {}
    for h, pr, vid in json.load(open(os.path.join(HERE, 'gallery-urls.json'))):
        req = urllib.request.Request(f'{base}/products/{h}?variant={vid}', headers={'User-Agent': 'kg-batch20'})
        res[f'{h} | {pr}'] = gallery(urllib.request.urlopen(req).read().decode())
    json.dump(res, open(sys.argv[2], 'w'), indent=1, ensure_ascii=False)
    print(sum(len(v) for v in res.values()), 'gallery photos across', len(res), 'prints')
else:
    a, b = (json.load(open(f)) for f in sys.argv[2:4]); bad = 0
    for k in a:
        fa, fb = [x[0] for x in a[k]], [x[0] for x in b.get(k, [])]
        if fa != fb: bad += 1; print('PHOTOS CHANGED', k, fa, fb)
        for (f, alt) in b.get(k, []): print(f'  {k}: {alt}')
    print('OK: same photos for every print' if not bad else f'{bad} prints changed'); sys.exit(1 if bad else 0)
