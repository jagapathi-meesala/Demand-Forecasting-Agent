"""Deterministic moving-average demand baseline."""
from contracts.tool_contract import ToolContract,ToolMetadata,ToolError
SCHEMA={"type":"object","required":["observations","horizon"],"properties":{"observations":{"type":"array"},"horizon":{"type":"integer"}}}
def execute(p):
    obs=p["observations"]; h=p["horizon"]
    if not isinstance(obs,list) or len(obs)<2: raise ToolError("at least two observations are required")
    if isinstance(h,bool) or not isinstance(h,int) or h<1 or h>365: raise ToolError("horizon must be an integer from 1 to 365")
    vals=[]
    for i,row in enumerate(obs):
        if not isinstance(row,dict) or isinstance(row.get("demand"),bool) or not isinstance(row.get("demand"),(int,float)): raise ToolError(f"observations[{i}] has invalid demand")
        if row["demand"]<0: raise ToolError(f"observations[{i}].demand cannot be negative")
        vals.append(float(row["demand"]))
    window=min(7,len(vals)); level=sum(vals[-window:])/window
    return {"method":"moving_average","window":window,"horizon":h,"forecast":[round(level,6)]*h}
TOOL=ToolContract(ToolMetadata("forecast-demand","Produce a deterministic moving-average baseline forecast from historical demand observations.",SCHEMA),execute)
