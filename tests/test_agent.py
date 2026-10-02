from core.agent_core import AgentCore
from tools import validate_demand_data,forecast_demand,evaluate_forecast
def core():
    c=AgentCore(); [c.register(t) for t in (validate_demand_data,forecast_demand,evaluate_forecast)]; return c
def test_discovery_and_execution():
    c=core(); assert c.discover()==['evaluate-forecast','forecast-demand','validate-demand-data']; assert c.execute('forecast-demand',{'observations':[{'timestamp':'1','demand':10},{'timestamp':'2','demand':20}],'horizon':2})['result']['forecast']==[15.0,15.0]
def test_unknown_tool(): assert core().execute('missing',{})['ok'] is False
