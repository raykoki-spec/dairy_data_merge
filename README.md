# File: README.md

# Nakuru Dairy Co-op Data Merge 

A Python based program that merges two data sets to create a single file and print clear summary for easier analysis and payment of the milk suppliers to be made.


## What It Does

- Merge two data sets (milk collection and farmer details)
- Apply logic to calculate total milk collection per zone and amount payable to farmers in their respective zone 
- Rank and indicate top farmer in every zone
- Create a clear report in form of table, grouping total supply and amount owed to each zone


## Setup

```bash
pip install -r requirements.txt
```

## Usage

``` 
Run the program from the project's folder

python nakuru_dairy.py
```

## How It Works

Data is merged from from two files to create a single file (merged).

```python
merged = pd.merge(collection, details, on="name", how="outer")
print(merged)
```

## Sample Output

```
================NAKURU DAIRY CO-OP SUMMARY====================

           litres  payout_kes top_farmer
zone                                    
Bahati        265       14700       Tuge
Highlands     445       22675      Ndeda
Menengai      145        6275     Kamket
```

## Stack

Python


