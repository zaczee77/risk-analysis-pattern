# Demo: risk analysis

A small reference demo of the risk analysis idea behind Txvni: each risk names a category, a likelihood, an impact, and a source, risks with no source or an unknown category are rejected with a reason, and a score and a level are computed from the supplied values only.

## How to run it

From the repository root, or from this folder:

```
python3 demo/risk_demo.py
```

Plain Python, no external packages, no network calls.

## What it does

1. It feeds 6 invented observations into the register, covering customer concentration, supplier dependency, regulatory, market, and operational categories, plus one observation for an unknown category.
2. It accepts 4 risks and rejects 2: one operational observation with no source, and one cybersecurity observation whose category is not in the fixed list.
3. It computes scores of 20, 12, 10, and 4 by multiplying likelihood by impact for each accepted risk.
4. It reports the levels high, medium, medium, and low in review order, with the source printed for each accepted risk.

## What it printed when it was tested

6 observations received, 4 accepted, 2 rejected with reasons missing source and unknown category, scores 20, 12, 10, and 4 in review order, levels high, medium, medium, and low, and all checks passed.

## What the sample data is

Every risk, value, and document name in `risk_demo.py` is invented sample data written only to exercise the pattern. Nothing here is a real document, a real deal, a real risk assessment, a real user, or a real decision. A real system would build risks from real ingested documents, check each claim against its source, and keep human review before any risk is used in a decision. None of that is modeled here.

## Files

1. `risk_demo.py`: the demo. The fixed category list, the sample observations, the level function, the register, the rejection rules, and the built in assertions.
2. `README.md`: this file.
