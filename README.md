# Demand Forecasting Agent

A framework-independent OpenGAP 0.1.0 agent for validating demand time-series data, generating a deterministic moving-average baseline, and evaluating forecast accuracy.

## Architecture
`agent.yaml` declares identity, skills, and tools. `core/` contains the framework-independent registry and execution path; `contracts/` defines the tool interface; `tools/` contains domain implementations; `adapters/` provides a neutral host boundary; `verification/` contains audits.

## Installation
Create a virtual environment and install `requirements.txt`. Set the three runtime environment variables shown in `.env.example` before using configuration-dependent code.

## Configuration
No runtime secret, credential, or operational default is committed. `config/settings.py` reads required numeric configuration from environment variables.

## Tools
- `validate-demand-data`: validates timestamped demand observations.
- `forecast-demand`: creates a moving-average baseline forecast.
- `evaluate-forecast`: calculates MAE, RMSE, and MAPE.

## Skills
- `demand-forecasting`
- `forecast-evaluation`

## Usage
Instantiate `AgentCore`, register the three imported `TOOL` objects, then call `execute(tool_name, payload)`. Results are structured with `ok`, `tool`, and either `result` or `error`.

## Testing
Run `pytest -q`. Tests cover contracts, tools, registry/core behavior, adapters, security, documentation, and OpenGAP manifest validation.

## Portability
The core has no dependency on OpenAI, Claude, CrewAI, LangChain, or Lyzr. `PortableAdapter` provides a framework-neutral invocation boundary; framework-specific compatibility is not claimed as tested by this repository.

## Limitations
The built-in forecast is a transparent moving-average baseline. It does not model seasonality, trend, promotions, holidays, external drivers, uncertainty intervals, or external data sources.
