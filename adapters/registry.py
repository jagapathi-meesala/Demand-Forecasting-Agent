"""Adapter registry for host integrations."""
from .portable_adapter import PortableAdapter
class AdapterRegistry:
    def __init__(self): self._adapters={}
    def register(self,name:str,adapter:PortableAdapter):
        if not name or not isinstance(adapter,PortableAdapter): raise ValueError("Invalid adapter registration")
        self._adapters[name]=adapter
    def get(self,name:str): return self._adapters.get(name)
    def names(self): return sorted(self._adapters)
