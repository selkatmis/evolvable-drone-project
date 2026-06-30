import os
from pathlib import Path
import pandas as pd

from parser import load_blackbox_csv
from metrics import *
from plotting import *
from config import *

summary = []

print("=" * 60)
print("BLACKBOX FLIGHT ANALYSIS")
print("=" * 60)

# ==========================================================
# PROCESS EVERY CSV
# ==========================================================

for filename in sorted(os.listdir(INPUT_FOLDER)):

    if not filename.lower().endswith(".csv"):
        continue

    print(f"\nProcessing: {filename}")

    filepath = INPUT_FOLDER / filename

    # ------------------------------------------------------
    # Load Blackbox
    # ------------------------------------------------------

    try:
        df = load_blackbox_csv(filepath)

    except Exception as e:
        print(f"❌ Could not load {filename}")
        print(e)
        continue

    # ------------------------------------------------------
    # Create results folder
    # ------------------------------------------------------

    flight_folder = OUTPUT_FOLDER / Path(filename).stem
    flight_folder.mkdir(exist_ok=True)

    # ------------------------------------------------------
    # Generate plots
    # ------------------------------------------------------

    plots = [

        battery_plot,

        current_plot,

        power_plot,

        motor_plot,

        rpm_plot,

        motor_histogram,

        gyro_plot,

        velocity_plot,

        speed_plot,

        altitude_plot,

        hover_plot,

        xy_plot,

        trajectory3d,

    ]
    

    for plot_function in plots:

        try:

            plot_function(df, flight_folder)

        except Exception as e:

            print(f"⚠ {plot_function.__name__} failed.")

            print(e)

    # ------------------------------------------------------
    # Compute metrics
    # ------------------------------------------------------

    row = {}

    row["Flight"] = Path(filename).stem

    metric_functions = [

        flight_metrics,

        battery_metrics,

        motor_metrics,

        rpm_metrics,

        gyro_metrics,

        position_metrics,

        velocity_metrics,

        stability_metrics

    ]

    for metric in metric_functions:

        try:

            row.update(metric(df))

        except Exception as e:

            print(f"⚠ {metric.__name__} failed.")

            print(e)

    summary.append(row)

    print("✓ Finished.")

# ==========================================================
# SAVE SUMMARY
# ==========================================================

summary_df = pd.DataFrame(summary)

summary_file = OUTPUT_FOLDER / "summary.csv"

summary_df.to_csv(summary_file, index=False)

print("\n" + "=" * 60)
print("ANALYSIS COMPLETE")
print("=" * 60)

print(f"\nFlights processed : {len(summary_df)}")

print(f"\nSummary saved to:\n{summary_file}")

print("\nSummary Preview:\n")

with pd.option_context(
    'display.max_columns', None,
    'display.width', 300
):
    print(summary_df)

print("\nDone!")