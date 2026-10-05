"""Draws the two result charts on this page from numbers reported in my MSc thesis.

Run from this folder:  python3 make_figures.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

FOREST, SAGE, ROSE, BLUSH, LAV, BUTTER, CREAM = (
    "#1E2A26", "#1F3A5F", "#A8483B", "#C9D1DB", "#8FA9C8", "#F3F5F8", "#FFFFFF")
plt.rcParams.update({"font.family": "sans-serif", "axes.spines.top": False, "font.size": 13,
                     "axes.edgecolor": FOREST, "text.color": FOREST,
                     "axes.labelcolor": FOREST, "xtick.color": FOREST, "ytick.color": FOREST})

# --- Figure: macro-F1 on the test flight -----------------------------------
labels = ["Always predict\n“healthy”", "Final model", "Final model\n(leak-free texture)"]
scores = [0.308, 0.394, 0.392]
colours = [BLUSH, SAGE, LAV]

fig, ax = plt.subplots(figsize=(8, 4.6), facecolor=CREAM)
ax.set_facecolor(CREAM)
bars = ax.bar(labels, scores, color=colours, edgecolor="none", width=0.6)
for b, s in zip(bars, scores):
    ax.text(b.get_x() + b.get_width() / 2, s + 0.012, f"{s:.3f}", ha="center",
            fontsize=15, fontweight="bold")
ax.axhline(0.308, color=ROSE, linestyle=(0, (5, 4)), linewidth=2)
ax.text(2.42, 0.316, "baseline", color=ROSE, ha="right", fontsize=12, fontweight="bold")
ax.set_ylim(0, 0.5)
ax.set_ylabel("Macro-F1 (3 classes)")
ax.set_title("Macro-F1 on the test flight (permutation test p = 0.004)", fontsize=14,
             fontweight="bold", pad=14)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("fig-scores.png", dpi=180, facecolor=CREAM)

# --- Figure: replicate agreement donut --------------------------------------
fig, ax = plt.subplots(figsize=(5, 5), facecolor=CREAM)
ax.pie([64.2, 35.8], colors=[SAGE, BLUSH], startangle=90, counterclock=False,
       wedgeprops={"width": 0.38, "edgecolor": CREAM, "linewidth": 4})
ax.text(0, 0.08, "35.8%", ha="center", fontsize=30, fontweight="bold", color=ROSE)
ax.text(0, -0.2, "of replicate pairs\ndisagree", ha="center", fontsize=12)
ax.set_title("Agreement between replicate plots", fontsize=14, fontweight="bold")
fig.tight_layout()
fig.savefig("fig-replicates.png", dpi=180, facecolor=CREAM)
