import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from checker import check

def test_summary_passes():
    q = json.load(open(os.path.join(os.path.dirname(__file__), "..", "quests", "summary.json")))
    assert all(r["passed"] for r in check(q, "Short summary. Source: example"))

def test_summary_fails_without_source():
    q = json.load(open(os.path.join(os.path.dirname(__file__), "..", "quests", "summary.json")))
    assert not all(r["passed"] for r in check(q, "Short summary."))
