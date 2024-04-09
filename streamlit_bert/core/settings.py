__all__ = "settings"

from dataclasses import dataclass, field
from functools import lru_cache
from typing import Dict


@dataclass
class Settings:
    API_URL: str = "https://api-inference.huggingface.co/models/google/efficientnet-b7"
    headers: Dict[str, int] = field(default_factory=
                                    lambda: {"Authorization": "Bearer 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"})


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
