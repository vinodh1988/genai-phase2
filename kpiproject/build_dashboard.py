import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA_FILE = "ecommerce_kpi.csv"
OUTPUT_DIR = "dashboard"


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def format_currency(value):
    return f"${value:,.0f}"


def format_number(value):
    return f"{value:,.0f}"


def format_percent(value):
    return f"{value * 100:.2f}%"


def compute_kpis(df):
    total_revenue = df["Revenue"].sum()
    total_orders = df["Orders"].sum()
    avg_conversion = df["Conversion_Rate"].mean()
    total_spend = df["Marketing_Spend"].sum()
    avg_aov = df["Avg_Order_Value"].mean()

    return [
        ("Total Revenue", format_currency(total_revenue)),
        ("Total Orders", format_number(total_orders)),
        ("Avg Conversion", format_percent(avg_conversion)),
        ("Total Marketing Spend", format_currency(total_spend)),
        ("Avg Order Value", format_currency(avg_aov)),
    ]


def plot_revenue_trend(df, output_path):
    monthly = df.set_index("Date").resample("M").sum(numeric_only=True)
    plt.figure(figsize=(10, 4))
    plt.plot(monthly.index, monthly["Revenue"], color="#1f7a8c", linewidth=2)
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def scatter_with_regression(x, y, title, xlabel, ylabel, output_path, color):
    slope, intercept = np.polyfit(x, y, 1)
    y_pred = slope * x + intercept
    r2 = 1 - (np.sum((y - y_pred) ** 2) / np.sum((y - np.mean(y)) ** 2))

    plt.figure(figsize=(6, 4))
    plt.scatter(x, y, alpha=0.6, color=color)
    plt.plot(x, y_pred, color="#ff6b35", linewidth=2)
    plt.title(f"{title} (R2: {r2:.2f})")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

    return r2


def build_html(kpis, image_files, output_path):
    kpi_cards = "\n".join(
        f"<div class=\"kpi-card\"><span>{label}</span><strong>{value}</strong></div>"
        for label, value in kpis
    )

    html = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>KPI Dashboard</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;700&family=Space+Grotesk:wght@500;600;700&display=swap"
      rel="stylesheet"
    />
    <style>
      :root {{
        --ink: #0b1f2a;
        --muted: #4b5a65;
        --card: #ffffff;
        --accent: #ff6b35;
        --accent-2: #1f7a8c;
        --bg-1: #f4efe9;
        --bg-2: #e3f1f2;
        --shadow: 0 20px 45px rgba(11, 31, 42, 0.12);
      }}

      * {{
        box-sizing: border-box;
      }}

      body {{
        margin: 0;
        font-family: "IBM Plex Sans", sans-serif;
        color: var(--ink);
        background: radial-gradient(circle at top left, var(--bg-2), transparent 45%),
          linear-gradient(135deg, var(--bg-1), #fbf8f2 60%);
        min-height: 100vh;
      }}

      header {{
        padding: 40px 7vw 24px;
      }}

      header h1 {{
        font-family: "Space Grotesk", sans-serif;
        font-size: clamp(28px, 3.2vw, 46px);
        margin: 0 0 12px;
        letter-spacing: -0.02em;
      }}

      header p {{
        margin: 0;
        color: var(--muted);
        max-width: 680px;
      }}

      main {{
        padding: 0 7vw 64px;
        display: grid;
        gap: 28px;
      }}

      .kpi-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 18px;
      }}

      .kpi-card {{
        background: var(--card);
        border-radius: 18px;
        padding: 18px 20px;
        box-shadow: var(--shadow);
        display: grid;
        gap: 8px;
      }}

      .kpi-card span {{
        color: var(--muted);
        font-size: 13px;
        letter-spacing: 0.08em;
        text-transform: uppercase;
      }}

      .kpi-card strong {{
        font-size: 24px;
        font-family: "Space Grotesk", sans-serif;
      }}

      .panel {{
        background: var(--card);
        border-radius: 24px;
        padding: 22px;
        box-shadow: var(--shadow);
      }}

      .panel h2 {{
        font-family: "Space Grotesk", sans-serif;
        font-size: 20px;
        margin: 0 0 16px;
      }}

      .chart-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 22px;
      }}

      img {{
        width: 100%;
        border-radius: 18px;
        box-shadow: 0 12px 35px rgba(11, 31, 42, 0.12);
      }}

      .note {{
        color: var(--muted);
        font-size: 13px;
        margin-top: 12px;
      }}

      @media (max-width: 768px) {{
        header {{
          padding: 32px 6vw 20px;
        }}

        main {{
          padding: 0 6vw 56px;
        }}
      }}
    </style>
  </head>
  <body>
    <header>
      <h1>E-commerce KPI Dashboard</h1>
      <p>
        Generated from Python with static images for trend and regression diagnostics.
      </p>
    </header>
    <main>
      <section class="kpi-grid">
        {kpi_cards}
      </section>
      <section class="panel">
        <h2>Revenue Trend</h2>
        <img src="{image_files['trend']}" alt="Revenue trend" />
        <div class="note">Monthly aggregation to highlight trend direction.</div>
      </section>
      <section class="panel">
        <h2>Scatter Diagnostics</h2>
        <div class="chart-grid">
          <div>
            <img src="{image_files['spend']}" alt="Spend vs revenue" />
            <div class="note">Marketing spend vs revenue with regression.</div>
          </div>
          <div>
            <img src="{image_files['visitors']}" alt="Visitors vs orders" />
            <div class="note">Website visitors vs orders.</div>
          </div>
          <div>
            <img src="{image_files['cac']}" alt="CAC vs revenue" />
            <div class="note">Customer acquisition cost vs revenue.</div>
          </div>
        </div>
      </section>
    </main>
  </body>
</html>
"""

    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(html)


def main():
    df = pd.read_csv(DATA_FILE, parse_dates=["Date"])
    ensure_dir(OUTPUT_DIR)

    kpis = compute_kpis(df)

    trend_path = os.path.join(OUTPUT_DIR, "revenue_trend.png")
    spend_path = os.path.join(OUTPUT_DIR, "spend_vs_revenue.png")
    visitors_path = os.path.join(OUTPUT_DIR, "visitors_vs_orders.png")
    cac_path = os.path.join(OUTPUT_DIR, "cac_vs_revenue.png")

    plot_revenue_trend(df, trend_path)
    scatter_with_regression(
        df["Marketing_Spend"].values,
        df["Revenue"].values,
        "Revenue vs Marketing Spend",
        "Marketing Spend",
        "Revenue",
        spend_path,
        "#1f7a8c",
    )
    scatter_with_regression(
        df["Website_Visitors"].values,
        df["Orders"].values,
        "Orders vs Website Visitors",
        "Website Visitors",
        "Orders",
        visitors_path,
        "#ff6b35",
    )
    scatter_with_regression(
        df["Customer_Acquisition_Cost"].values,
        df["Revenue"].values,
        "Revenue vs Customer Acquisition Cost",
        "Customer Acquisition Cost",
        "Revenue",
        cac_path,
        "#ffa62b",
    )

    image_files = {
        "trend": os.path.basename(trend_path),
        "spend": os.path.basename(spend_path),
        "visitors": os.path.basename(visitors_path),
        "cac": os.path.basename(cac_path),
    }

    html_path = os.path.join(OUTPUT_DIR, "index.html")
    build_html(kpis, image_files, html_path)
    print(f"Dashboard generated in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
