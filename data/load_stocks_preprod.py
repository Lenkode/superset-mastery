import pandas as pd
from sqlalchemy import create_engine, text

print("Reading CSV...")
df = pd.read_csv("all_stocks_5yr.csv")

# Clean up column names
df.columns = [c.lower().strip() for c in df.columns]

# Parse date
df["date"] = pd.to_datetime(df["date"])

print(f"Loaded {len(df):,} rows, {df['name'].nunique()} tickers")
print(df.head())

# Connect to datadb
engine = create_engine("postgresql+psycopg2://analyst:analyst@localhost:5536/finance")

print("Loading into PostgreSQL...")
df.to_sql("stock_prices", engine, if_exists="replace", index=False, chunksize=10000)

print("Creating indexes...")
with engine.connect() as conn:
    conn.execute(text("CREATE INDEX IF NOT EXISTS idx_stock_date ON stock_prices(date);"))
    conn.execute(text("CREATE INDEX IF NOT EXISTS idx_stock_name ON stock_prices(name);"))
    conn.commit()

print("All done!")
