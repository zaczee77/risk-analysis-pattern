# Risk analysis pattern

A reference pattern and a small runnable demo for recording deal risks with a category, a likelihood, an impact, and a source for every risk. The pattern comes from work Nirmeet Rao has shipped: Txvni, his AI deal workspace for private equity, hedge fund, and family office teams, which ingests documents and spreadsheets for cited question answering, KPI extraction, risk analysis, benchmarks, IC memos, collaboration, and audit trail.

## The problem

A risk note is easy to write and hard to check. A memo can call a deal risky without naming what kind of risk it is, how likely it is, how much it would matter, or which document supports the claim. When a reader asks where the concern came from, the research has to be done again from the start.

A sourced risk register prevents that loss. Each risk names its category, its likelihood, its impact, and its source document. A simple score combines likelihood and impact, and a level is reported from that score, so the strongest concerns can be reviewed first.

## What the pattern does

1. Every risk category that can be recorded is named in advance in a fixed list.
2. Every risk names its category, its likelihood, its impact, and its source.
3. A risk with no source is rejected and recorded as rejected, not quietly included.
4. A risk in an unknown category is rejected, so new categories cannot appear by accident.
5. A likelihood or impact outside the range from 1 to 5 is rejected.
6. The result prints the score, the level, and the source for every accepted risk, ordered by score from highest to lowest.

## The demo in this repository

The demo folder contains a small reference demo in plain Python with no external packages. It feeds 6 invented risk observations into the register. Four risks are accepted, one risk is rejected because it has no source, and one risk is rejected because its category is unknown. The highest accepted risk scores 20 and is reported at the high level.

The docs folder describes the pattern in full: what a risk record contains, why a source is required, why the category list is fixed, and what a score can and cannot prove.

## What this is not

This demo is not the Txvni product. It models the risk analysis idea Txvni lists among its features, at miniature scale, with invented sample data. No real documents, deals, users, or outcomes appear here, and no accuracy or outcome number is claimed. A real system would add the steps this demo does not model, such as reading real documents, checking claims against sources, weighing evidence with care, and human review before any risk is used in a decision. None of those are modeled here.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao
