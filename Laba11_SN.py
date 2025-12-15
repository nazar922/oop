from typing import List, Optional, Tuple

# 1. 

class Animal:
    def eat(self) -> None:
        print("I am eating...")

class Dog(Animal):
    def bark(self) -> None:
        print("Woof! Woof!")

class Engine:
     def start(self) -> None:
        print("Engine started.")

class CarComposition:
    def __init__(self) -> None:
        self.engine = Engine()  
class CarAggregation:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine  
        
# 2. 

class Geometry:
    def __init__(self, coords: List[Tuple[float, float]]):
        self.coords = coords

    def get_count(self) -> int:
        return len(self.coords)

class Feature:
    def __init__(self, fid: int, coords: List[Tuple[float, float]], attributes: dict):
        self.fid = fid
        self.attributes = attributes
        
        self.geometry = Geometry(coords)

    def describe(self) -> None:
        print(f"[Feature ID: {self.fid}]")
        print(f" - Vertices: {self.geometry.get_count()}")
        print(f" - Attrs: {self.attributes}")

# 3. 

class Layer:
    def __init__(self, name: str):
        self.name = name

    def get_info(self) -> str:
        return f"Layer: {self.name}"

class VectorLayer(Layer): 
    def __init__(self, name: str):
        super().__init__(name)
        self.features: List[Feature] = []

    def add_feature(self, feature: Feature) -> None:
        self.features.append(feature)
    
    def get_info(self) -> str:
        return f"Vector Layer '{self.name}' with {len(self.features)} features"

class MapProject:
    def __init__(self, project_name: str):
        self.name = project_name
        self.layers: List[Layer] = []

    def add_layer(self, layer: Layer) -> None:
        self.layers.append(layer)

    def list_layers(self) -> None:
        print(f"\n Project: {self.name} ")
        for layer in self.layers:
            print(layer.get_info())

# 5.4.

class WebLayer:
    def __init__(self, url: str):
        self.url = url

    def get_info(self) -> str:
        return f"Web Layer connected to {self.url}"

# ГОЛОВНИЙ КОД 
if __name__ == "__main__":
    print(" 1. IS-A vs HAS-A ")
    dog = Dog()
    dog.eat()
    dog.bark()

    my_car_comp = CarComposition()
    my_car_comp.engine.start()

    engine_separate = Engine()
    my_car_agg = CarAggregation(engine_separate)
    my_car_agg.engine.start()

    print("\n 2 & 5. GIS Mini-Project (Composition) ")
  
    feat1 = Feature(101, [(0,0), (10,10), (10,0)], {"type": "Building"})
    feat1.describe()

    feat2 = Feature(102, [(5,5), (15,15)], {"type": "Road"})

    print("\n 3 & 5. GIS Mini-Project (Aggregation) ")
    gis_project = MapProject("Lviv City Plan")

    buildings_layer = VectorLayer("Buildings")
    roads_layer = VectorLayer("Roads")
    
    buildings_layer.add_feature(feat1)
    roads_layer.add_feature(feat2)

    gis_project.add_layer(buildings_layer)
    gis_project.add_layer(roads_layer)

    osm_layer = WebLayer("https://osm.org/api")
    print(osm_layer.get_info()) 

    gis_project.list_layers()