# 3-Day Intensive Hands-On Plan: Bash, Python (Classes & Generators), and Data Structures for HFT Data Production Engineer

**Objective**: Build a working end-to-end HFT-style data pipeline from scratch.
**Outcome**: A portfolio-ready mini data platform demonstrating production-grade patterns.

Audience: Experienced data / software engineer targeting a Data Production Engineer role at an HFT firm (e.g. HRT).
Assumption: Comfortable with basic Linux, Python syntax, Git, and SQL.
Time Budget: ~8–10 focused hours per day.

---

## How to Use This Plan

- **One task at a time**: Each numbered item below is a discrete to-do. Complete them in order.
- **Day structure**: Each day has 4-5 tasks. Finish Day 1 before starting Day 2.
- **Verify deliverable**: Each task has a clear file/product to produce. Don't move on until it exists.
- **Journal**: Keep `notes/journal.md` updated with reflections after each day.

### Environment Setup (Do First)

Create your working directory:

```bash
cd /Users/bytedance/Documents/code/leetcode/concepts/prep
mkdir -p bash pipeline/{raw,stage,clean,agg} python/{bin} tests notes logs state
```

Install Python dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas pyarrow numpy fastapi pytest mypy rich
```

---

## Day 1: Bash for Production Data Pipelines

Goal: Be able to write robust bash scripts that orchestrate ETL jobs, handle failures, and integrate with Python.

### Task 1.1 — Bash Foundations (09:00–10:00)

**Concept Focus**: Job control, redirection, quoting, exit codes, shell options.

**Hands-on**:
- Create `bash/00_basics.sh` that:
  - Downloads or generates a test CSV with trade data
  - Uses `head`, `tail`, `wc`, `du -h` to explore the file
  - Pipes through `grep`, `cut`, `awk` to extract a symbol's trades
  - Redirects stdout/stderr to separate log files
  - Add `set -euo pipefail` and break things to understand behavior

**Deliverable**: `bash/00_basics.sh` with comments explaining each concept.

---

### Task 1.2 — Parameterized Scripts & Environment (10:00–11:30)

**Concept Focus**: Shebang, script arguments (`$0`, `$1`, `$@`, `getopts`), environment variables, `trap` for cleanup.

**Hands-on**:
- Write `bash/fetch_trades.sh`:
  - Usage: `./fetch_trades.sh -s SYMBOL -d YYYY-MM-DD -o OUT_DIR`
  - Parses flags with `getopts`
  - Creates output directory if missing
  - Exports `SYMBOL`, `TRADE_DATE`, `OUT_DIR` as env vars
  - Generates mock trade data (or fetches from a public API)
  - Writes to `OUT_DIR/trades_${SYMBOL}_${TRADE_DATE}.csv`
  - Uses `trap` to clean up temp files on EXIT

**Deliverable**: `bash/fetch_trades.sh` with `-h` usage help.

---

### Task 1.3 — Build a Simple ETL Pipeline (11:30–13:00)

**Concept Focus**: Pipelines, `find`/`xargs`, idempotency (rerunnable jobs).

**Hands-on**:
- Create directories: `pipeline/raw/`, `pipeline/stage/`, `pipeline/clean/`
- Create `symbols.txt` with a list of trading symbols
- Write `bash/etl_pipeline.sh`:
  - Takes a date argument
  - Calls `fetch_trades.sh` for each symbol in `symbols.txt`
  - Validates files exist and are non-empty
  - Transforms data using `awk` or Python:
    - Ensures required columns: `ts,symbol,price,qty,venue`
    - Filters invalid rows (non-positive qty/price)
  - Writes cleaned files to `pipeline/clean/`
  - Skips work if clean file already exists (idempotent)

**Deliverable**: `bash/etl_pipeline.sh` that logs to `logs/etl_YYYYMMDD.log`.

Break: 30–45 minutes.

---

### Task 1.4 — Observability: Logging & Alerts (14:00–15:30)

**Concept Focus**: Structured logging functions, timestamps, exit codes, error aggregation.

**Hands-on**:
- Create `bash/lib_logging.sh`:

```bash
#!/usr/bin/env bash
log_ts() { date +"%Y-%m-%dT%H:%M:%S%z"; }
log_info()  { echo "$(log_ts) [INFO]  $*"; }
log_warn()  { echo "$(log_ts) [WARN]  $*" >&2; }
log_error() { echo "$(log_ts) [ERROR] $*" >&2; }
```

- Source it in `etl_pipeline.sh` and replace raw `echo` calls
- Modify `etl_pipeline.sh` to:
  - Track per-symbol failures in an array
  - Continue processing other symbols if one fails
  - Exit non-zero if any symbol failed, with summary

**Deliverable**: `bash/lib_logging.sh` + updated `bash/etl_pipeline.sh` with structured logs.

---

### Task 1.5 — Scheduling & Backfills (15:30–17:30)

**Concept Focus**: `cron`, time-based partitioning, backfill patterns.

**Hands-on**:
- Write `bash/run_daily.sh`:
  - Accepts `--date` (defaults to today UTC)
  - Runs `etl_pipeline.sh` with that date
  - Creates `state/success_${DATE}` marker on success
  - Skips if marker exists
  - Supports `--start-date` and `--end-date` for backfill ranges
- Write `notes/cron_example.txt` with a sample crontab entry:

```cron
# Run at 00:15 UTC every day
15 0 * * * /path/to/hft-bootcamp/bash/run_daily.sh >> /var/log/hft_data_daily.log 2>&1
```

**Deliverable**: `bash/run_daily.sh` + `notes/cron_example.txt`.

**Reflection** (10 min): Write in `notes/journal.md` what felt clunky in bash that you'd prefer to handle in Python.

---

## Day 2: Python Classes, Generators, and Data Structures

Goal: Build Python components with clear OOP, streaming generators, and efficient data structures.

### Task 2.1 — Python OOP for Data Models (09:00–10:30)

**Concept Focus**: `@dataclass`, encapsulation, type hints, mypy.

**Hands-on**:
- Create `python/models.py`:

```python
from dataclasses import dataclass
from datetime import datetime
from typing import NewType

Venue = NewType("Venue", str)

@dataclass(frozen=True)
class Trade:
    ts: datetime
    symbol: str
    price: float
    qty: int
    venue: Venue

    def notional(self) -> float:
        return self.price * self.qty
```

- Add a `Quote` dataclass (bid, ask, bid_size, ask_size, mid_price method)
- Create `python/parse.py` with `parse_trade_row(dict) -> Trade` and validation
- Add `tests/test_models.py` with pytest tests

**Deliverable**: `python/models.py`, `python/parse.py`, `tests/test_models.py`.

---

### Task 2.2 — Iterators and Generators (10:30–12:00)

**Concept Focus**: Iterator protocol, generator functions, lazy evaluation, streaming.

**Hands-on**:
- Create `python/streams.py`:

```python
from collections.abc import Iterator, Iterable
from pathlib import Path
import csv
from .models import Trade
from .parse import parse_trade_row

def iter_trade_rows(path: Path) -> Iterator[dict[str, str]]:
    with path.open("r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

def iter_trades(path: Path) -> Iterator[Trade]:
    for row in iter_trade_rows(path):
        try:
            yield parse_trade_row(row)
        except ValueError:
            continue
```

- Add generator filters:

```python
def filter_symbol(trades: Iterable[Trade], symbol: str) -> Iterator[Trade]:
    for t in trades:
        if t.symbol == symbol:
            yield t

def filter_min_notional(trades: Iterable[Trade], min_notional: float) -> Iterator[Trade]:
    for t in trades:
        if t.notional() >= min_notional:
            yield t
```

- Create executable `python/bin/inspect_trades.py` that streams trades and prints stats

**Deliverable**: `python/streams.py` + `python/bin/inspect_trades.py`.

Break.

---

### Task 2.3 — Data Structures for Low-Latency (13:00–14:30)

**Concept Focus**: `deque`, `dict`, `set`, `heapq`, `bisect`; complexity trade-offs.

**Hands-on**:
- Create `python/ds_playground.py`:
  - Implement `VwapWindow` using `collections.deque`:

```python
from collections import deque
from datetime import datetime, timedelta
from .models import Trade

class VwapWindow:
    def __init__(self, window: timedelta) -> None:
        self.window = window
        self._trades: deque[Trade] = deque()
        self._sum_notional: float = 0.0
        self._sum_qty: int = 0

    def add(self, trade: Trade) -> None:
        self._trades.append(trade)
        self._sum_notional += trade.notional()
        self._sum_qty += trade.qty
        self._evict_old(trade.ts)

    def _evict_old(self, now: datetime) -> None:
        cutoff = now - self.window
        while self._trades and self._trades[0].ts < cutoff:
            old = self._trades.popleft()
            self._sum_notional -= old.notional()
            self._sum_qty -= old.qty

    def vwap(self) -> float | None:
        if self._sum_qty == 0:
            return None
        return self._sum_notional / self._sum_qty
```

  - Write micro-benchmarks comparing `list.pop(0)` vs `deque.popleft()`, list membership vs set

**Deliverable**: `python/ds_playground.py` with VWAP and benchmarks.

---

### Task 2.4 — Advanced Generators & Pipelines (14:30–16:00)

**Concept Focus**: `yield from`, `itertools`, compositional pipelines.

**Hands-on**:
- Extend `python/streams.py`:
  - Implement `chain_trade_files(paths: Iterable[Path]) -> Iterator[Trade]` with `yield from`
  - Add `batched(iterable, n)` generator
  - Implement `iter_aggregated_notional(trades, batch_size=1000)` yielding partial aggregates
- Create `python/bin/summarize_symbols.py`:
  - Streams all `pipeline/clean/*.csv` files
  - Outputs per-symbol summary without loading all data into memory

**Deliverable**: Updated `python/streams.py` + `python/bin/summarize_symbols.py`.

---

### Task 2.5 — Robustness: Errors, Types, Tests (16:00–18:00)

**Concept Focus**: Custom exceptions, defensive programming, mypy, pytest.

**Hands-on**:
- Create `python/errors.py` with custom exceptions: `ParseError`, `SchemaError`
- Update `parse_trade_row` to raise specific exceptions
- Document error handling strategy in `notes/journal.md`
- Create `mypy.ini` and run `mypy python/`
- Add tests in `tests/test_streams.py`:
  - Malformed rows are handled correctly
  - VWAP window behaves at boundaries

**Deliverable**: `python/errors.py`, type-checked code, passing tests.

---

## Day 3: End-to-End Pipeline & Production Readiness

Goal: Combine bash + Python into a cohesive, testable, observable data platform.

### Task 3.1 — Design the End-to-End Flow (09:00–10:30)

**Concept Focus**: Data flow architecture, bash/Python interface boundaries.

**Hands-on**:
- Create `notes/pipeline_diagram.md` with:
  - Data flow: external source → raw → validation → clean → aggregation
  - Directory layout:
    ```
    pipeline/
      raw/YYYYMMDD/
      clean/YYYYMMDD/
      agg/YYYYMMDD/
    ```

**Deliverable**: `notes/pipeline_diagram.md`.

---

### Task 3.2 — Wire Bash → Python ETL (10:30–12:30)

**Concept Focus**: Exit codes across boundaries, consistent logging.

**Hands-on**:
- Update `bash/etl_pipeline.sh` to call Python scripts:
  - `python -m python.bin.clean_trades --input raw --output clean --date ... --symbol ...`
  - Capture Python exit codes; mark symbol failed if non-zero
- Create `python/bin/clean_trades.py`:
  - Reads raw CSV using `iter_trades`
  - Validates and writes normalized CSV to clean/
  - Logs discarded row count

**Deliverable**: Updated `bash/etl_pipeline.sh` + `python/bin/clean_trades.py`.

Break.

---

### Task 3.3 — Streaming Aggregation & Metrics (13:30–15:00)

**Concept Focus**: Continuous aggregation, latency/throughput, monitoring.

**Hands-on**:
- Create `python/bin/aggregate_vwap.py`:
  - Input: cleaned files for a date
  - Uses `chain_trade_files` + per-symbol `VwapWindow` (5-min windows)
  - Outputs per-symbol VWAP time series to `pipeline/agg/YYYYMMDD/symbol.csv`
  - Logs metrics: rows/sec, error rate to `logs/metrics_agg_YYYYMMDD.log`

**Deliverable**: `python/bin/aggregate_vwap.py` + sample metrics log.

---

### Task 3.4 — Incident Simulation & Runbook (15:00–16:30)

**Concept Focus**: Debugging, runbooks, backfill procedures.

**Hands-on**:
- **Simulate incident**: Corrupt a raw CSV (remove column, add bad line), run `run_daily.sh`, observe failures
- Create `notes/runbook.md` with at least two scenarios:
  - **Symptom**: Missing data for symbol XYZ
  - **Diagnostic Steps**: Check raw file, clean output, grep logs
  - **Remediation**: Backfill command

**Deliverable**: `notes/runbook.md`.

---

### Task 3.5 — Hardening & Polish (16:30–18:00)

**Concept Focus**: Production maturity, interviewer-ready artifacts.

**Hands-on**:
- Create `Makefile`:

```makefile
.PHONY: test typecheck lint etl-day agg-day

test:
    pytest -q

typecheck:
    mypy python

etl-day:
    bash/bash/run_daily.sh --date=$(DATE)

agg-day:
    python -m python.bin.aggregate_vwap --date=$(DATE)
```

- Create top-level `README.md` describing the system for an HFT team
- Write final reflection in `notes/journal.md`:
  - Bash vs Python trade-offs
  - How generators changed the code structure
  - Next steps (Kafka, Parquet, proper alerting)

**Deliverable**: `Makefile`, `README.md`, final journal entry.

---

## Optional Stretch Goals

- Replace CSV with Parquet using `pyarrow`
- Add FastAPI service to serve VWAP endpoints
- Containerize with Docker + docker-compose
- Add Redis pub/sub simulation

---

## How to Leverage This for HFT Interviews

- Clean up the repo: consistent naming, good docs
- Add `DOCS/design.md` explaining trade-offs
- Be ready to discuss:
  - How bash orchestrates jobs and recovers from failures
  - How generators make processing memory-efficient
  - Why specific data structures (`deque`, `set`, `heapq`) were chosen
- Practice whiteboard explanations:
  - Sliding-window VWAP algorithm complexity
  - Scaling from single node to distributed (sharding by symbol, hourly partitions)
