from dataclasses import dataclass


@dataclass
class Polygon:
    coordinates: list[list[tuple[float, float]]]

    def convert_to_gee_roi(self):
        from ee import Geometry

        return Geometry({"type": "Polygon", "coordinates": self.coordinates})
