from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
REQUIRED_FILES=['agent.yaml','SOUL.md','README.md','AGENTS.md','DUTIES.md','RULES.md','EXPLAINABILITY.md','.env.example','.gitignore','requirements.txt','pytest.ini']
REQUIRED_DIRS=['adapters','config','contracts','core','skills','tools','tests','verification']
HEADINGS=['## Inputs and Data Sources','## Decision and Reasoning','## Limits and Constraints']
CONFLICTS=['## Inputs','## Decision','## Limits']
def audit():
    errors=[]
    for f in REQUIRED_FILES:
        p=ROOT/f
        if not p.is_file() or not p.read_text().strip(): errors.append(f"missing/empty file: {f}")
    for d in REQUIRED_DIRS:
        if not (ROOT/d).is_dir(): errors.append(f"missing directory: {d}")
    p=ROOT/'EXPLAINABILITY.md'
    ex=p.read_text() if p.exists() else ''
    for h in HEADINGS:
        if ex.count(h)!=1: errors.append(f"required heading count is not 1: {h}")
        if h in ex:
            section=ex.split(h,1)[1].split('\n## ',1)[0]
            if len(re.findall(r'(?<=[.!?])\s+',section))<2: errors.append(f"section has fewer than two sentences: {h}")
    for h in CONFLICTS:
        if re.search(r'^'+re.escape(h)+r'\s*$',ex,re.M): errors.append(f"conflicting heading present: {h}")
    return errors
if __name__=='__main__':
    e=audit(); print('READINESS AUDIT: PASS' if not e else '\n'.join(['READINESS AUDIT: FAIL',*e])); sys.exit(bool(e))
