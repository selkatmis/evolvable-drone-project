import pandas as pd

# ---------------------------------------------------
# FILES
# ---------------------------------------------------

raw = pd.read_csv(
    r"C:\Users\akshi\OneDrive\Documents\Thesis Project - Evolvable Drones\Comparison Results\Final_Comparison_Table.csv"
)

cal = pd.read_csv(
    r"C:\Users\akshi\OneDrive\Documents\Thesis Project - Evolvable Drones\Comparison Results\Final_Calibrated_Comparison_Table.csv"
)

# ---------------------------------------------------
# BUILD TABLE
# ---------------------------------------------------

table = pd.DataFrame()

table["Flight"] = raw["Flight"]

table["Duration Error (%) Raw"] = raw["Duration Error (%)"].round(2)
table["Duration Error (%) Cal"] = cal["Duration Error (%)"].round(2)

table["Angular RMS (Real)"] = raw["Real Angular RMS"].round(2)
table["Angular RMS Raw"] = raw["Simulation Angular RMS"].round(2)
table["Angular RMS Cal"] = cal["Simulation Angular RMS"].round(2)

table["Angular Max (Real)"] = raw["Real Angular Max"].round(2)
table["Angular Max Raw"] = raw["Simulation Angular Max"].round(2)
table["Angular Max Cal"] = cal["Simulation Angular Max"].round(2)

# ---------------------------------------------------
# SAVE
# ---------------------------------------------------

output = r"C:\Users\akshi\OneDrive\Documents\Thesis Project - Evolvable Drones\Comparison Results\Thesis_Table.csv"

table.to_csv(output, index=False)

print(table)

print("\nSaved to:")
print(output)