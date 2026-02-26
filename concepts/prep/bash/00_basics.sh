#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="$SCRIPT_DIR/../pipeline/raw"
mkdir -p "$DATA_DIR"

echo "=== Generating test trade data ==="
python3 - << 'PY'
import csv
import random
from datetime import datetime, timedelta

symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
venues = ["NYSE", "NASDAQ", "BATS", "ARCA"]

output_path = "test_trades.csv"
with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ts", "symbol", "price", "qty", "venue"])
    base = datetime(2025, 1, 15, 9, 30, 0)
    for i in range(100):
        ts = base + timedelta(seconds=i*5)
        symbol = random.choice(symbols)
        price = round(random.uniform(100, 200), 2)
        qty = random.randint(10, 1000)
        venue = random.choice(venues)
        writer.writerow([ts.isoformat(), symbol, price, qty, venue])
print(f"Generated {output_path} with 100 trades")
PY

CSV_FILE="$DATA_DIR/test_trades.csv"
cp test_trades.csv "$CSV_FILE"

echo ""
echo "=== Exploring the CSV file ==="
echo "First 5 lines:"
head -n 5 "$CSV_FILE"

echo ""
echo "Last 5 lines:"
tail -n 5 "$CSV_FILE"

echo ""
echo "Line count:"
wc -l "$CSV_FILE"

echo ""
echo "File size:"
du -h "$CSV_FILE"

echo ""
echo "=== Filtering for AAPL trades ==="
grep "AAPL" "$CSV_FILE" | head -n 5

echo ""
echo "=== Using awk to get unique symbols ==="
awk -F, 'NR>1 {print $2}' "$CSV_FILE" | sort | uniq -c

echo ""
echo "=== Total quantity for each symbol (awk) ==="
awk -F, 'NR>1 {symbol=$2; qty=$4; sum[symbol]+=qty} END {for(s in sum) print s, sum[s]}' "$CSV_FILE"
