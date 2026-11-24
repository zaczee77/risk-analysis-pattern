"""Reference demo: recording deal risks with category, likelihood, impact, and source.

Every sample name and figure in this file is invented.
The demo models the risk analysis step described for Txvni, an AI deal
workspace that lists risk analysis among its features. It is not the
Txvni product and it makes no claim about real usage or outcomes.
"""

ALLOWED_CATEGORIES = [
    "customer_concentration",
    "supplier_dependency",
    "regulatory",
    "market",
    "operational",
]


def level_for(score):
    if score >= 15:
        return "high"
    if score >= 8:
        return "medium"
    return "low"


class RiskRegister:
    def __init__(self, allowed_categories):
        self.allowed_categories = list(allowed_categories)
        self.risks = []
        self.rejected = []

    def add_risk(self, category, likelihood, impact, source):
        if category not in self.allowed_categories:
            self.rejected.append((category, "unknown category"))
            return False
        if not source or not source.strip():
            self.rejected.append((category, "missing source"))
            return False
        if not (1 <= likelihood <= 5) or not (1 <= impact <= 5):
            self.rejected.append((category, "value out of range"))
            return False
        score = likelihood * impact
        self.risks.append(
            {
                "category": category,
                "likelihood": likelihood,
                "impact": impact,
                "score": score,
                "level": level_for(score),
                "source": source,
            }
        )
        return True

    def sorted_risks(self):
        return sorted(self.risks, key=lambda item: item["score"], reverse=True)


SAMPLE_OBSERVATIONS = [
    ("customer_concentration", 4, 5, "sample_risk_notes.md"),
    ("supplier_dependency", 3, 4, "sample_risk_notes.md"),
    ("regulatory", 2, 5, "sample_compliance_notes.md"),
    ("market", 2, 2, "sample_market_notes.md"),
    ("operational", 3, 3, ""),
    ("cybersecurity", 4, 4, "sample_risk_notes.md"),
]


def main():
    register = RiskRegister(ALLOWED_CATEGORIES)
    accepted = 0
    for category, likelihood, impact, source in SAMPLE_OBSERVATIONS:
        if register.add_risk(category, likelihood, impact, source):
            accepted += 1

    total = len(SAMPLE_OBSERVATIONS)
    print(f"{total} observations received, {accepted} accepted, {len(register.rejected)} rejected")
    assert total == 6 and accepted == 4 and len(register.rejected) == 2

    reasons = sorted(reason for _, reason in register.rejected)
    print(f"rejection reasons: {reasons}")
    assert reasons == ["missing source", "unknown category"]

    ordered = register.sorted_risks()
    for item in ordered:
        print(
            f"{item['category']}: likelihood {item['likelihood']}, "
            f"impact {item['impact']}, score {item['score']}, "
            f"level {item['level']}, source {item['source']}"
        )

    scores = [item["score"] for item in ordered]
    print(f"scores in review order: {scores}")
    assert scores == [20, 12, 10, 4]

    levels = [item["level"] for item in ordered]
    print(f"levels in review order: {levels}")
    assert levels == ["high", "medium", "medium", "low"]

    print("all checks passed")


if __name__ == "__main__":
    main()
