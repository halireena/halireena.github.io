"""Test-set AUCs from our MSc machine-learning group report (neuroblastoma, GSE62564).
Run from this folder:  python3 make_figures.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
NAVY, MID, INK = "#1F3A5F", "#8FA9C8", "#1E2A26"
plt.rcParams.update({"font.family": "sans-serif", "font.size": 12, "axes.edgecolor": INK, "text.color": INK,
                     "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
                     "axes.spines.top": False, "axes.spines.right": False})
outcomes = ["Death", "High risk", "Progression"]
rnaseq, array = [0.886, 0.971, 0.777], [0.901, 0.967, 0.811]
fig, ax = plt.subplots(figsize=(8, 4))
w = 0.36
for k, (vals, lab, c) in enumerate([(rnaseq, "RNA-seq", NAVY), (array, "Microarray", MID)]):
    xs = [i + (k - 0.5) * w for i in range(3)]
    ax.bar(xs, vals, w, label=lab, color=c)
    for x, v in zip(xs, vals):
        ax.text(x, v + 0.01, f"{v:.3f}", ha="center", fontsize=10)
ax.axhline(0.5, color="#A8483B", linestyle=(0, (4, 4)), linewidth=1.5)
ax.text(2.6, 0.515, "chance", color="#A8483B", ha="right", fontsize=10)
ax.set_xticks(range(3)); ax.set_xticklabels(outcomes); ax.set_ylim(0.4, 1.12)
ax.set_ylabel("Test-set AUC"); ax.legend(frameon=False, loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.02))
ax.set_title("Random Forest predictions for 498 neuroblastoma patients", fontsize=12, pad=12)
fig.tight_layout(); fig.savefig("fig-auc.png", dpi=180, facecolor="white")
