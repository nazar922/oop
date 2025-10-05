class Flower:
    def __init__(self, name, color, petal_count, is_fragrant):
        self.name = name
        self.color = color
        self.petal_count = petal_count
        self.is_fragrant = is_fragrant

rose = Flower("Троянда", "червоний", 32, True)
tulip = Flower("Тюльпан", "жовтий", 6, False)

class Gardener:
    def __init__(self, name, experience, favorite_flower):
        self.name = name
        self.experience = experience
        self.favorite_flower = favorite_flower
        self.flowers = []

    def plant(self, flower):
        self.flowers.append(flower)
        print(f"{self.name} посадив {flower.name}.")

    def show_flowers(self):
        print(f"{self.name} доглядає за квітами:")
        for flower in self.flowers:
            smell = "ароматна" if flower.is_fragrant else "не ароматна"
            print(f"- {flower.name}, {flower.color}, {flower.petal_count} пелюсток, {smell}")

print("Завдання 1: Квітка (тільки атрибути)")
print(f"Квітка: {rose.name}, колір: {rose.color}, пелюсток: {rose.petal_count}, ароматна: {rose.is_fragrant}")
print(f"Квітка: {tulip.name}, колір: {tulip.color}, пелюсток: {tulip.petal_count}, ароматна: {tulip.is_fragrant}")

gardener = Gardener("Олег", 5, "Троянда")

print("\nЗавдання 2: Садівник. (атрибути і методи)")
gardener.plant(rose)
gardener.plant(tulip)
gardener.show_flowers()



