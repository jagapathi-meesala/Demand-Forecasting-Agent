"""Framework-independent tool contract."""
from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class ToolMetadata:
    name: str
    description: str
    input_schema: dict

class ToolError(Exception): pass

class ToolContract:
    metadata: ToolMetadata
    execute_fn: Callable[[dict], dict]
    def __init__(self, metadata: ToolMetadata, execute_fn: Callable[[dict], dict]):
        self.metadata, self.execute_fn = metadata, execute_fn
    def validate(self, payload: Any) -> None:
        if not isinstance(payload, dict): raise ToolError("Input must be an object")
        required=self.metadata.input_schema.get("required",[])
        missing=[k for k in required if k not in payload]
        if missing: raise ToolError(f"Missing required fields: {', '.join(missing)}")
        props=self.metadata.input_schema.get("properties",{})
        for k,v in payload.items():
            if k in props and props[k].get("type")=="array" and not isinstance(v,list): raise ToolError(f"{k} must be an array")
    def run(self,payload:dict)->dict:
        try:
            self.validate(payload)
            return {"ok":True,"tool":self.metadata.name,"result":self.execute_fn(payload)}
        except ToolError as exc:
            return {"ok":False,"tool":self.metadata.name,"error":str(exc)}
        except (ValueError,TypeError,KeyError) as exc:
            return {"ok":False,"tool":self.metadata.name,"error":str(exc)}
