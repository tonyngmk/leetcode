# AGENTS.md — HFT Data Production Engineer Bootcamp

## Mission

Build an end-to-end HFT-style data pipeline from scratch over 3 days, demonstrating production-grade patterns suitable for a Data Production Engineer role at an HFT firm (e.g., HRT, Citadel, Jane Street).

## What We Are Building

A mini data platform that:
- Ingests trade data (mock or public APIs)
- Validates and cleans the data via Python generators
- Computes streaming aggregates (VWAP, volume)
- Provides observability (logging, metrics, runbooks)
- Is orchestrated by bash scripts with idempotent, rerunnable jobs

## Files

| File | Purpose |
|------|---------|
| `LEARNING_PLAN_V2.md` | Detailed step-by-step guide |
| `todo.md` | Progress tracker (checkboxes for each task) |
| `AGENTS.md` | This file — context for LLMs |

All work happens in the `concepts/prep/` directory (not a separate subfolder).

## Directory Structure (to be created)

```
concepts/prep/
├── bash/
│   ├── 00_basics.sh
│   ├── fetch_trades.sh
│   ├── etl_pipeline.sh
│   ├── lib_logging.sh
│   └── run_daily.sh
├── python/
│   ├── models.py
│   ├── parse.py
│   ├── streams.py
│   ├── errors.py
│   ├── ds_playground.py
│   └── bin/
│       ├── inspect_trades.py
│       ├── summarize_symbols.py
│       ├── clean_trades.py
│       └── aggregate_vwap.py
├── pipeline/
│   ├── raw/
│   ├── clean/
│   └── agg/
├── tests/
│   ├── test_models.py
│   └── test_streams.py
├── notes/
│   ├── journal.md
│   ├── pipeline_diagram.md
│   ├── runbook.md
│   └── cron_example.txt
├── Makefile
└── README.md
```

## How to Use This File

When the user asks for help:

1. **Find current position**: Check `todo.md` for the first unchecked task
2. **Read the task**: Look up the task number in `LEARNING_PLAN_V2.md`
3. **Help complete it**: Provide guidance, write code, debug issues
4. **Mark complete**: After the user finishes, update `todo.md` to check off the task

## Principles

- **Sequential**: Always complete Day 1 before Day 2, Day 2 before Day 3
- **Deliverable-driven**: Each task produces a concrete file
- **No skipping**: Don't move to the next task until current one is done
- **HFT mindset**: Prioritize correctness, memory efficiency, observability

## Environment

- Python 3.10+ with venv
- Dependencies: pandas, pyarrow, numpy, fastapi, pytest, mypy, rich
- Tools: bash, tmux, git, jq, curl, rg, sed, awk
