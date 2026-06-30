import os
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams.update({
    "figure.figsize": (10,5),
    "font.size": 12,
    "axes.grid": True
})


def save_plot(fig, filename):
    fig.tight_layout()
    fig.savefig(filename, dpi=300)
    plt.close(fig)


##############################################################
# BATTERY
##############################################################

def battery_plot(df, out):

    if "vbatLatest" not in df.columns:
        return

    t = df["time"] / 1e6

    fig = plt.figure()

    plt.plot(t, df["vbatLatest"], lw=2)

    plt.xlabel("Time (s)")
    plt.ylabel("Battery Voltage")
    plt.title("Battery Voltage")

    save_plot(fig, os.path.join(out, "battery_voltage.png"))


##############################################################
# CURRENT
##############################################################

def current_plot(df, out):

    if "amperageLatest" not in df.columns:
        return

    t = df["time"] / 1e6

    fig = plt.figure()

    plt.plot(t, df["amperageLatest"])

    plt.xlabel("Time (s)")
    plt.ylabel("Current")

    plt.title("Current Draw")

    save_plot(fig, os.path.join(out, "current.png"))


##############################################################
# MOTORS
##############################################################

def motor_plot(df, out):

    motors = [c for c in df.columns if c.startswith("motor[")]

    if len(motors)==0:
        return

    t = df["time"]/1e6

    fig = plt.figure()

    for m in motors:
        plt.plot(t, df[m], label=m)

    plt.legend()

    plt.xlabel("Time (s)")
    plt.ylabel("Motor Output")

    plt.title("Motor Outputs")

    save_plot(fig, os.path.join(out,"motor_outputs.png"))


##############################################################
# MOTOR HISTOGRAM
##############################################################

def motor_histogram(df, out):

    motors = [c for c in df.columns if c.startswith("motor[")]

    if len(motors)==0:
        return

    fig = plt.figure()

    for m in motors:
        plt.hist(df[m],
                 bins=40,
                 alpha=0.5,
                 label=m)

    plt.legend()

    plt.xlabel("Motor Output")

    plt.ylabel("Count")

    plt.title("Motor Distribution")

    save_plot(fig,
              os.path.join(out,
                           "motor_histogram.png"))


##############################################################
# GYRO
##############################################################

def gyro_plot(df, out):

    gyro=[c for c in df.columns if c.startswith("gyroADC[")]

    if len(gyro)<3:
        return

    t=df["time"]/1e6

    fig=plt.figure()

    for g in gyro:
        plt.plot(t,df[g],label=g)

    plt.legend()

    plt.xlabel("Time (s)")
    plt.ylabel("deg/s")

    plt.title("Angular Velocity")

    save_plot(fig,
              os.path.join(out,
                           "gyro.png"))


##############################################################
# VELOCITY
##############################################################

def velocity_plot(df,out):

    cols=["vel[0]","vel[1]","vel[2]"]

    if not set(cols).issubset(df.columns):
        return

    t=df["time"]/1e6

    fig=plt.figure()

    labels=["X","Y","Z"]

    for c,l in zip(cols,labels):

        plt.plot(t,
                 df[c],
                 label=l)

    plt.legend()

    plt.xlabel("Time (s)")

    plt.ylabel("m/s")

    plt.title("Velocity")

    save_plot(fig,
              os.path.join(out,
                           "velocity.png"))


##############################################################
# ALTITUDE
##############################################################

def altitude_plot(df,out):

    if "pos[2]" not in df.columns:
        return

    t=df["time"]/1e6

    fig=plt.figure()

    plt.plot(t,
             df["pos[2]"])

    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.title("Altitude")

    save_plot(fig,
              os.path.join(out,
                           "altitude.png"))


##############################################################
# XY TRAJECTORY
##############################################################

def xy_plot(df,out):

    cols=["pos[0]","pos[1]"]

    if not set(cols).issubset(df.columns):
        return

    fig=plt.figure()

    plt.plot(df["pos[0]"],
             df["pos[1]"])

    plt.xlabel("X")

    plt.ylabel("Y")

    plt.axis("equal")

    plt.title("XY Trajectory")

    save_plot(fig,
              os.path.join(out,
                           "trajectory_xy.png"))


##############################################################
# 3D TRAJECTORY
##############################################################

def trajectory3d(df,out):

    cols=["pos[0]","pos[1]","pos[2]"]

    if not set(cols).issubset(df.columns):
        return

    fig=plt.figure(figsize=(8,8))

    ax=fig.add_subplot(111,
                       projection="3d")

    ax.plot(df["pos[0]"],
            df["pos[1]"],
            df["pos[2]"],
            lw=2)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.title("3D Flight Trajectory")

    save_plot(fig,
              os.path.join(out,
                           "trajectory3D.png"))

##############################################################
# MOTOR RPM
##############################################################

def rpm_plot(df, out):

    rpm = [c for c in df.columns if c.startswith("omega[")]

    if len(rpm) == 0:
        return

    t = df["time"] / 1e6

    fig = plt.figure(figsize=(10,5))

    for r in rpm:
        plt.plot(t, df[r], label=r)

    plt.xlabel("Time (s)")
    plt.ylabel("Motor RPM")
    plt.title("Motor RPM")

    plt.grid(True)
    plt.legend()

    save_plot(fig, os.path.join(out, "motor_rpm.png"))

##############################################################
# POWER
##############################################################

def power_plot(df, out):

    if "vbatLatest" not in df.columns:
        return

    if "amperageLatest" not in df.columns:
        return

    voltage = df["vbatLatest"]
    current = df["amperageLatest"]

    power = voltage * current

    t = df["time"] / 1e6

    fig = plt.figure(figsize=(10,5))

    plt.plot(t, power)

    plt.xlabel("Time (s)")
    plt.ylabel("Power")

    plt.title("Estimated Power Consumption")

    plt.grid(True)

    save_plot(fig, os.path.join(out, "power.png"))

##############################################################
# SPEED
##############################################################

def speed_plot(df, out):

    cols = ["vel[0]","vel[1]","vel[2]"]

    if not set(cols).issubset(df.columns):
        return

    vx = df["vel[0]"]
    vy = df["vel[1]"]
    vz = df["vel[2]"]

    speed = np.sqrt(vx**2 + vy**2 + vz**2)

    t = df["time"] / 1e6

    fig = plt.figure(figsize=(10,5))

    plt.plot(t, speed)

    plt.xlabel("Time (s)")
    plt.ylabel("Speed (m/s)")

    plt.title("Total Velocity")

    plt.grid(True)

    save_plot(fig, os.path.join(out, "speed.png"))

##############################################################
# HOVER
##############################################################

def hover_plot(df, out):

    if "pos[2]" not in df.columns:
        return

    t = df["time"] / 1e6

    fig = plt.figure(figsize=(10,5))

    plt.plot(t, df["pos[2]"])

    plt.xlabel("Time (s)")
    plt.ylabel("Altitude")

    plt.title("Hover Capability")

    plt.grid(True)

    save_plot(fig, os.path.join(out, "hover.png"))

