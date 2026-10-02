"""Minimal framework-neutral adapter boundary.
No external agent framework is imported by the core implementation.
"""
from typing import Any
class PortableAdapter:
    framework="framework-independent"
    def __init__(self, runner): self.runner=runner
    def invoke(self, tool_name:str, payload:dict)->dict: return self.runner.execute(tool_name,payload)
