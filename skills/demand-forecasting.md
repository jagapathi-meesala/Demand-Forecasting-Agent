# Demand Forecasting Skill

## Purpose
Validate historical demand observations and create deterministic baseline forecasts without requiring a specific ML framework.

## Inputs
Timestamped observations containing `timestamp` and non-negative numeric `demand`, plus a positive forecast horizon.

## Processing
The baseline uses the mean of the most recent up to seven observations and repeats that level for the requested horizon. Validation rejects missing fields, duplicate timestamps, invalid types, and negative demand.

## Outputs
A structured forecast containing the method, window, horizon, and forecast values.

## Limitations
This baseline does not model seasonality, trend, holidays, promotions, exogenous variables, or probabilistic uncertainty. It is a transparent baseline rather than a claim of production-level forecasting accuracy.

## Expected behavior
The same valid input produces the same output.
