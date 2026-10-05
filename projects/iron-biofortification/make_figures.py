"""Iron content of each study group, measured by atomic absorption spectrophotometry.
Values are the averages in Table 34 of my BSc dissertation (Northumbria University, 2024).
Run from this folder:  python3 make_figures.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

NAVY, MID, GREY, INK = "#1F3A5F", "#8FA9C8", "#C9D1DB", "#1E2A26"
plt.rcParams.update({"font.family": "sans-serif", "font.size": 12, "axes.edgecolor": INK, "text.color": INK,
                     "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
                     "axes.spines.top": False, "axes.spines.right": False})

systems = ["Kangkung\nNFT", "Mukunuwenna\nNFT", "Mukunuwenna\ncoconut coir"]
iron = {  # ppm: control (162.5 ppm Fe), 200 ppm Fe, 250 ppm Fe
    "Control (162.5 ppm)": [6.0, 18.5, 5.5],
    "200 ppm iron":        [5.3, 15.0, 19.2],
    "250 ppm iron":        [19.5, 11.7, 20.3],
}
colours = [GREY, MID, NAVY]
fig, ax = plt.subplots(figsize=(9, 4.6))
w = 0.26
for k, (label, vals) in enumerate(iron.items()):
    xs = [i + (k - 1) * w for i in range(3)]
    ax.bar(xs, vals, w, label=label, color=colours[k])
    for x, v in zip(xs, vals):
        ax.text(x, v + 0.4, f"{v:g}", ha="center", fontsize=10)
ax.set_xticks(range(3)); ax.set_xticklabels(systems)
ax.set_ylabel("Iron in plant tissue (ppm)")
ax.set_ylim(0, 24)
ax.legend(frameon=False, title="Nutrient solution", loc="upper left", ncol=3, fontsize=10, title_fontsize=10)
ax.set_title("Iron taken up by each cultivation system at three iron levels", fontsize=12)
fig.tight_layout()
fig.savefig("fig-iron.png", dpi=180, facecolor="white")
