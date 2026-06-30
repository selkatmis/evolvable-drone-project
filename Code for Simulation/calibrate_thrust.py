import pandas as pd
import numpy as np

# ==========================================================
# SETTINGS
# ==========================================================

INPUT_FILE = r"C:\Users\akshi\OneDrive\Documents\Thesis Project - Evolvable Drones\Thrust input\test 3 all_thrust.csv"

OUTPUT_FILE = r"C:\Users\akshi\OneDrive\Documents\Thesis Project - Evolvable Drones\Thrust input\test 3_thrust_calibrated.csv"

DRONE_MASS = 0.251      # kg
GRAVITY = 9.81

# ==========================================================
# LOAD THRUST CSV
# ==========================================================

df = pd.read_csv(INPUT_FILE, header=None)

df.columns = [
    "motor0",
    "motor1",
    "motor2",
    "motor3"
]

# ==========================================================
# CURRENT THRUST
# ==========================================================

current_total = (
    df["motor0"].mean()
    + df["motor1"].mean()
    + df["motor2"].mean()
    + df["motor3"].mean()
)

required_total = DRONE_MASS * GRAVITY

scale_factor = required_total / current_total

print("=" * 50)
print("THRUST CALIBRATION")
print("=" * 50)

print(f"Current total thrust : {current_total:.4f} N")
print(f"Required hover thrust: {required_total:.4f} N")
print(f"Scale factor         : {scale_factor:.3f}")

# ==========================================================
# APPLY SCALE
# ==========================================================

df *= scale_factor

# ==========================================================
# SAVE
# ==========================================================

df.to_csv(
    OUTPUT_FILE,
    header=False,
    index=False
)

print()
print("Saved calibrated thrust file:")
print(OUTPUT_FILE)

print()
print("New mean thrusts:")

for c in df.columns:
    print(c, df[c].mean())

print("Total:", df.sum(axis=1).mean())