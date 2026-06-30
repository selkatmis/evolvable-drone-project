import numpy as np
import pandas as pd

# ============================================================
# BASIC FLIGHT INFORMATION
# ============================================================

def flight_metrics(df):

    results = {}

    results["Samples"] = len(df)

    if "time" in df.columns:

        duration = (df["time"].iloc[-1] - df["time"].iloc[0]) / 1e6

        results["Duration (s)"] = duration

        if duration > 0:
            results["Sample Rate (Hz)"] = len(df) / duration

    return results


# ============================================================
# BATTERY
# ============================================================

def battery_metrics(df):

    results = {}

    if "vbatLatest" not in df.columns:
        return results

    voltage = df["vbatLatest"]

    results["Battery Start"] = voltage.iloc[0]
    results["Battery End"] = voltage.iloc[-1]
    results["Battery Drop"] = voltage.iloc[0] - voltage.iloc[-1]
    results["Battery Min"] = voltage.min()
    results["Battery Max"] = voltage.max()
    results["Battery Mean"] = voltage.mean()

    if "amperageLatest" in df.columns:

        current = df["amperageLatest"]

        results["Current Mean"] = current.mean()
        results["Current Max"] = current.max()

        power = voltage * current

        results["Power Mean"] = power.mean()
        results["Power Max"] = power.max()

    return results


# ============================================================
# MOTOR METRICS
# ============================================================

def motor_metrics(df):

    results = {}

    motors = [c for c in df.columns if c.startswith("motor[")]

    if len(motors) == 0:
        return results

    means = []

    for m in motors:

        vals = df[m]

        results[m + " Mean"] = vals.mean()
        results[m + " Std"] = vals.std()
        results[m + " Min"] = vals.min()
        results[m + " Max"] = vals.max()

        means.append(vals.mean())

    results["Motor Mean"] = np.mean(means)
    results["Motor Std Between"] = np.std(means)

    return results


# ============================================================
# RPM
# ============================================================

def rpm_metrics(df):

    results = {}

    rpm_cols = [c for c in df.columns if c.startswith("omega[")]

    if len(rpm_cols) == 0:
        return results

    all_rpm = []

    for c in rpm_cols:

        vals = df[c]

        results[c + " Mean"] = vals.mean()
        results[c + " Max"] = vals.max()
        results[c + " Std"] = vals.std()

        all_rpm.extend(vals.values)

    all_rpm = np.asarray(all_rpm)

    results["RPM Mean"] = np.mean(all_rpm)
    results["RPM Max"] = np.max(all_rpm)
    results["RPM Std"] = np.std(all_rpm)

    return results


# ============================================================
# ANGULAR RATES
# ============================================================

def gyro_metrics(df):

    results = {}

    gyro = [c for c in df.columns if c.startswith("gyroADC[")]

    if len(gyro) == 0:
        return results

    rms = []

    for g in gyro:

        vals = df[g]

        results[g + " Mean"] = vals.mean()
        results[g + " Max"] = np.abs(vals).max()
        results[g + " Std"] = vals.std()

        r = np.sqrt(np.mean(vals ** 2))

        results[g + " RMS"] = r

        rms.append(r)

    results["Angular Rate RMS"] = np.mean(rms)

    return results


# ============================================================
# POSITION
# ============================================================

def position_metrics(df):

    results = {}

    cols = ["pos[0]", "pos[1]", "pos[2]"]

    if not set(cols).issubset(df.columns):
        return results

    x = df["pos[0]"]
    y = df["pos[1]"]
    z = df["pos[2]"]

    results["Max Altitude"] = z.max()
    results["Min Altitude"] = z.min()

    dx = np.diff(x)
    dy = np.diff(y)
    dz = np.diff(z)

    distance = np.sum(
        np.sqrt(dx**2 + dy**2 + dz**2)
    )

    results["Distance Travelled"] = distance

    displacement = np.sqrt(
        (x.iloc[-1]-x.iloc[0])**2 +
        (y.iloc[-1]-y.iloc[0])**2 +
        (z.iloc[-1]-z.iloc[0])**2
    )

    results["Final Displacement"] = displacement

    return results


# ============================================================
# VELOCITY
# ============================================================

def velocity_metrics(df):

    results = {}

    cols = ["vel[0]", "vel[1]", "vel[2]"]

    if not set(cols).issubset(df.columns):
        return results

    vx = df["vel[0]"]
    vy = df["vel[1]"]
    vz = df["vel[2]"]

    speed = np.sqrt(vx**2 + vy**2 + vz**2)

    results["Mean Speed"] = speed.mean()
    results["Max Speed"] = speed.max()

    results["Vertical Speed Mean"] = np.abs(vz).mean()
    results["Vertical Speed Max"] = np.abs(vz).max()

    return results


# ============================================================
# STABILITY
# ============================================================

def stability_metrics(df):

    results = {}

    gyro = [c for c in df.columns if c.startswith("gyroADC[")]

    motors = [c for c in df.columns if c.startswith("motor[")]

    if len(gyro):

        rms = []

        for g in gyro:

            rms.append(
                np.sqrt(np.mean(df[g]**2))
            )

        results["Hover Stability Index"] = np.mean(rms)

    if len(motors):

        means = []

        for m in motors:

            means.append(df[m].mean())

        results["Motor Balance Index"] = np.std(means)

    return results