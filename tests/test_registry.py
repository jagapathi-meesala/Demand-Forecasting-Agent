from core.agent_core import AgentCore
from contracts.tool_contract import ToolContract,ToolMetadata
def test_register_and_execute():
 c=AgentCore(); c.register(ToolContract(ToolMetadata('echo','echo',{'type':'object'}),lambda p:p)); assert c.execute('echo',{'x':1})['result']=={'x':1}
