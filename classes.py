class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return f"Waypoint: {self.name}, {self.lat}, {self.lon}"

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return f"Geocache: {self.name}, {self.difficulty}, {self.size}, {self.lat}, {self.lon}"

waypoint = Waypoint("Catacombs", 41.7050, -121.51521)

print(waypoint)

geocache =  Geocache("Newberry Views", "diff: 1.5", "size: 2", 44.05137, -121.41556)

print(geocache)