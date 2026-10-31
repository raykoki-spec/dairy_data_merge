
"""
Dairy Co-op Data Merge
----------------------
Merges two data sets created by Co-op manager(Daily collection and Farmers details).
Pivots the results by zone.
Prints a clean summary table.

Usage:
    python nakuru_dairy.py

Config:
    Edit the name of files to match those of the current csv files.
"""
import pandas as pd

collection = pd.DataFrame({
    "name": ["Mwangi", "Kamau", "Tuge", "Kibet", "Kamket", "Osia", "Wafula", "Sindani", "Ndeda", "Kahenza", "wanyonyi", "Mungai"],
    "date": ["2024-01-01", "2024-01-01", "2024-01-02", "2024-01-02", "2024-01-03", "2024-01-03", "2024-01-04", "2024-01-04", "2024-01-04", "2024-01-04", "2024-01-03", "2024-01-02"],
    "litres": [60, 50, 85, 70, 95, 50, 65, 90, 105, 60, 55, 70]

})

details = pd.DataFrame({
    "name": ["Mwangi", "Kamau", "Tuge", "Kibet", "Kamket", "Osia", "Wafula", "Sindani", "Ndeda", "Kahenza", "wanyonyi", "Mungai"],
    "zone": ["Bahati", "Bahati", "Bahati", "Bahati", "Menengai", "Menengai", "Highlands", "Highlands", "Highlands", "Highlands", "Highlands", "Highlands"],
    "price_per_litre": [50, 55, 60, 55, 45, 40, 55, 60, 45, 50, 45, 50]
})


merged = pd.merge(collection, details, on="name", how="outer")
print("=====================NAKURU DAIRY FARMERS LOG====================")
print()
print(merged)

merged["payout_kes"] = merged["litres"] * merged["price_per_litre"]


pivot = pd.pivot_table(
    merged,
    values=["litres", "payout_kes"],
    index="zone",
    aggfunc="sum"
)

farmer_totals = merged.groupby(["zone", "name"])["litres"].sum().reset_index()
top = farmer_totals.loc[farmer_totals.groupby("zone")["litres"].idxmax()]
top = top.set_index("zone")["name"]

pivot["top_farmer"] = top


print("---------------------------------------------------------------")

print("\n================NAKURU DAIRY CO-OP SUMMARY====================")
print()
print(pivot)