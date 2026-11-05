"""Burundi 2025 reform: which new commune(s) each of the 119 old communes went to.

Each new hill (colline) is located, by its point, inside the old commune
polygons; the hills' areas are summed per (old commune, new commune) pair.
No name matching is used, so hills with the same name do not matter.

Inputs (not in the repository; public data, see RESEARCH_LOG.md, 5 Nov 2026):
  old_adm1.geojson, old_adm2.geojson  geoBoundaries gbOpen BDI ADM1 and ADM2
      (2007 boundaries, 18 provinces and 119 communes; public domain)
  new.json  HDX cod-ab-bdi v02 (Bureau de Centralisation de Géomatique, 2026,
      CC BY-IGO), bdi_admin_boundaries.xlsx converted to JSON (sheet -> rows)

Run: python scripts/burundi_crosswalk.py old_adm1.geojson old_adm2.geojson new.json out.json
"""
import json, sys
from collections import defaultdict

adm1 = json.load(open(sys.argv[1]))["features"]
adm2 = json.load(open(sys.argv[2]))["features"]
x = json.load(open(sys.argv[3]))

def rows(sheet):
    h = x[sheet][0]
    return [{h[k]: v for k, v in r.items() if k in h} for r in x[sheet][1:]]

def rings(geom):
    polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
    return polys

def inside(pt, geom):
    px, py = pt
    for poly in rings(geom):
        ext, holes = poly[0], poly[1:]
        def inring(r):
            c = False; j = len(r) - 1
            for i in range(len(r)):
                xi, yi = r[i][:2]; xj, yj = r[j][:2]
                if (yi > py) != (yj > py) and px < (xj - xi) * (py - yi) / (yj - yi) + xi:
                    c = not c
                j = i
            return c
        if inring(ext) and not any(inring(h) for h in holes):
            return True
    return False

def bbox(geom):
    xs = [p[0] for poly in rings(geom) for p in poly[0]]; ys = [p[1] for poly in rings(geom) for p in poly[0]]
    return min(xs), min(ys), max(xs), max(ys)

def locate(pt, feats):
    for f in feats:
        b = f["_bbox"]
        if b[0] <= pt[0] <= b[2] and b[1] <= pt[1] <= b[3] and inside(pt, f["geometry"]):
            return f
    return None

for f in adm1 + adm2:
    f["_bbox"] = bbox(f["geometry"])
# old province of each old commune: province containing a vertex-average point of the commune
for f in adm2:
    ext = rings(f["geometry"])[0][0]
    c = (sum(p[0] for p in ext) / len(ext), sum(p[1] for p in ext) / len(ext))
    if not inside(c, f["geometry"]):
        c = tuple(ext[0][:2])
    p = locate(c, adm1)
    f["_prov"] = p["properties"]["shapeName"] if p else "?"

hills = {r["adm4_pcode"]: r for r in rows("bdi_admin4")}
points = {r["adm4_pcode"]: r for r in rows("bdi_adminpoints") if r.get("adm4_pcode") and r.get("x_coord")}
share = defaultdict(lambda: defaultdict(float)); total = defaultdict(float)
unplaced = []
for pc, h in hills.items():
    p = points.get(pc)
    if not p:
        unplaced.append(h["adm4_name"]); continue
    old = locate((float(p["x_coord"]), float(p["y_coord"])), adm2)
    if not old:
        unplaced.append(h["adm4_name"]); continue
    key = (old["_prov"], old["properties"]["shapeName"])
    a = float(h.get("area_sqkm") or 0)
    share[key][(h["adm1_name"], h["adm2_name"])] += a; total[key] += a
out = []
for key in sorted(share):
    parts = sorted(((v / total[key], new) for new, v in share[key].items()), reverse=True)
    out.append({"old_province": key[0], "old_commune": key[1],
                "new": [{"province": n[0], "commune": n[1], "share": round(s, 3)} for s, n in parts]})
json.dump({"crosswalk": out, "unplaced_hills": unplaced}, open(sys.argv[4], "w"), ensure_ascii=False, indent=1)
print(len(hills), "new hills;", len(points), "with points;", len(unplaced), "unplaced;", len(out), "old communes reached")
