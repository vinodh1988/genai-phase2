import csv
import math
import random
from datetime import date, timedelta

SEED = 42
DAYS = 730
START_DATE = date(2024, 2, 15)
OUTPUT_FILE = "ecommerce_kpi.csv"

REGIONS = [
    {"name": "North", "weight": 0.28, "spend_mult": 1.05, "aov_mult": 1.02, "conv_mult": 1.00},
    {"name": "South", "weight": 0.24, "spend_mult": 0.95, "aov_mult": 0.98, "conv_mult": 0.97},
    {"name": "East", "weight": 0.26, "spend_mult": 1.00, "aov_mult": 1.03, "conv_mult": 1.02},
    {"name": "West", "weight": 0.22, "spend_mult": 1.08, "aov_mult": 1.06, "conv_mult": 1.03},
]


def clamp(value, low, high):
    return max(low, min(high, value))


def pick_region(rng):
    choices = [r["name"] for r in REGIONS]
    weights = [r["weight"] for r in REGIONS]
    return rng.choices(choices, weights=weights, k=1)[0]


def get_region_factors(region_name):
    for region in REGIONS:
        if region["name"] == region_name:
            return region
    return REGIONS[0]


def generate_rows():
    rng = random.Random(SEED)
    rows = []

    for day_index in range(DAYS):
        current_date = START_DATE + timedelta(days=day_index)
        day_of_year = current_date.timetuple().tm_yday

        region = pick_region(rng)
        factors = get_region_factors(region)

        weekly = 1.0 + 0.06 * math.sin(2 * math.pi * day_index / 7)
        annual = 1.0 + 0.14 * math.sin(2 * math.pi * day_of_year / 365)
        promo = 1.0
        if 150 <= day_of_year <= 170:
            promo += 0.18
        if 330 <= day_of_year <= 360:
            promo += 0.25

        base_spend = 9000 * weekly * annual * promo
        spend_noise = rng.gauss(0, 1100)
        marketing_spend = max(1200, base_spend + spend_noise) * factors["spend_mult"]

        visitors = marketing_spend * (2.9 + rng.gauss(0, 0.28)) + 5200 * annual
        visitors = max(300, visitors)

        conv_rate = 0.018 * factors["conv_mult"] * (1 + 0.0000015 * marketing_spend)
        conv_rate += rng.gauss(0, 0.0022)
        conv_rate = clamp(conv_rate, 0.006, 0.05)

        orders = int(visitors * conv_rate)

        aov = 68 * factors["aov_mult"] * (1 + 0.06 * annual) + rng.gauss(0, 6.5)
        aov = clamp(aov, 25, 220)

        revenue = orders * aov * (1 + rng.gauss(0, 0.03))
        revenue = max(0, revenue)

        new_customer_rate = clamp(0.55 + rng.gauss(0, 0.07), 0.35, 0.85)
        new_customers = max(1, int(orders * new_customer_rate))
        cac = marketing_spend / new_customers

        rows.append(
            {
                "Date": current_date.isoformat(),
                "Marketing_Spend": round(marketing_spend, 2),
                "Website_Visitors": int(visitors),
                "Conversion_Rate": round(orders / max(visitors, 1), 4),
                "Orders": orders,
                "Revenue": round(revenue, 2),
                "Avg_Order_Value": round(aov, 2),
                "Customer_Acquisition_Cost": round(cac, 2),
                "Region": region,
            }
        )

    return rows


def write_csv(rows, output_path):
    fieldnames = [
        "Date",
        "Marketing_Spend",
        "Website_Visitors",
        "Conversion_Rate",
        "Orders",
        "Revenue",
        "Avg_Order_Value",
        "Customer_Acquisition_Cost",
        "Region",
    ]

    with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    data_rows = generate_rows()
    write_csv(data_rows, OUTPUT_FILE)
    print(f"Wrote {len(data_rows)} rows to {OUTPUT_FILE}")
