import random
from pathlib import Path

import numpy as np
import pandas as pd

OUTPUT = Path(__file__).resolve().parent / "logisticsforce_sample.csv"

random.seed(42)
np.random.seed(42)

routes = [
    ("Lilongwe", "Blantyre"),
    ("Lilongwe", "Mzuzu"),
    ("Blantyre", "Zomba"),
    ("Lusaka", "Ndola"),
    ("Lusaka", "Lilongwe"),
    ("Beira", "Lilongwe"),
    ("Dar es Salaam", "Lilongwe"),
    ("Harare", "Blantyre"),
]

cargo_types = ["Fertilizer", "Maize", "Soya", "Seed", "Agrochemicals", "General Cargo"]
statuses = ["Delivered", "Delayed", "In Transit", "Cancelled"]
status_weights = [0.72, 0.16, 0.10, 0.02]

rows = []
num_rows = 80_000
start_date = pd.Timestamp("2025-01-01")

for i in range(num_rows):
    origin, destination = random.choice(routes)
    cargo = random.choice(cargo_types)
    shipment_date = start_date + pd.Timedelta(days=random.randint(0, 364))
    tonnage = round(max(5, np.random.normal(28, 8)), 2)
    rate_per_ton = random.randint(45, 140)
    revenue = round(tonnage * rate_per_ton, 2)
    status = random.choices(statuses, weights=status_weights, k=1)[0]
    delay_hours = 0 if status == "Delivered" else max(1, int(np.random.exponential(12)))

    rows.append(
        {
            "shipment_id": f"SHP-{i + 1:06d}",
            "shipment_date": shipment_date.date(),
            "truck_id": f"TRK-{random.randint(1, 420):04d}",
            "origin": origin,
            "destination": destination,
            "route": f"{origin} to {destination}",
            "cargo_type": cargo,
            "tonnage": tonnage,
            "revenue_usd": revenue,
            "status": status,
            "delay_hours": delay_hours,
        }
    )

df = pd.DataFrame(rows)
df.to_csv(OUTPUT, index=False)
print(f"Created {OUTPUT} with {len(df):,} rows")
