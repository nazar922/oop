typing import Any

class Station:
    
    total_stations: int = 0

    def __init__(self, name: str, stype: str, elevation: float, lat: float, lon: float) -> None:
        
        self.name: str = name
        self.stype: str = stype
        self.elevation: float = elevation
        self.lat: float = lat
        self.lon: float = lon

        Station.total_stations += 1

    def move(self, dlat: float, dlon: float) -> None:
        
        self.lat += dlatthon 
        self.lon += dlon

    def coordinates(self) -> tuple[float, float]:
        
        return self.lat, self.lon

    def elevation_info(self) -> str:
        
        return f"Висота станції {self.name}: {self.elevation} м"

    def __str__(self) -> str:
        
        return (
            f"Станція '{self.name}' ({self.stype}) — "
            f"координати: ({self.lat:.2f}, {self.lon:.2f}), "
            f"висота: {self.elevation} м"
        )

    def __repr__(self) -> str:
        
        return (
            f"Station(name='{self.name}', stype='{self.stype}', "
            f"elevation={self.elevation}, lat={self.lat}, lon={self.lon})"
        )

    def __eq__(self, other: Any) -> bool:
        
        if not isinstance(other, Station):
            return NotImplemented
        return (
            self.stype == other.stype
            and self.lat == other.lat
            and self.lon == other.lon
        )

if __name__ == "__main__":
    # Створення об’єктів
    s1 = Station("Kyiv-1", "метео", 179.0, 50.45, 30.52)
    s2 = Station("Lviv", "метео", 296.0, 49.84, 24.03)
    s3 = Station("Kyiv-1 копія", "метео", 179.0, 50.45, 30.52)

    # Виклик методів
    print(">>> Початкові координати:")
    print(s1.coordinates())
    s1.move(0.1, -0.2)
    print(">>> Нові координати після move():", s1.coordinates())

    print("\n>>> Інформація про станції:")
    print(s1)
    print(repr(s2))
    print(s2.elevation_info())

    # Перевірка рівності
    print("\n>>> Порівняння станцій:")
    print("s1 == s3 ?", s1 == s3)
    print("s2 == s3 ?", s2 == s3)

    # Перевірка службових атрибутів
    print("\n>>> Службова інформація:")
    print("dir(s1):", dir(s1))
    print("s1.__dict__:", s1.__dict__)
    print("s1.__class__:", s1.__class__)
    print("Документація класу:\n", Station.__doc__)

    print("\n>>> Загальна кількість створених станцій:", Station.total_stations)
