class Gps:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    @classmethod
    def parse_from_line(cls, line: str):
        # 49.12312,12.12312
        if line.startswith('#'):
            return None
        lat, lng = line.split(',')
        lat = float(lat)
        lng = float(lng)
        if lat > 40 and lng < 20:
            return cls(lat, lng)
        return None
    
    def __repr__(self):
        return f"{self.lat}-{self.lng}"

liste = [
    "49.12312,12.12312",
    "#49.12312,12.12312" ,
    "12.12312,8.12312" ,
    "50.12312,14.12312" 
    ]

gps_liste = []
for line in liste:
    g = Gps.parse_from_line(line)
    if g is not None:
        gps_liste.append(g)


print(gps_liste)