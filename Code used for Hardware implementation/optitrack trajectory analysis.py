# import pandas as pd
# import numpy as np

# csv_file = r"C:\Users\akshi\OneDrive\Documents\Thesis Project - Evolvable Drones\New Design working\Test #2\Take 2026-06-15 05.35.22 PM.csv"

# # Load the CSV with multi-row headers
# df = pd.read_csv(csv_file, header=[0,1,2,3,4])

# print("\nLoaded CSV\n")

# # Find markers
# markers = {}

# for col in df.columns:
#     try:
#         marker_name = col[1]  # usually "Unlabeled XXXXX"

#         if "Unlabeled" not in str(marker_name):
#             continue

#         if marker_name not in markers:
#             markers[marker_name] = []

#         markers[marker_name].append(col)

#     except:
#         pass

# print(f"Found {len(markers)} markers\n")

# movement_results = []

# for marker, cols in markers.items():

#     x_col = None
#     y_col = None
#     z_col = None

#     for c in cols:

#         last = str(c[-1])

#         if last == "X":
#             x_col = c
#         elif last == "Y":
#             y_col = c
#         elif last == "Z":
#             z_col = c

#     if x_col is None or y_col is None or z_col is None:
#         continue

#     x = pd.to_numeric(df[x_col], errors="coerce")
#     y = pd.to_numeric(df[y_col], errors="coerce")
#     z = pd.to_numeric(df[z_col], errors="coerce")

#     movement = (
#         (x.max() - x.min()) +
#         (y.max() - y.min()) +
#         (z.max() - z.min())
#     )

#     movement_results.append((marker, movement))

# movement_results.sort(key=lambda x: x[1], reverse=True)

# print("Markers ranked by movement:\n")

# for marker, movement in movement_results:
#     print(f"{marker:20s}  movement = {movement:.3f} m")


# import pandas as pd

# csv_file = r"C:\Users\akshi\OneDrive\Documents\Thesis Project - Evolvable Drones\New Design working\Test #2\Take 2026-06-15 05.35.22 PM.csv"

# with open(csv_file, "r", encoding="utf-8", errors="ignore") as f:
#     for i in range(20):
#         print(f"{i}: {f.readline().rstrip()}")


# import pandas as pd

# csv_file = r"C:\Users\akshi\OneDrive\Documents\Thesis Project - Evolvable Drones\New Design working\Test #2\Take 2026-06-15 05.35.22 PM.csv"

# # header starts on line 2
# df = pd.read_csv(csv_file, skiprows=2, header=[0,1,2,3,4])

# print(df.columns.tolist()[:20])

import pandas as pd
import matplotlib.pyplot as plt

csv_file = r"C:\Users\akshi\OneDrive\Documents\Thesis Project - Evolvable Drones\New Design working\Test #2\Take 2026-06-15 05.35.22 PM.csv"

df = pd.read_csv(csv_file, skiprows=2, header=[0,1,2,3,4])

time_col = ('Unnamed: 1_level_0',
            'Unnamed: 1_level_1',
            'Unnamed: 1_level_2',
            'Unnamed: 1_level_3',
            'Time (Seconds)')

x_col = ('Rigid Body',"Akshi's drone",
         '44E62892668111F1FA258DFB8DDA959C',
         'Position','X')

y_col = ('Rigid Body',"Akshi's drone",
         '44E62892668111F1FA258DFB8DDA959C',
         'Position','Y')

z_col = ('Rigid Body',"Akshi's drone",
         '44E62892668111F1FA258DFB8DDA959C',
         'Position','Z')

time = pd.to_numeric(df[time_col], errors='coerce')
x = pd.to_numeric(df[x_col], errors='coerce')
y = pd.to_numeric(df[y_col], errors='coerce')
z = pd.to_numeric(df[z_col], errors='coerce')

plt.figure(figsize=(10,5))
plt.plot(time, z)
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.title("Drone Altitude")
plt.grid()
plt.show()

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z)

ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_zlabel("Z (m)")
ax.set_title("OptiTrack Drone Trajectory")

plt.show()

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z)

ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_zlabel("Z (m)")
ax.set_title("OptiTrack Drone Trajectory")

plt.show()