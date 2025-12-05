from typing import Callable


def make_ticket_formatter(prefix: str, start: int) -> Callable[[int], str]:
    
    def format_ticket(seq_number: int) -> str:
        
        ticket_number = start + seq_number
        return f"{prefix}-{ticket_number:04d}"

    return format_ticket

if __name__ == "__main__":
    # Створюємо три різні форматувачі квитків
    eco_ticket = make_ticket_formatter("ECO", 1000)
    vip_ticket = make_ticket_formatter("VIP", 500)
    bus_ticket = make_ticket_formatter("BUS", 1)

    # Виклики вкладеної функції
    print(eco_ticket(5))   
    print(eco_ticket(25))  
    print(vip_ticket(10))  
    print(vip_ticket(0))   
    print(bus_ticket(7))   
    print(bus_ticket(99))  
