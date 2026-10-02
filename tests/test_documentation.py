from pathlib import Path
def test_required_docs():
 for p in ['README.md','SOUL.md','RULES.md','DUTIES.md','AGENTS.md','EXPLAINABILITY.md']: assert Path(p).read_text().strip()
def test_explainability_headings():
 s=Path('EXPLAINABILITY.md').read_text(); assert all(h in s for h in ['## Inputs and Data Sources','## Decision and Reasoning','## Limits and Constraints']); assert '## Inputs\n' not in s and '## Decision\n' not in s and '## Limits\n' not in s
