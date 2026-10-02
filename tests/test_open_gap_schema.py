from pathlib import Path
import re, yaml

def test_manifest_schema_static_rules():
    data=yaml.safe_load(Path("agent.yaml").read_text())
    allowed={"spec_version","name","version","description","author","license","model","extends","dependencies","skills","tools","agents","delegation","runtime","a2a","compliance","registries","tags","mcp_servers","metadata"}
    assert set(data) <= allowed
    assert data["spec_version"] == "0.1.0"
    assert re.fullmatch(r"^[a-z][a-z0-9-]*$",data["name"])
    assert re.fullmatch(r"^\d+\.\d+\.\d+(-[a-zA-Z0-9.]+)?(\+[a-zA-Z0-9.]+)?$",data["version"])
    assert isinstance(data["description"],str) and data["description"]
    assert all(re.fullmatch(r"^[a-z][a-z0-9-]*$",x) for x in data["skills"])
    assert all(re.fullmatch(r"^[a-z][a-z0-9-]*$",x) for x in data["tools"])
