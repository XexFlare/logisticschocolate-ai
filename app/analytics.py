from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "logisticsforce_sample.csv"


def load_data() -> pd.DataFrame:
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            "Sample data not found. Run: python data/generate_sample_data.py"
        )
    df = pd.read_csv(DATA_PATH, parse_dates=["shipment_date"])
    return df


def kpi_summary(df: pd.DataFrame) -> dict:
    return {
        "shipments": len(df),
        "revenue_usd": df["revenue_usd"].sum(),
        "tonnage": df["tonnage"].sum(),
        "avg_delay_hours": df["delay_hours"].mean(),
    }


def revenue_by_route(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("route", as_index=False)
        .agg(revenue_usd=("revenue_usd", "sum"), shipments=("shipment_id", "count"), tonnage=("tonnage", "sum"))
        .sort_values("revenue_usd", ascending=False)
    )


def monthly_tonnage(df: pd.DataFrame) -> pd.DataFrame:
    monthly = df.copy()
    monthly["month"] = monthly["shipment_date"].dt.to_period("M").astype(str)
    return monthly.groupby("month", as_index=False).agg(tonnage=("tonnage", "sum"))


def delay_by_route(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("route", as_index=False)
        .agg(avg_delay_hours=("delay_hours", "mean"), delayed_shipments=("status", lambda x: (x == "Delayed").sum()))
        .sort_values("avg_delay_hours", ascending=False)
    )
