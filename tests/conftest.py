from typing import Optional

from src.core.classes import category_for
from src.core.types import BBox, PotholeInfo, TrackedObject

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.core.config import Config, load_config
from src.geometry.ego_path import EgoPath

FRAME_WIDTH = 960
FRAME_HEIGHT = 540


@pytest.fixture
def config() -> Config:
    path = Path(__file__).resolve().parent.parent / "configs" / "default.yaml"
    return load_config(path) if path.exists() else Config()

@pytest.fixture
def ego_path(config: Config) -> EgoPath:
    path = EgoPath(config)
    path.configure(FRAME_WIDTH, FRAME_HEIGHT)
    return path

def make_object(
    track_id: int = 1,
    class_name: str = "person",
    bbox: tuple[float, float, float, float] = (430, 240, 500, 430),
    distance: Optional[float] = 10.0,
    confidence: float = 0.9,
    hits: int = 10,
    velocity_px: tuple[float, float] = (0.0, 0.0),
    closing_speed: Optional[float] = None,
    pothole: Optional[PotholeInfo] = None,
) -> TrackedObject:
    """Build a tracked object with sensible defaults."""
    obj = TrackedObject(
        track_id=track_id,
        class_name=class_name,
        confidence=confidence,
        bbox=BBox(*bbox),
        category=category_for(class_name),
        age=hits,
        hits=hits,
        estimated_distance=distance,
        velocity_px=velocity_px,
        speed_px=(velocity_px[0] ** 2 + velocity_px[1] ** 2) ** 0.5,
        pothole=pothole,
    )
    if distance is not None:
        obj.distance_history = [distance] * 6
    obj.closing_speed_mps = closing_speed
    return obj
