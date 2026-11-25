import pandas as pd


def prepare_trips(df):
    data = df.copy()
    numeric_cols = ["weight_t", "distance_km", "duration_h", "cost_rub", "delay_h"]
    for col in numeric_cols:
        data[col] = pd.to_numeric(data[col], errors="coerce")
    report = {"строк до обработки": len(data), "пропусков до обработки": int(data.isna().sum().sum())}
    data = data.drop_duplicates(subset="trip_id")
    data = data.dropna(subset=["date", "route", "carrier", "cargo_type", "weight_t", "distance_km", "cost_rub", "delay_h"])
    data = data[(data["weight_t"] > 0) & (data["distance_km"] > 0) & (data["cost_rub"] > 0) & (data["delay_h"] >= 0)]
    data["month"] = data["date"].dt.to_period("M").astype(str)
    data["cost_per_km"] = (data["cost_rub"] / data["distance_km"]).round(2)
    data["on_time"] = (data["delay_h"] == 0)
    report["строк после обработки"] = len(data)
    report["удалено строк"] = report["строк до обработки"] - len(data)
    report["пропусков после обработки"] = int(data.isna().sum().sum())
    return data, report
