"""Makes the example data and the two figures for this project page.

Run from this folder:  python3 make_figures.py
The website only uses the files this script writes (data.csv, fig1.png,
fig2.png), so GitHub never has to run Python.
"""
import csv
import random

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

random.seed(42)

# --- Data: fake daily temperature and ice-cream sales ----------------------
rows = []
for day in range(1, 91):
    temp = 15 + 10 * (day / 90) + random.gauss(0, 2)
    sales = 40 + 6 * temp + random.gauss(0, 15)
    rows.append({"day": day, "temperature_c": round(temp, 1), "sales": round(sales)})

with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

days = [r["day"] for r in rows]
temps = [r["temperature_c"] for r in rows]
sales = [r["sales"] for r in rows]

# --- Figure 1: sales over time ----------------------------------------------
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(days, sales, color="#2780e3")
ax.set_xlabel("Day")
ax.set_ylabel("Ice creams sold")
ax.set_title("Daily sales over 90 days")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("fig1.png", dpi=150)

# --- Figure 2: sales vs temperature with a fitted line ---------------------
n = len(temps)
mean_t, mean_s = sum(temps) / n, sum(sales) / n
slope = sum((t - mean_t) * (s - mean_s) for t, s in zip(temps, sales)) / sum(
    (t - mean_t) ** 2 for t in temps
)
intercept = mean_s - slope * mean_t

fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(temps, sales, alpha=0.7, color="#2780e3")
xs = [min(temps), max(temps)]
ax.plot(xs, [intercept + slope * x for x in xs], color="#e3272a",
        label=f"sales ≈ {intercept:.0f} + {slope:.1f} × temp")
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Ice creams sold")
ax.set_title("Warmer days, more sales")
ax.legend(frameon=False)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("fig2.png", dpi=150)

print(f"slope = {slope:.2f} ice creams per °C")
