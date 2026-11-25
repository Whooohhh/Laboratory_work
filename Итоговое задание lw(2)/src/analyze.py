import pandas as pd


def calculate_metrics(df):
    monthly = df.groupby("month").agg(revenue=("cost_rub", "sum"), trips=("trip_id", "count")).reset_index()
    monthly["revenue_mln"] = monthly["revenue"] / 1_000_000
    route_stats = df.groupby("route").agg(revenue=("cost_rub", "sum"), trips=("trip_id", "count")).sort_values("revenue")
    carrier_stats = df.groupby("carrier").agg(trips=("trip_id", "count"), OTD=("on_time", "mean"), avg_delay=("delay_h", "mean"))
    carrier_stats["OTD_pct"] = carrier_stats["OTD"] * 100
    cargo_stats = df.groupby("cargo_type").agg(revenue=("cost_rub", "sum"), trips=("trip_id", "count")).sort_values("revenue")
    kpis = {
        "trips": int(len(df)),
        "total_revenue": float(df["cost_rub"].sum()),
        "mean_trip_cost": float(df["cost_rub"].mean()),
        "median_trip_cost": float(df["cost_rub"].median()),
        "on_time_pct": float(df["on_time"].mean() * 100),
        "mean_delay": float(df["delay_h"].mean()),
    }
    return {"monthly": monthly, "route_stats": route_stats, "carrier_stats": carrier_stats, "cargo_stats": cargo_stats, "kpis": kpis}
