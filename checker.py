"""Check a submission against a quest's acceptance criteria."""
import json, sys

def check(quest, submission):
    results = []
    for c in quest["acceptance_criteria"]:
        kind, val = c["type"], c.get("value")
        if kind == "contains":
            ok = val in submission
        elif kind == "max_chars":
            ok = len(submission) <= val
        elif kind == "min_chars":
            ok = len(submission) >= val
        else:
            ok = False
        results.append({"criterion": c["description"], "passed": ok})
    return results

if __name__ == "__main__":
    quest = json.load(open(sys.argv[1]))
    sub = open(sys.argv[2]).read()
    res = check(quest, sub)
    for r in res:
        print(("PASS" if r["passed"] else "FAIL"), r["criterion"])
    sys.exit(0 if all(r["passed"] for r in res) else 1)
