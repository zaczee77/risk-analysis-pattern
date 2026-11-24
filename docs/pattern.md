# The risk analysis pattern

## Where the pattern comes from

Txvni is an AI deal workspace built by Nirmeet Rao and presented on his portfolio at nirmeetrao.com. Its own description lists document and spreadsheet ingestion, cited question answering, KPI extraction, risk analysis, benchmarks, IC memos, collaboration, and audit trail. Risk analysis sits in the middle of that chain. Earlier steps extract facts from documents, and later steps such as IC memos use the recorded risks when they explain what could go wrong with a deal.

The same need appears wherever a team records concerns about a decision. If the category, the likelihood, the impact, and the source travel with the claim, a reader can check the claim in one step. If they do not, checking means redoing the research.

## The risk record

A risk record holds a category name, a likelihood value, an impact value, and a source name. The category says what kind of risk it is. The likelihood and the impact each run from 1 to 5, where 1 is the lowest and 5 is the highest. The source name is the document the risk came from, named exactly as it was ingested, so a reader can find it again.

The register computes one score from the two values by multiplying likelihood by impact. The score runs from 1 to 25. A score of 15 or more is reported at the high level, a score of 8 or more is reported at the medium level, and any lower score is reported at the low level.

## The four rules

1. A source is required. A risk with an empty source is rejected and the rejection is recorded with its reason. A claim that cannot be traced is not included quietly and is not fixed by guessing a source.
2. Categories are fixed in advance. The register holds the list of category names it accepts. A risk naming a category outside that list is rejected, so the report keeps the shape the team expects and new categories cannot appear by accident.
3. Values stay in range. A likelihood or impact outside the range from 1 to 5 is rejected, because a score built from an out of range value would not compare fairly with the other risks.
4. The highest scores are reviewed first. Sorting the accepted risks by score from highest to lowest makes the review order plain and keeps the strongest recorded concerns at the top.

## Design principles

1. A score is not a judgment. The register reports a score and a level from two supplied values. It does not say whether the risk is real, well supported, or important enough to change a decision. That judgment stays with human review.
2. Rejection is information. The rejected list, with reasons, tells the team exactly what work remains: find a source for one risk, or decide whether a new category truly belongs in the list.
3. A score is a narrow claim. It combines two numbers that a person supplied. It does not prove the numbers are correct, the evidence is strong, or the risk will happen. Those judgments stay outside the register.
4. The source stays visible in the output. Printing the source with each risk makes checking cheap for the reader and keeps the habit of sourcing strong for the writer.

## What the demo shows, and what it does not show

The demo shows the pattern at miniature scale: 6 invented observations, 4 accepted, 2 rejected with reasons, scores of 20, 12, 10, and 4, and levels high, medium, medium, and low. It does not show real documents, real extraction, real risk judgment, real figures, or the Txvni product, and it claims no accuracy or outcome result. It is a reference implementation of the pattern, written in plain Python with no external packages.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao
