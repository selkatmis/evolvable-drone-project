import os
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# SETTINGS
# ==========================================================

INPUT_FOLDER = r"C:\Users\akshi\OneDrive\Documents\Thesis Project - Evolvable Drones\Thrust conversions"

KF = 1.80e-07

print("=" * 60)
print("BLACKBOX -> THRUST CONVERTER")
print("=" * 60)

# ==========================================================
# FIND ALL CSV FILES
# ==========================================================

csv_files = [
    f for f in os.listdir(INPUT_FOLDER)
    if f.lower().endswith(".csv")
    and "_thrust" not in f.lower()
]

print(f"\nFound {len(csv_files)} CSV files.\n")

# ==========================================================
# PROCESS EACH FLIGHT
# ==========================================================

for filename in sorted(csv_files):

    print(f"Processing: {filename}")

    csv_path = os.path.join(INPUT_FOLDER, filename)

    # ------------------------------------------------------
    # LOAD BLACKBOX
    # ------------------------------------------------------

    try:
        df = pd.read_csv(csv_path, skiprows=140)

    except Exception as e:
        print(f"Could not read {filename}")
        print(e)
        continue

    # ------------------------------------------------------
    # TIME
    # ------------------------------------------------------

    df["time_s"] = (
        df["time"] - df["time"].iloc[0]
    ) / 1_000_000

    # ------------------------------------------------------
    # CHECK REQUIRED COLUMNS
    # ------------------------------------------------------

    required = [
        "omega[0]",
        "omega[1]",
        "omega[2]",
        "omega[3]"
    ]

    missing = [c for c in required if c not in df.columns]

    if len(missing):

        print("Missing columns:")
        print(missing)
        continue

    # ------------------------------------------------------
    # PRINT STATISTICS
    # ------------------------------------------------------

    print("\nRotor Speed Summary:")

    for i in range(4):

        print(f"\nMotor {i}")

        print(df[f"omega[{i}]"].describe())

    # ------------------------------------------------------
    # OPTIONAL PLOT
    # ------------------------------------------------------

    plt.figure(figsize=(12,6))

    for i in range(4):

        plt.plot(
            df["time_s"],
            df[f"omega[{i}]"],
            label=f"omega[{i}]"
        )

    plt.title(filename)
    plt.xlabel("Time (s)")
    plt.ylabel("Rotor Speed")

    plt.grid(True)
    plt.legend()

    plt.show()

    # ------------------------------------------------------
    # OMEGA -> THRUST
    # ------------------------------------------------------

    for i in range(4):

        df[f"thrust_{i}"] = KF * (
            df[f"omega[{i}]"] ** 2
        )

    # ------------------------------------------------------
    # SAVE THRUST PROFILE
    # ------------------------------------------------------

    output_name = filename.replace(".csv", "_thrust.csv")

    output_path = os.path.join(
        INPUT_FOLDER,
        output_name
    )

    df[
        [
            "thrust_0",
            "thrust_1",
            "thrust_2",
            "thrust_3"
        ]
    ].to_csv(
        output_path,
        index=False,
        header=False
    )

    print(f"\nSaved: {output_name}")

print("\n" + "=" * 60)
print("ALL FLIGHTS CONVERTED")
print("=" * 60)