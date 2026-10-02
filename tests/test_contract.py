from contracts.tool_contract import ToolContract,ToolMetadata
def test_missing_required():
 t=ToolContract(ToolMetadata('x','x',{'type':'object','required':['a']}),lambda p:p); r=t.run({}); assert not r['ok']
def test_non_object():
 t=ToolContract(ToolMetadata('x','x',{'type':'object'}),lambda p:p); r=t.run([]); assert not r['ok']
