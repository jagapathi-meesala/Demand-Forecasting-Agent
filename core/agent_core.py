"""Framework-independent demand forecasting agent core."""
from contracts.tool_contract import ToolContract,ToolMetadata,ToolError
class AgentCore:
    def __init__(self): self._tools={}
    def register(self,tool:ToolContract):
        if not isinstance(tool,ToolContract): raise TypeError("tool must implement ToolContract")
        self._tools[tool.metadata.name]=tool
    def discover(self): return sorted(self._tools)
    def execute(self,name,payload):
        tool=self._tools.get(name)
        if tool is None: return {"ok":False,"tool":name,"error":"Unknown tool"}
        try: return tool.run(payload)
        except Exception as exc: return {"ok":False,"tool":name,"error":f"Unhandled tool failure: {exc}"}
