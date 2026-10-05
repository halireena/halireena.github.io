"""Draws the figures on this page from the results reported in the project README:
https://github.com/halireena/E-MTAB-2990-Potato-Phosphate-Transcriptomics
Run from this folder:  python3 make_figures.py
"""
import html
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

NAVY, LIGHT, GREY, INK, MUTED, LINE, TINT = "#1F3A5F", "#8FA9C8", "#C9D1DB", "#1E2A26", "#5B6B64", "#DDE3EA", "#F3F5F8"
plt.rcParams.update({"font.family": "sans-serif", "font.size": 12, "axes.edgecolor": INK,
                     "text.color": INK, "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
                     "axes.spines.top": False, "axes.spines.right": False})

# Figure 1: DEGs in Maris Piper, and the two phosphate gene families
fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.2), gridspec_kw={"width_ratios": [1, 1.3]})
up, down = 208, 77   # 285 DEGs, 73% upregulated
a.bar(["Up", "Down"], [up, down], color=[NAVY, GREY], width=0.6)
for x, v in enumerate([up, down]):
    a.text(x, v + 4, str(v), ha="center", fontweight="bold")
a.set_ylabel("Differentially expressed genes")
a.set_title("Maris Piper, low vs regular phosphate\n285 DEGs (BH-adjusted p < 0.05)", fontsize=12)
fams = ["Acid phosphatases", "PHT1 phosphate\ntransporters"]
b.barh(fams, [11, 6], color=NAVY, height=0.55, label="Upregulated")
for y, v in enumerate([11, 6]):
    b.text(v + 0.2, y, f"{v} of {v} detected", va="center")
b.set_xlim(0, 15); b.invert_yaxis()
b.set_xlabel("Genes")
b.set_title("Every detected family member was upregulated", fontsize=12)
fig.tight_layout()
fig.savefig("fig-degs.png", dpi=180, facecolor="white")

# Figure 2: cultivar specificity
fig, ax = plt.subplots(figsize=(8, 3.6))
ax.barh(["Shared by all four cultivars", "Unique to Maris Piper"], [137, 555], color=[GREY, NAVY], height=0.55)
for y, v in enumerate([137, 555]):
    ax.text(v + 8, y, str(v), va="center", fontweight="bold")
ax.set_xlim(0, 640)
ax.set_xlabel("Differentially expressed genes (8-group cross-cultivar model)")
ax.set_title("Most of the Maris Piper response is cultivar-specific", fontsize=12)
fig.tight_layout()
fig.savefig("fig-cultivars.png", dpi=180, facecolor="white")

# Pipeline schematic
steps = [("1 · QC", ["load, normalise,", "filter probes"]), ("2 · limma", ["differential", "expression"]),
         ("3 · Enrichment", ["GO via biomaRt +", "clusterProfiler"]), ("4 · Cross-cultivar", ["8-group model,", "heatmaps"]),
         ("5 · Evolution", ["ABCB gene tree,", "21 Solanaceae"])]
w, h, bw = 960, 250, 160
gap = (w - 40 - len(steps) * bw) / (len(steps) - 1)
out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="Inter, Helvetica, Arial, sans-serif" role="img" aria-label="Five-stage R pipeline">',
       f'<rect width="{w}" height="{h}" fill="#FFFFFF"/>']
for i, (t, sub) in enumerate(steps):
    x = 20 + i * (bw + gap)
    out.append(f'<rect x="{x:.0f}" y="50" width="{bw}" height="120" rx="6" fill="{TINT}" stroke="{LINE}" stroke-width="1.5"/>')
    out.append(f'<rect x="{x:.0f}" y="50" width="{bw}" height="6" rx="3" fill="{NAVY}"/>')
    out.append(f'<text x="{x+bw/2:.0f}" y="95" text-anchor="middle" font-size="15" font-weight="600" fill="{INK}">{html.escape(t)}</text>')
    for j, line in enumerate(sub):
        out.append(f'<text x="{x+bw/2:.0f}" y="{120+j*19}" text-anchor="middle" font-size="13" fill="{MUTED}">{html.escape(line)}</text>')
    if i < len(steps) - 1:
        ax_, bx = x + bw + 6, x + bw + gap - 6
        out.append(f'<path d="M{ax_:.0f} 110 H {bx:.0f}" stroke="{NAVY}" stroke-width="2"/><path d="M{bx-8:.0f} 104 L {bx:.0f} 110 L {bx-8:.0f} 116" fill="none" stroke="{NAVY}" stroke-width="2"/>')
out.append(f'<text x="{w/2:.0f}" y="220" text-anchor="middle" font-size="13" fill="{MUTED}">E-MTAB-2990 · Agilent potato 60K array · 4 cultivars × 2 phosphate conditions × 3 replicates = 24 root samples</text></svg>')
open("pipeline.svg", "w").write("\n".join(out))
