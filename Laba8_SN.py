from __future__ import annotations
from typing import Optional

class River:
   
    def __init__(self, name: str, length: float, source: str) -> None:
        
        self.name = name
        self._length = length
        self.__source = source

    @property
    def source(self) -> str:
        
        return "Інформація прихована"

    @source.setter
    def source(self, new_source: str) -> None:
       
        if not new_source:
            raise ValueError("Джерело річки не може бути порожнім!")
        self.__source = new_source

    @source.deleter
    def source(self) -> None:
        
        print("Джерело річки видалено.")
        self.__source = None

    def info(self) -> str:
       
        return f"Річка {self.name}, довжина {self._length} км."

if __name__ == "__main__":

    river = River("Дніпро", 2201, "Валдайське вододільне плато")

    print(" Частина 1. Доступ до атрибутів ")
    print(river.name)       
    print(river._length)    

    try:
        print(river.__source) 
    except AttributeError:
        print("Помилка: приватний атрибут недоступний напряму!")

    print("\n Перегляд простору імен через dir() ")
    print(dir(river))  

    print("\n Частина 2. Використання @property")
    print("Отримання джерела:", river.source) 

    river.source = "Карпати"  
    print("Після зміни джерела:", river.source)

    del river.source  

    print("\n Частина 3. Перевірка name manging ")
    print("Фізичне значення приватного атрибуту:", river._River__source)

    print("\n Опис річки")
    print(river.info())
