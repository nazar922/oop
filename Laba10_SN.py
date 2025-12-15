from typing import List, Union, Any

class Account:
    
    def __init__(self, username: str, balance: float):
        self.username = username
        self.balance = balance

    def fee(self) -> float:
        
        return 0.0

    def limit(self) -> int:
       
        return 0

    def __add__(self, other: "Account") -> "Account":
        
        if isinstance(other, Account):
            new_user = f"{self.username}&{other.username}"
            return Account(new_user, self.balance + other.balance)
        raise TypeError("Unsupported operand type for +")

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] {self.username}: ${self.balance}"

class BasicAccount(Account):
    
    def fee(self) -> float:
        return 10.0

    def limit(self) -> int:
        return 50

class PremiumAccount(Account):
    
    def fee(self) -> float:
        return 100.0

    def limit(self) -> int:
        return 10000

class StudentAccount(Account):
    
    def fee(self) -> float:
        return 5.0

    def limit(self) -> int:
        return 20

class TrialAccess:
    
    def __init__(self, temp_id: str):
        self.temp_id = temp_id

    def fee(self) -> float:
        return 0.0  

    def __str__(self) -> str:
        return f"[Trial] {self.temp_id}"


def process_payment(obj: Any) -> None:
    
    amount = obj.fee()
    print(f"Processing payment for {obj}: ${amount}")
    
class AccountManager:
   
    @staticmethod
    def calculate_total_fees(*args: Union[Account, TrialAccess]) -> float:
        
        total = 0.0
        for item in args:
            total += item.fee()
        return total
       
if __name__ == "__main__":
    #Task 4.1
    print(f"Int sum: {1 + 2}")
    print(f"Str sum: {'Geo' + 'Spatial'}")
    print(f"List sum: {[1, 2] + [3, 4]}")

    #Task 1.5, 5.1
    users: List[Account] = [
        BasicAccount("User1", 50),
        PremiumAccount("Admin", 500),
        StudentAccount("Student1", 15),
    ]

    print("\n Polymorphism (Inheritance) ")
    for u in users:
        
        print(f"{u.username}: Fee=${u.fee()}, Limit={u.limit()} layers")

    #Task 2.3, 5.2
    print("\n Duck Typing ")
    trial = TrialAccess("Guest_01")
    process_payment(users[0])  
    process_payment(trial)     

    #Task 3
    print("\n Static Polymorphism Simulation (*args) ")
    total_2 = AccountManager.calculate_total_fees(users[0], users[1])
    total_all = AccountManager.calculate_total_fees(users[0], users[1], users[2], trial)
    print(f"Total (2 users): {total_2}")
    print(f"Total (All + Trial): {total_all}")

    #Task 4.4
    print("\n Operator Overloading ")
    acc1 = BasicAccount("A", 100)
    acc2 = BasicAccount("B", 200)
    merged = acc1 + acc2
    print(f"Merged: {merged}")  