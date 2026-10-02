"""Environment-only runtime configuration."""
import os


def _required_int(name: str) -> int:
    raw=os.getenv(name)
    if raw is None or raw.strip()=="":
        raise ValueError(f"Missing required environment variable: {name}")
    try: value=int(raw)
    except ValueError as exc: raise ValueError(f"{name} must be an integer") from exc
    if value<=0: raise ValueError(f"{name} must be positive")
    return value


def load_settings() -> dict:
    return {
        "max_rows": _required_int("DEMAND_FORECAST_MAX_ROWS"),
        "default_horizon": _required_int("DEMAND_FORECAST_DEFAULT_HORIZON"),
        "min_history": _required_int("DEMAND_FORECAST_MIN_HISTORY"),
    }
