import csv
from datetime import date, timedelta
from pathlib import Path

def generate(destination=Path("data/sales.csv")):
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["sale_id", "sale_date", "region", "quantity", "unit_price"])
        for i in range(120):
            writer.writerow([i + 1, date(2026, 1, 1) + timedelta(days=i), ["North", "South", "West"][i % 3], i % 5 + 1, 10 + i % 7])
    return destination

if __name__ == "__main__":
    print(generate())
