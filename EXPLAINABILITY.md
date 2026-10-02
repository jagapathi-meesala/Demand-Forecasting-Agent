## Inputs and Data Sources
The agent accepts user-supplied timestamped demand observations containing a timestamp and non-negative numeric demand. The data source is the input payload supplied to the tool; the built-in implementation does not silently fetch external data.

### Input Requirements
Each observation must be an object with `timestamp` and `demand`, timestamps must be unique, and demand must be numeric and non-negative. Forecast requests also require a positive integer horizon within the supported range.

### Failure Handling
Malformed objects, missing fields, duplicate timestamps, invalid numeric types, negative demand, invalid horizon values, and mismatched evaluation arrays produce structured errors. The agent does not replace invalid values with fabricated defaults.

## Decision and Reasoning
The forecast decision is a deterministic moving-average baseline using the most recent up to seven valid demand observations. The forecast level is calculated as the arithmetic mean of that window and repeated for each requested future period.

### Rules Applied
Forecast evaluation calculates MAE as the mean absolute error and RMSE as the square root of mean squared error. MAPE is calculated over non-zero actual values because percentage error is undefined when an actual value is zero.

### Expected Outputs
Forecast responses identify the method, window, horizon, and forecast values. Evaluation responses identify sample count and the calculated MAE, RMSE, and MAPE percentage.

### Worked Example
For recent demand values of 10, 20, and 30 with a horizon of two, the baseline level is 20 and the forecast is [20, 20]. If actual values are [18, 22], the evaluation tool reports deterministic error metrics from those aligned pairs.

## Limits and Constraints
The baseline does not model trend, seasonality, promotions, holidays, weather, pricing, stock-outs, or other exogenous drivers. It also does not provide probabilistic prediction intervals or guarantee operational demand outcomes.

### Constraints
The built-in forecast horizon is limited to 365 periods, and at least two historical observations are required. MAPE returns null when every actual value is zero.

### Known Issues
A moving average can lag rapidly changing demand and may be unsuitable where strong seasonal or causal patterns dominate. Forecast quality must therefore be assessed against appropriate historical baselines and business requirements.

### Unsupported Behavior
The agent does not connect to external databases, APIs, ERP systems, or cloud forecasting services unless a separate tested adapter is added. It does not claim framework-specific execution merely because adapter boundaries exist.
