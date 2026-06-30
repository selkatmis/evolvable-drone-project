import matplotlib.pyplot as plt
import numpy as np

# ==========================================================
# DATA
# ==========================================================

metrics = [
    "Mean Rotor\nSpeed",
    "Angular\nRMS",
    "Maximum\nAngular Rate"
]

old = np.array([
    256.15,
    59.92,
    641.58
])

improved = np.array([
    372.62,
    321.89,
    2353.57
])

# ==========================================================
# NORMALISE
# Best-performing design = 100%
# ==========================================================

maximum = np.maximum(old, improved)

old_norm = old / maximum * 100
improved_norm = improved / maximum * 100

# ==========================================================
# PLOT
# ==========================================================

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11
})

x = np.arange(len(metrics))
width = 0.34

fig, ax = plt.subplots(figsize=(8,5))

bars1 = ax.bar(
    x - width/2,
    old_norm,
    width,
    label="Original Design",
    color="#C00000",
    edgecolor="black"
)

bars2 = ax.bar(
    x + width/2,
    improved_norm,
    width,
    label="Improved Design",
    color="#4472C4",
    edgecolor="black"
)

# ==========================================================
# FORMAT
# ==========================================================

ax.set_ylim(0,110)

ax.set_ylabel("Normalized Value (%)")

ax.set_xticks(x)
ax.set_xticklabels(metrics)

ax.set_title(
    "Comparison of Original and Improved Drone Design",
    fontsize=14,
    weight="bold"
)

ax.grid(
    axis="y",
    linestyle="--",
    alpha=0.35
)

ax.legend()

# ==========================================================
# PERCENT LABELS
# ==========================================================

for bars in [bars1, bars2]:

    for bar in bars:

        h = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width()/2,
            h + 2,
            f"{h:.0f}%",
            ha="center",
            fontsize=10
        )

plt.tight_layout()

plt.savefig(
    "Drone_Design_Comparison_Normalised.png",
    dpi=600,
    bbox_inches="tight"
)

plt.show()