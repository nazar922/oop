from __future__ import annotations
from datetime import datetime
from typing import Optional

class Event:
   
    def __init__(self, name: str, date: datetime) -> None:
        
        self.name = name
        self._date = date  

    @property
    def date(self) -> datetime:
        """Повертає дату події."""
        return self._date

    @date.setter
    def date(self, new_date: datetime) -> None:
        """Змінює дату, якщо вона не None."""
        if not isinstance(new_date, datetime):
            raise ValueError("Дата повинна бути типу datetime!")
        self._date = new_date

    @date.deleter
    def date(self) -> None:
        """Видаляє атрибут _date."""
        print("Дата події видалена.")
        del self._date

    @classmethod
    def from_date(cls, date_str: str) -> "Event":
        
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return cls("Подія без назви", date)

    @staticmethod
    def is_future(date: datetime) -> bool:
       
        return date > datetime.now()

    def info(self) -> str:
        
        return f"Подія '{self.name}' відбудеться {self.date.strftime('%Y-%m-%d')}"

if __name__ == "__main__":

    event1 = Event("Концерт", datetime(2025, 5, 12))
    print(event1.info())

    event2 = Event.from_date("2025-10-20")
    print(event2.info())

    print("Чи ця дата в майбутньому?:", Event.is_future(event2.date))

    event2.date = datetime(2026, 1, 1)
    print("Після зміни дати:", event2.info())

    del event2.date
