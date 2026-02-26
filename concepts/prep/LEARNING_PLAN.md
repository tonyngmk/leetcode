# 3-Day Intensive Hands-On Plan: Bash, Python (Classes & Generators), and Data Structures for HFT Data Production Engineer

Audience: Experienced data / software engineer targeting a Data Production Engineer role at an HFT firm (e.g. HRT).
Assumption: Comfortable with basic Linux, Python syntax, Git, and SQL.
Time Budget: ~8â€“10 focused hours per day.

---

## How to Use This Plan

- Treat each day as a full bootcamp day. If you have less time, keep the sequence but compress durations.
- Every major block has:
  - **Concept Focus** â€“ what to learn
  - **Hands-on** â€“ concrete tasks or mini-projects
  - **Deliverable** â€“ artifact you should produce (script, notebook, notes)
- Bias towards **HFT-style workflows**:
  - Unix-first mindset; reproducible pipelines
  - Streaming / incremental processing of large data
  - Correctness and observability under time pressure

Recommended environment:

- Linux or macOS with:
  - `bash`, `tmux`, `git`, `python3`, `pip`, `jq`, `curl`, `rg`/`grep`, `sed`, `awk`
- Python 3.10+ with `venv` and these packages in a dedicated env:
  - `pandas`, `pyarrow`, `numpy`, `fastapi` (optional), `pytest`, `mypy`, `rich`

Create a working directory for the 3 days:

```bash
mkdir -p hft-bootcamp/{bash,pipeline,python,tests,notes}
cd hft-bootcamp
```

Keep a `notes/journal.md` where you log what you did, issues hit, and questions.

---

## Day 1: Bash for Production Data Pipelines

Goal: Be able to write robust bash scripts that:
- Orchestrate ETL-style jobs
- Handle failures, logging, and monitoring
- Integrate with Python jobs

### 1.1 (09:00â€“10:00) Bash Foundations with a Production Mindset

**Concept Focus**
- Shell basics you will lean on constantly:
  - Job control: `&`, `jobs`, `fg`, `bg`, `Ctrl+Z`, `disown`
  - Redirection: `>`, `>>`, `2>`, `2>&1`, `|`, `tee`
  - Globbing vs regex; quoting: `'"` vs backticks
  - Exit codes: `$?`, `set -euo pipefail`
  - Shell options: `set -e`, `set -u`, `set -o pipefail`, `set -x`

**Hands-on**
- In `bash/00_basics.sh` write:
  - Commands that:
    - Download a test CSV of trades (you can fabricate or pull from some public source)
    - Show first/last lines with `head`, `tail`
    - Count lines and file size with `wc`, `du -h`
    - Pipe through `grep`, `cut`, `awk` to extract a symbolâ€™s trades
  - Use redirections to create log files: `stdout.log`, `stderr.log`.
  - Add `set -euo pipefail` at top and break things intentionally to see behavior.

**Deliverable**
- `bash/00_basics.sh` annotated with comments explaining each concept.

---

### 1.2 (10:00â€“11:30) Parameterized Bash Scripts & Environment

**Concept Focus**
- Shebang: `#!/usr/bin/env bash`
- Script arguments: `$0`, `$1`, `$@`, `getopts`
- Environment variables vs shell variables: `export`, `.env` pattern
- Safe path and temporary directories: `mktemp -d`, `trap`

**Hands-on**
- Write `bash/fetch_trades.sh` that:
  - Usage: `./fetch_trades.sh -s SYMBOL -d YYYY-MM-DD -o OUT_DIR`
  - Parses flags using `getopts`.
  - Creates output directory if missing.
  - Exports `SYMBOL`, `TRADE_DATE`, `OUT_DIR` as env vars.
  - Mocks a data vendor with `curl` to some HTTP API or simply generates fake data with `python - << 'PY' ... PY`.
  - Writes data to `OUT_DIR/trades_${SYMBOL}_${TRADE_DATE}.csv`.
- Add a `trap` to clean up temp files on `EXIT`.

**Deliverable**
- `bash/fetch_trades.sh` with usage help (`-h`).

---

### 1.3 (11:30â€“13:00) Building a Simple Bash Data Pipeline (ETL)

**Concept Focus**
- Pipelines chaining multiple programs
- Using `find`, `xargs`, `parallel`-like patterns
- Incremental/rerunnable jobs with idempotency (donâ€™t reprocess already-processed data)

**Hands-on**
- Create `pipeline/raw/`, `pipeline/stage/`, `pipeline/clean/` directories.
- Write `bash/etl_pipeline.sh` that:
  - For a given date, calls `fetch_trades.sh` for symbols from a text file `symbols.txt`.
  - Validates file existence and non-zero size.
  - Applies a simple transformation using `awk` or `python`:
    - Ensure required columns are present (e.g. `ts,symbol,price,qty,venue`)
    - Filter out invalid rows (e.g. non-positive qty or price)
  - Writes cleaned files to `pipeline/clean/`.
- Make it rerunnable: if a clean file for (symbol, date) exists, skip the work with a log message.

**Deliverable**
- `bash/etl_pipeline.sh` which runs from a single command and logs to `logs/etl_YYYYMMDD.log`.

Take a 30â€“45 minute break.

---

### 1.4 (14:00â€“15:30) Observability: Logging, Exit Codes, and Alerts

**Concept Focus**
- Logging patterns:
  - `log_info`, `log_warn`, `log_error` helper functions
  - Timestamps in logs
  - Writing both to file and stderr with `tee`
- Exit codes and `set -e` vs manual error handling
- Quick-and-dirty alerts with `mail`, Slack webhook (or just `echo` placeholders)

**Hands-on**
- Extend `bash/lib_logging.sh`:

  ```bash
  #!/usr/bin/env bash

  log_ts() {
    date +"%Y-%m-%dT%H:%M:%S%z"
  }

  log_info()  { echo "$(log_ts) [INFO]  $*"; }
  log_warn()  { echo "$(log_ts) [WARN]  $*" >&2; }
  log_error() { echo "$(log_ts) [ERROR] $*" >&2; }
  ```

- Source it from `etl_pipeline.sh` and replace raw `echo` with logging.
- Make the script exit non-zero if any symbol fails, but continue processing others:
  - Per-symbol try/catch style using `||` and aggregating failures into an array.
- At the end, if there were failures, output a summary and exit 1.

**Deliverable**
- `bash/lib_logging.sh` + updated `etl_pipeline.sh` with structured logs and aggregated status.

---

### 1.5 (15:30â€“17:30) Scheduling & Production Simulation

**Concept Focus**
- `cron`-style scheduling and pitfalls
- Time-based partitioning (by date / hour) â€“ critical in HFT
- Backfills

**Hands-on**
- Write `bash/run_daily.sh`:
  - Accepts `--date` optional; defaults to `$(date -u +%Y-%m-%d)`
  - Runs `etl_pipeline.sh` with that date
  - Writes a run marker file `state/success_${DATE}` on success
  - If run marker exists, log and exit without doing work
- Add support for backfill range: `--start-date`, `--end-date` to loop over days.
- Write a sample crontab entry in `notes/cron_example.txt` (donâ€™t actually install):

  ```cron
  # Run at 00:15 UTC every day
  15 0 * * * /path/to/hft-bootcamp/bash/run_daily.sh >> /var/log/hft_data_daily.log 2>&1
  ```

**Deliverable**
- `bash/run_daily.sh` + `notes/cron_example.txt`.

Reflection (10â€“15 minutes): add to `notes/journal.md` what felt clunky in bash that you might move to Python later.

---

## Day 2: Python Classes, Generators, and Data Structures for Streaming Data

Goal: Design Python components that:
- Represent market/data concepts with clear classes
- Use generators/iterators for streaming files and network-like feeds
- Use appropriate data structures for low-latency operations

### 2.1 (09:00â€“10:30) Python OOP for Data Production

**Concept Focus**
- Core OOP features relevant here:
  - `@dataclass` for simple records
  - Encapsulation of transformation logic in methods
  - Cohesion: classes per responsibility, not per file
  - Type hints and mypy

**Hands-on**
- In `python/models.py` define:

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

- Add a `Quote` dataclass with bid/ask, sizes, and mid-price method.
- Write `python/parse.py` with a function converting a CSV row (dict) to `Trade` instance, with validation and clear exception types.
- Add `tests/test_models.py` using `pytest` to sanity check behavior.

**Deliverable**
- `python/models.py`, `python/parse.py`, and `tests/test_models.py`.

---

### 2.2 (10:30â€“12:00) Iterators and Generators for Streaming Files

**Concept Focus**
- Iterator protocol: `__iter__`, `__next__`
- Generator functions: `yield`, lazy evaluation
- Use cases in HFT data pipelines:
  - Reading huge log / tick files line-by-line
  - Multi-stage pipelines (parse â†’ enrich â†’ filter â†’ aggregate)

**Hands-on**
- In `python/streams.py` implement:

  ```python
  from collections.abc import Iterator, Iterable
  from pathlib import Path
  from typing import TextIO
  import csv
  from .models import Trade
  from .parse import parse_trade_row  # you wrote this earlier

  def open_csv(path: Path) -> TextIO:
      return path.open("r", newline="")

  def iter_trade_rows(path: Path) -> Iterator[dict[str, str]]:
      with open_csv(path) as f:
          reader = csv.DictReader(f)
          for row in reader:
              yield row

  def iter_trades(path: Path) -> Iterator[Trade]:
      for row in iter_trade_rows(path):
          try:
              yield parse_trade_row(row)
          except ValueError:
              # log or collect bad rows in a real system
              continue
  ```

- Chain more generators:

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

- Write a CLI `python/bin/inspect_trades.py` that:
  - Accepts a path and symbol
  - Uses the generators to stream trades and prints summary stats (count, total notional, min/max price).

**Deliverable**
- `python/streams.py` and `python/bin/inspect_trades.py` (made executable with `chmod +x`).

Take a break.

---

### 2.3 (13:00â€“14:30) Data Structures for Low-Latency Operations

**Concept Focus**
- Data structure trade-offs youâ€™ll actually feel in HFT-like workloads:
  - `list` vs `deque` for queues
  - `set` / `dict` for O(1) membership and keyed storage
  - `heapq` for priority queues (e.g., soonest expiry)
  - `bisect` and sorted lists for small ordered collections
- Complexity intuition and where it matters in data production (e.g., thousands vs millions of instruments, per-symbol windows).

**Hands-on**
- In `python/ds_playground.py`:
  - Implement a sliding window VWAP calculator using `collections.deque`:

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

  - Write micro-benchmarks (simple `time.perf_counter`) comparing:
    - `list.pop(0)` vs `deque.popleft()`
    - Linear `in` over list vs membership in `set`

**Deliverable**
- `python/ds_playground.py` with VWAP and mini-benchmarks.

---

### 2.4 (14:30â€“16:00) Advanced Generators & Compositional Pipelines

**Concept Focus**
- Generator expressions
- `yield from` and composing generators
- Using standard library `itertools` for file/stream processing
- Backpressure-like patterns with `islice`, `takewhile`, `dropwhile`

**Hands-on**
- Extend `python/streams.py`:
  - Implement `chain_trade_files(paths: Iterable[Path]) -> Iterator[Trade]` using `yield from`.
  - Add `batched(iterable, n)` (Python 3.12 has `itertools.batched`, but implement your own too):

    ```python
    from collections.abc import Iterable, Iterator
    from typing import TypeVar

    T = TypeVar("T")

    def batched(iterable: Iterable[T], n: int) -> Iterator[list[T]]:
        batch: list[T] = []
        for item in iterable:
            batch.append(item)
            if len(batch) == n:
                yield batch
                batch = []
        if batch:
            yield batch
    ```

  - Use this to implement `iter_aggregated_notional(trades, batch_size=1000)` that yields partial aggregates to simulate streaming stats.
- Build a mini â€œgenerator pipelineâ€ script:
  - Reads all `pipeline/clean/*.csv` from Day 1
  - Streams them through generators
  - Outputs per-symbol summary to `stdout` without loading all data into memory.

**Deliverable**
- Updated `python/streams.py` and a `python/bin/summarize_symbols.py`.

---

### 2.5 (16:00â€“18:00) Robustness: Errors, Types, and Tests

**Concept Focus**
- Exception hierarchy for data issues (parse error, missing column, out-of-range value)
- Defensive programming vs fail-fast
- Type checking with `mypy`
- Unit tests that simulate bad rows and edge cases

**Hands-on**
- Define custom exceptions in `python/errors.py` (e.g., `ParseError`, `SchemaError`).
- Make `parse_trade_row` raise these specific exceptions.
- Decide where to catch them (in generator pipeline vs at CLI layer) and document rationale in `notes/journal.md`.
- Set up `mypy.ini` and run `mypy python/`.
- Add tests in `tests/test_streams.py` to:
  - Verify that malformed rows are skipped or bubbled up as intended.
  - Ensure VWAP window behaves correctly around boundaries.

**Deliverable**
- `python/errors.py`, updated code with types, and passing `pytest` / `mypy` (or known issues documented).

---

## Day 3: End-to-End HFT-style Data Pipeline & Production Readiness

Goal: Combine bash + Python into a cohesive, testable, and observable mini data platform simulating an HFT data production workflow.

### 3.1 (09:00â€“10:30) Designing the End-to-End Flow

**Concept Focus**
- Clarify data flow similar to an HFT data production pipeline:
  - External source â†’ raw storage â†’ validation/standardization â†’ clean store â†’ feature generation â†’ research/trade consumption
- Interfaces between bash and Python:
  - Bash for orchestration and OS interactions
  - Python for data-heavy parsing and transformation

**Hands-on**
- Draw a simple diagram (in `notes/pipeline_diagram.md`) outlining:
  - Inputs: per-symbol CSV (Day 1)
  - Processing: Python generators (Day 2)
  - Outputs: per-symbol aggregates (VWAP, volume) and anomalies
- Decide on a directory layout under `pipeline/`:
  - `raw/YYYYMMDD/`
  - `clean/YYYYMMDD/`
  - `agg/YYYYMMDD/`

**Deliverable**
- `notes/pipeline_diagram.md` with clear path conventions and responsibilities.

---

### 3.2 (10:30â€“12:30) Wiring Bash â†’ Python: Production-style ETL

**Concept Focus**
- Making bash treat Python as a first-class job step
- Exit codes and error propagation across boundaries
- Logging context (date, symbol, step) consistently

**Hands-on**
- Modify `bash/etl_pipeline.sh` to:
  - Use Python scripts rather than `awk` for transformation:
    - E.g., `python -m python.bin.clean_trades --input raw --output clean --date ... --symbol ...`
  - Capture Python exit codes; if non-zero, log and mark symbol as failed.
- Implement `python/bin/clean_trades.py`:
  - Reads raw file (path from args)
  - Uses `iter_trades` generator, validates, and writes out a normalized CSV
  - Counts discarded rows and logs summary to stderr or a log file.

**Deliverable**
- Updated `bash/etl_pipeline.sh` and new `python/bin/clean_trades.py`.

Take a break.

---

### 3.3 (13:30â€“15:00) Online-ish Aggregation and Monitoring

**Concept Focus**
- Continuous-ish aggregation pipeline
- Latency vs throughput: small batches and streaming stats
- Monitoring key metrics:
  - Rows per second
  - Error rate
  - Per-symbol data freshness

**Hands-on**
- Implement `python/bin/aggregate_vwap.py`:
  - Input: cleaned files for a given date
  - Uses `chain_trade_files` and `VwapWindow` per symbol (e.g., 5-minute window)
  - Outputs per-symbol VWAP time series to `pipeline/agg/YYYYMMDD/symbol.csv`
- Add metrics logging:
  - Use `time.perf_counter()` to compute rows/second
  - Log metrics to `logs/metrics_agg_YYYYMMDD.log`

**Deliverable**
- `python/bin/aggregate_vwap.py` and example metrics log.

---

### 3.4 (15:00â€“16:30) Simulated Incident & Runbook

**Concept Focus**
- Production incidents in data pipelines at HFT firms:
  - Missing data for certain symbols
  - Schema change from provider (extra/missing column)
  - Partial backfill required
- Runbook writing: checklists and commands that an on-call engineer can follow

**Hands-on**
- Simulate an incident:
  - Manually break a raw CSV (remove a column, introduce corrupt line)
  - Run `run_daily.sh` and observe failure surfaces.
- In `notes/runbook.md`, write:
  - **Symptom:** e.g., â€œData for symbol XYZ missing for 2025-01-15â€
  - **Diagnostic Steps:** bash one-liners and Python snippets to:
    - Check if raw file present and non-empty
    - Check if clean/agg outputs exist
    - Grep logs for errors related to that symbol and date
  - **Remediation Steps:** how to backfill just that symbol/date.

**Deliverable**
- `notes/runbook.md` with at least two incident scenarios and playbooks.

---

### 3.5 (16:30â€“18:00) Hardening & HFT-Focused Polish

**Concept Focus**
- What HFT interviewers / teams look for in this space:
  - Deterministic, reproducible runs
  - Clear separation of concerns
  - Awareness of latency and memory trade-offs
  - Operational maturity (logging, metrics, runbooks, tests)

**Hands-on**
- Add a `Makefile` at repo root with pseudo-production targets:

  ```make
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

- Add a top-level `README.md` describing the system as if you were handing it to an HRT team:
  - One-paragraph overview
  - Architecture diagram reference
  - How to run a dayâ€™s pipeline
  - How to backfill
- In `notes/journal.md`, write a short reflection (~1 page):
  - Where bash shines vs where Python should take over
  - How generators and data structures impacted the code structure
  - What youâ€™d do next with more time (e.g., Kafka, Parquet, proper metrics/alerts).

**Deliverable**
- `Makefile`, top-level `README.md`, and final reflection in `notes/journal.md`.

---

## Optional Stretch Goals (If You Have Extra Time)

- Replace CSV storage with Parquet using `pyarrow` or `pandas`.
- Add a tiny FastAPI service that reads from the aggregated VWAP files and serves REST endpoints like `/vwap?symbol=XYZ&date=YYYY-MM-DD`.
- Containerize the whole stack with Docker and a simple `docker-compose.yml`.
- Integrate a basic message-queue simulation (e.g., Redis pub/sub) where bash kicks off Python consumers.

---

## How to Leverage This for HFT Interviews

- Turn this 3-day project into a portfolio repo:
  - Clean up naming and documentation.
  - Add a short `DOCS/design.md` explaining design trade-offs.
- In interviews, be ready to walk through:
  - How the bash scripts orchestrate jobs and recover from failures.
  - How Python generators make file processing memory-efficient.
   - Why specific data structures (`deque`, `set`, `heapq`) were chosen.
- Practice whiteboard explanations of:
  - The sliding-window VWAP algorithm and its complexity.
  - How you would scale from single node to distributed (e.g., sharding by symbol, hourly partitions).

If you execute this plan with focus, you will end Day 3 with a realistic, end-to-end mini data production system thatâ€™s very close in spirit to what a Data Production Engineer at an HFT firm works on day-to-day.