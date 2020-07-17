class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon)
        super().__init__(name, lat lon)
        self.difficulty = difficulty
        self.size = size
