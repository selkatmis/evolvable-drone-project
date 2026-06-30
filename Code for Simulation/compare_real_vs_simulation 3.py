
import os
import numpy as np
import pandas as pd

# ==========================================================
# EDIT THESE PATHS ONLY IF YOUR FOLDERS MOVE
# ==========================================================

REAL_SUMMARY = r"C:\Users\akshi\OneDrive\Documents\Thesis Project - Evolvable Drones\Blackbox analysis\Results\summary.csv"

SIM_FOLDER = r"C:\Users\akshi\OneDrive\Documents\Thesis Project - Evolvable Drones\Simulation\Simulation csvs\Calibrated results"
OUTPUT_FOLDER = r"C:\Users\akshi\OneDrive\Documents\Thesis Project - Evolvable Drones\Comparison Results"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ==========================================================
# LOAD REAL SUMMARY
# ==========================================================

real = pd.read_csv(REAL_SUMMARY)
real.columns = real.columns.str.strip()

print("Loaded summary.")
print(real["Flight"])

rows = []

# ==========================================================
# LOOP OVER SIMULATION FILES
# ==========================================================

for sim_file in sorted(os.listdir(SIM_FOLDER)):

    if not sim_file.lower().endswith(".csv"):
        continue

    print(f"\nProcessing {sim_file}")

    sim = pd.read_csv(os.path.join(SIM_FOLDER, sim_file))

    name = sim_file.lower()

    if "test 1" in name:
        match = "test 1"
    elif "test 2" in name:
        match = "test 2"
    elif "test 3" in name:
        match = "test 3 all"
    else:
        print("Skipping:", sim_file)
        continue

    real_row = real[
        real["Flight"].str.lower().str.contains(match)
    ].iloc[0]

    # ---------- Simulation metrics ----------

    duration_sim = float(sim["time"].iloc[-1])

    ang = np.sqrt(
        sim["wx"]**2 +
        sim["wy"]**2 +
        sim["wz"]**2
    )

    angular_rms_sim = float(np.sqrt(np.mean(ang**2)))
    angular_max_sim = float(np.max(ang))

    speed = np.sqrt(
        sim["vx"]**2 +
        sim["vy"]**2 +
        sim["vz"]**2
    )

    mean_speed = float(np.mean(speed))
    max_speed = float(np.max(speed))

    hover_time = float(np.sum(sim["z"] < -0.05) * 0.005)

    duration_real = float(real_row["Duration (s)"])

    duration_error = abs(duration_sim-duration_real)/duration_real*100

    rows.append({

        "Flight": real_row["Flight"],

        "Real Duration (s)": duration_real,
        "Simulation Duration (s)": duration_sim,
        "Duration Error (%)": duration_error,

        "Real Mean RPM": real_row["RPM Mean"],
        "Real Max RPM": real_row["RPM Max"],

        "Real Motor Mean": real_row["Motor Mean"],
        "Real Motor Balance": real_row["Motor Std Between"],

        "Real Angular RMS": real_row["Angular Rate RMS"],
        "Simulation Angular RMS": angular_rms_sim,

        "Real Angular Max":
            max(
                real_row["gyroADC[0] Max"],
                real_row["gyroADC[1] Max"],
                real_row["gyroADC[2] Max"]
            ),

        "Simulation Angular Max": angular_max_sim,

        "Simulation Mean Speed": mean_speed,
        "Simulation Max Speed": max_speed,

        "Simulation Hover Time (s)": hover_time,

        "Battery Start": real_row["Battery Start"],
        "Battery End": real_row["Battery End"],
        "Battery Drop": real_row["Battery Drop"],

        "Mean Power": real_row["Power Mean"]

    })

# ==========================================================
# SAVE RESULTS
# ==========================================================

comparison = pd.DataFrame(rows)

comparison = comparison.sort_values("Flight").reset_index(drop=True)

outfile = os.path.join(
    OUTPUT_FOLDER,
    "Final_Calibrated_Comparison_Table.csv"
)

comparison.to_csv(outfile, index=False)

print("\n====================================================")
print("FINAL COMPARISON TABLE")
print("====================================================")

with pd.option_context(
    "display.max_columns", None,
    "display.width", 200
):
    print(comparison)

print("\nSaved to:")
print(outfile)
