from dataclasses import dataclass


@dataclass
class Polygon:
    coordinates: list[list[tuple[float, float]]]
