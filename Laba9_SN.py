from __future__ import annotations
from typing import Any

class Sensor:
    
    def __init__(self, name: str) -> None:
        self.name = name

    def read(self) -> str:
        
        return "Sensor data"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name})"

class ThermoSensor(Sensor):
    

    def read(self) -> str:
       
        base = super().read()
        return base + " | Temperature: 22.5°C"

class GeoSensor(Sensor):
    

    def read(self) -> str:
       
        base = super().read()
        return base + " | Coordinates: (49.84, 24.03)"

class CalibratableEntity:
   

    def calibrate(self) -> str:
        return "Calibration completed."

    def read(self) -> str:
       
        return "Calibrated data"

class CalibratedThermoSensor(CalibratableEntity, ThermoSensor):
   
    def read(self) -> str:
       base = super().read()  # проходить через MRO
        return base + " | Final processed"

class A:
    def func(self) -> str:
        return "A"

class B(A):
    def func(self) -> str:
        return "B -> " + super().func()

class C(A):
    def func(self) -> str:
        return "C -> " + super().func()

class D(B, C):
    def func(self) -> str:
        return "D -> " + super().func()

if __name__ == "__main__":
    print(" Частина 1. Успадкування")
    t = ThermoSensor("T-1")
    g = GeoSensor("G-1")

    print(t.read())
    print(g.read())

    print("\n Частина 2. Множинне успадкування ")
    ct = CalibratedThermoSensor("CT-1")
    print(ct.read())                  
    print(ct.calibrate())            

    print("\nMRO (CalibratedThermoSensor):")
    print(CalibratedThermoSensor.__mro__)

    print("\n Частина 3. Diamond Problem")
    d = D()
    print(d.func())
    print("MRO (D):", D.__mro__)
