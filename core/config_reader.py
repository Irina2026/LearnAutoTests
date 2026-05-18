from pathlib import Path
from typing import Any

import yaml


class ConfigReader:
    DEFAULT_CONFIG_PATH = Path("config/config.yaml")

    _instance = None

    def __new__(cls, config_path: str | Path | None = None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load(config_path)
        return cls._instance

    def _load(self, config_path: str | Path | None = None):
        path = Path(config_path) if config_path is not None else self.DEFAULT_CONFIG_PATH

        if not path.exists():
            raise FileNotFoundError(f"Конфиг не найден: {path.absolute()}")

        with path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            self._config = data if isinstance(data, dict) else {}

    def get(self, key: str, default: Any = None) -> Any:
        current = self._config
        for part in key.split("."):
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return default
        return current

    @property
    def environment(self) -> dict:
        return self._config.get("environment", {})


