from pathlib import Path
from typing import Any

import yaml


class ConfigReader:
    _instance = None

    def __new__(cls, config_path: str | Path | None = None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load(config_path)
        return cls._instance

    def _load(self, config_path: str | Path | None = None):
        if config_path is None:
            path: Path = Path(__file__).parent.parent / "config" / "config.yaml"
        else:
            path: Path = Path(config_path)

        if not path.exists():
            raise FileNotFoundError(f"Конфиг не найден: {path}")

        with open(path, "r", encoding="utf-8") as f:
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

    @property
    def search(self) -> dict:
        return self._config.get("search", {})

    @property
    def selectors(self) -> dict:
        return self._config.get("selectors", {})
