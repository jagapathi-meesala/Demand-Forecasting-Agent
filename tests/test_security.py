from tools import validate_demand_data,forecast_demand,evaluate_forecast
def test_invalid_types(): assert not validate_demand_data.run({'observations':'bad'})['ok']; assert not forecast_demand.run({'observations':[],'horizon':1})['ok']; assert not evaluate_forecast.run({'actual':[1],'forecast':[1,2]})['ok']
def test_no_secret_in_example():
 text=open('.env.example').read().lower(); assert 'password' not in text and 'api_key=' not in text and 'token=' not in text
