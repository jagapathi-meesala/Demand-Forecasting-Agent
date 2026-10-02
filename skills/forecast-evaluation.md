# Forecast Evaluation Skill

## Purpose
Measure forecast error using standard deterministic metrics.

## Inputs
Equal-length non-empty numeric `actual` and `forecast` arrays.

## Processing
Compute mean absolute error (MAE), root mean squared error (RMSE), and mean absolute percentage error (MAPE) while excluding zero actual values from MAPE.

## Outputs
Return count and rounded MAE, RMSE, and MAPE percentage.

## Limitations
MAPE is undefined when every actual value is zero, so the tool returns `null` in that case. Metrics do not establish whether a forecasting model is appropriate for a particular business context.

## Expected behavior
Invalid lengths and non-numeric values produce structured errors rather than fabricated metrics.
