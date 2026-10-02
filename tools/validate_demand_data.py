"""Validate demand observations."""
from contracts.tool_contract import ToolContract,ToolMetadata,ToolError
SCHEMA={"type":"object","required":["observations"],"properties":{"observations":{"type":"array"}}}
def execute(p):
    obs=p["observations"]
    if not isinstance(obs,list) or not obs: raise ToolError("observations must be a non-empty array")
    seen=set(); values=[]
    for i,row in enumerate(obs):
        if not isinstance(row,dict): raise ToolError(f"observations[{i}] must be an object")
        if "timestamp" not in row or "demand" not in row: raise ToolError(f"observations[{i}] requires timestamp and demand")
        ts=row["timestamp"]; d=row["demand"]
        if not isinstance(ts,str) or not ts.strip(): raise ToolError(f"observations[{i}].timestamp must be a non-empty string")
        if isinstance(d,bool) or not isinstance(d,(int,float)): raise ToolError(f"observations[{i}].demand must be numeric")
        if d<0: raise ToolError(f"observations[{i}].demand cannot be negative")
        if ts in seen: raise ToolError(f"duplicate timestamp: {ts}")
        seen.add(ts); values.append(float(d))
    return {"valid":True,"count":len(obs),"min_demand":min(values),"max_demand":max(values)}
TOOL=ToolContract(ToolMetadata("validate-demand-data","Validate timestamped demand observations for completeness, type safety, and usable history.",SCHEMA),execute)
