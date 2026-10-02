from tools import validate_demand_data,forecast_demand,evaluate_forecast
def test_validation(): assert validate_demand_data.run({'observations':[{'timestamp':'a','demand':2},{'timestamp':'b','demand':4}]})['ok']
def test_validation_rejects_negative(): assert not validate_demand_data.run({'observations':[{'timestamp':'a','demand':-1}]})['ok']
def test_forecast(): r=forecast_demand.run({'observations':[{'timestamp':'a','demand':1},{'timestamp':'b','demand':3},{'timestamp':'c','demand':5}],'horizon':2}); assert r['result']['forecast']==[3.0,3.0]
def test_metrics(): r=evaluate_forecast.run({'actual':[10,20],'forecast':[8,25]}); assert r['result']['mae']==3.5 and r['result']['rmse']==3.807887
