#!/usr/bin/env python3
"""Generate assets/contributions.svg: every day with a contribution is one colour,
days without are plain half-white. Uses the GitHub GraphQL API when GITHUB_TOKEN is
set (what the workflow does), otherwise falls back to the public ghchart.rshah.org data."""
import json, os, re, sys, urllib.request, datetime as dt

USER = os.environ.get("GH_USER", "Gowrikamahesh17")
OUT = os.environ.get("OUT", "assets/contributions.svg")
ACTIVE, EMPTY, LABEL, BORDER, BG = "#701A3D", "#F8F0F3", "#E5B5C7", "#701A3D", "#190B12"

def from_graphql(token):
    q = '{user(login:"%s"){contributionsCollection{contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}}}' % USER
    req = urllib.request.Request("https://api.github.com/graphql", json.dumps({"query": q}).encode(),
        {"Authorization": f"bearer {token}", "Content-Type": "application/json", "User-Agent": "contrib-svg"})
    cal = json.load(urllib.request.urlopen(req))["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    days = {d["date"]: d["contributionCount"] for w in cal["weeks"] for d in w["contributionDays"]}
    return days, cal["totalContributions"]

def from_ghchart():
    req = urllib.request.Request(f"https://ghchart.rshah.org/{USER}", headers={"User-Agent": "contrib-svg"})
    svg = urllib.request.urlopen(req).read().decode()
    days = {d: int(s) for s, d in re.findall(r'data-score="(\d+)" data-date="([\d-]+)"', svg)}
    return days, None

token = os.environ.get("GITHUB_TOKEN")
days, total = from_graphql(token) if token else from_ghchart()
dates = sorted(dt.date.fromisoformat(d) for d in days)
start = dates[0] - dt.timedelta(days=(dates[0].weekday() + 1) % 7)  # week starts Sunday
P, C, L, T = 14, 11, 44, 40
weeks = (dates[-1] - start).days // 7 + 1
W, H = L + weeks * P + 24, T + 7 * P + 44
o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="GitHub contributions in the last year">',
     f'<rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="14" fill="{BG}" stroke="{BORDER}" stroke-width="1.5"/>',
     '<g font-family="Helvetica, Arial, sans-serif" font-size="11">']
for i, name in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
    o.append(f'<text x="12" y="{T + i*P + 9}" fill="{LABEL}" fill-opacity=".8">{name}</text>')
last_m = None
for w in range(weeks):
    d0 = start + dt.timedelta(weeks=w)
    if d0.month != last_m:
        o.append(f'<text x="{L + w*P}" y="{T - 10}" fill="{LABEL}" fill-opacity=".8">{d0.strftime("%b")}</text>')
        last_m = d0.month
    for r in range(7):
        d = d0 + dt.timedelta(days=r)
        k = d.isoformat()
        if k not in days: continue
        on = days[k] > 0
        fill, op = (ACTIVE, 1) if on else (EMPTY, .55)
        o.append(f'<rect x="{L + w*P}" y="{T + r*P}" width="{C}" height="{C}" rx="2" fill="{fill}" fill-opacity="{op}"{" stroke=\"#C77B9B\" stroke-width=\"1.2\"" if on else ""}><title>{k}: {"contributions" if on else "none"}</title></rect>')
ly = T + 7 * P + 24
label = f"{total} contributions in the last year" if total is not None else "Contributions in the last year"
o.append(f'<text x="{L}" y="{ly}" fill="{LABEL}">{label}</text>')
o.append(f'<rect x="{W-24-90}" y="{ly-10}" width="{C}" height="{C}" rx="2" fill="{EMPTY}" fill-opacity=".55"/><text x="{W-24-74}" y="{ly}" fill="{LABEL}" fill-opacity=".8">none</text>')
o.append(f'<rect x="{W-24-38}" y="{ly-10}" width="{C}" height="{C}" rx="2" fill="{ACTIVE}" stroke="#C77B9B" stroke-width="1.2"/><text x="{W-24-22}" y="{ly}" fill="{LABEL}" fill-opacity=".8">some</text>')
o.append('</g></svg>')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write("\n".join(o))
print("wrote", OUT, "days:", len(days), "active:", sum(1 for v in days.values() if v > 0))
