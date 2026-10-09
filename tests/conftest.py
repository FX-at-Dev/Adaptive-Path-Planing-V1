import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.core.config import Config, load_config

FRAME_WIDTH = 960
FRAME_HEIGHT = 540


@pytest.fixture
def config() -> Config:
    path = Path(__file__).resolve().parent.parent / "configs" / "default.yaml"
    return load_config(path) if path.exists() else Config()
