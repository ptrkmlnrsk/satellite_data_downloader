from src.domain.polygon import Polygon


def convert_to_gee_roi(roi: Polygon):
    from ee import Geometry

    return Geometry({"type": "Polygon", "coordinates": roi.coordinates})
