"""Forecast accuracy metrics."""
from math import sqrt
from contracts.tool_contract import ToolContract,ToolMetadata,ToolError
SCHEMA={"type":"object","required":["actual","forecast"],"properties":{"actual":{"type":"array"},"forecast":{"type":"array"}}}
def execute(p):
    a,f=p["actual"],p["forecast"]
    if not isinstance(a,list) or not isinstance(f,list) or len(a)!=len(f) or not a: raise ToolError("actual and forecast must be non-empty arrays of equal length")
    pairs=[]
    for i,(x,y) in enumerate(zip(a,f)):
        if any(isinstance(z,bool) or not isinstance(z,(int,float)) for z in (x,y)): raise ToolError(f"values at index {i} must be numeric")
        pairs.append((float(x),float(y)))
    errors=[x-y for x,y in pairs]
    mae=sum(abs(e) for e in errors)/len(errors); rmse=sqrt(sum(e*e for e in errors)/len(errors))
    nonzero=[(x,e) for x,e in zip(a,errors) if float(x)!=0]
    mape=(sum(abs(e)/abs(float(x)) for x,e in nonzero)/len(nonzero)*100) if nonzero else None
    return {"count":len(pairs),"mae":round(mae,6),"rmse":round(rmse,6),"mape_percent":None if mape is None else round(mape,6)}
TOOL=ToolContract(ToolMetadata("evaluate-forecast","Calculate MAE, RMSE, and MAPE for aligned actual and forecast series.",SCHEMA),execute)
