from adapters.portable_adapter import PortableAdapter
from adapters.registry import AdapterRegistry
class Runner:
 def execute(self,n,p): return {'ok':True,'tool':n,'result':p}
def test_adapter():
 r=AdapterRegistry(); a=PortableAdapter(Runner()); r.register('neutral',a); assert r.get('neutral').invoke('x',{'a':1})['ok']
