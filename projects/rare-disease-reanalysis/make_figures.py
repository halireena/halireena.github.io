"""Figures for this page, drawn from the results reported in the project README:
https://github.com/halireena/abiomix-rare-disease-prioritisation
Run from this folder:  python3 make_figures.py
"""
import html
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

NAVY, GREY, INK, MUTED, LINE, TINT = "#1F3A5F", "#C9D1DB", "#1E2A26", "#5B6B64", "#DDE3EA", "#F3F5F8"
plt.rcParams.update({"font.family": "sans-serif", "font.size": 12, "axes.edgecolor": INK, "text.color": INK,
                     "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
                     "axes.spines.top": False, "axes.spines.right": False})

labels = ["Variant rows in\nthe raw dataset", "Unique variants after\ncleaning and deduplication", "Variants used to check\nthe ACMG kernel vs ClinVar"]
values = [7_700_000, 430_284, 84_000]
fig, ax = plt.subplots(figsize=(9, 3.8))
ax.barh(labels, values, color=[GREY, NAVY, NAVY], height=0.55)
ax.set_xscale("log"); ax.set_xlim(1e4, 3e7); ax.invert_yaxis()
for y, v in enumerate(values):
    ax.text(v * 1.15, y, f"{v:,}" if v != 84_000 else "84,000+", va="center", fontweight="bold")
ax.set_xlabel("Number of variants (log scale)")
ax.set_title("From 7.7 million rows to an auditable candidate list · 96.3% concordance with ClinVar", fontsize=12)
fig.tight_layout(); fig.savefig("fig-funnel.png", dpi=180, facecolor="white")

steps = [("1 · Ingest", ["parse, QC,", "deduplicate"]), ("2 · HPO", ["phenotypes from", "clinical notes"]),
         ("3 · Annotate", ["gnomAD, ClinVar,", "REVEL, SpliceAI"]), ("4 · ACMG", ["rule-based", "SQL kernel"]),
         ("5 · Rerank", ["phenotype ×", "genotype score"]), ("6 · Decide", ["Reportable /", "Review / Insufficient"]),
         ("7 · Literature", ["evidence for", "lead candidate"])]
w, bw = 1100, 132
gap = (w - 40 - len(steps) * bw) / (len(steps) - 1)
out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 240" font-family="Inter, Helvetica, Arial, sans-serif" role="img" aria-label="Seven-stage rare-disease re-analysis pipeline">',
       f'<rect width="{w}" height="240" fill="#FFFFFF"/>']
for i, (t, sub) in enumerate(steps):
    x = 20 + i * (bw + gap)
    out.append(f'<rect x="{x:.0f}" y="45" width="{bw}" height="115" rx="6" fill="{TINT}" stroke="{LINE}" stroke-width="1.5"/><rect x="{x:.0f}" y="45" width="{bw}" height="6" rx="3" fill="{NAVY}"/>')
    out.append(f'<text x="{x+bw/2:.0f}" y="88" text-anchor="middle" font-size="14" font-weight="600" fill="{INK}">{html.escape(t)}</text>')
    for j, line in enumerate(sub):
        out.append(f'<text x="{x+bw/2:.0f}" y="{112+j*18}" text-anchor="middle" font-size="12" fill="{MUTED}">{html.escape(line)}</text>')
    if i < len(steps) - 1:
        a, b = x + bw + 3, x + bw + gap - 3
        out.append(f'<path d="M{a:.0f} 102 H {b:.0f}" stroke="{NAVY}" stroke-width="2"/><path d="M{b-6:.0f} 97 L {b:.0f} 102 L {b-6:.0f} 107" fill="none" stroke="{NAVY}" stroke-width="2"/>')
out.append(f'<text x="{w/2:.0f}" y="205" text-anchor="middle" font-size="13" fill="{MUTED}">Synthetic dataset provided by Abiomix · 138 cases, 119 families · no real patient data</text></svg>')
open("pipeline.svg", "w").write("\n".join(out))
