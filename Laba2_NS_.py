import inspect

class City:
   
    country = "Україна"

    def __init__(self, name, population, coordinates):
        
        self.name = name
        self.population = population
        self.coordinates = coordinates

    def info(self):
        
        print(f"Місто: {self.name}")
        print(f"Населення: {self.population}")
        print(f"Координати: {self.coordinates}")
        print(f"Країна: {City.country}")

    def move(self, dlat, dlon):
       
        lat, lon = self.coordinates
        self.coordinates = (lat + dlat, lon + dlon)


class LandPlot:

    base_rate_uah_per_ha = 1200.0

    def __init__(self, cadastral_number, area_ha, category):
        
        self.cadastral_number = cadastral_number
        self.area_ha = area_ha
        self.category = category

    def info(self):
       
        print(f"Кадастровий номер: {self.cadastral_number}")
        print(f"Площа (га): {self.area_ha}")
        print(f"Категорія: {self.category}")
        print(f"Базова ставка: {LandPlot.base_rate_uah_per_ha} грн/га")

    def calculate_tax(self, category_coeff):
       
        return self.area_ha * LandPlot.base_rate_uah_per_ha * category_coeff

# Створення об'єктів City

vinnytsia = City("Вінниця", 370000, (49.2328, 28.481))
cherkasy = City("Черкаси", 280000, (49.4444, 32.0597))

vinnytsia.info()
print("\nЗміна координат Вінниці...")
vinnytsia.move(0.1, -0.1)
vinnytsia.info()

print("\nІнформація про Черкаси:")
cherkasy.info()

# Створення об'єктів LandPlot

plot1 = LandPlot("0510100000:02:001:0010", 2.5, "житлова")
plot2 = LandPlot("0510100000:02:001:0011", 5.0, "с/г")

print("\nІнформація про ділянки:")
plot1.info()
print(f"Податок: {plot1.calculate_tax(1.2):.2f} грн")

print()
plot2.info()
print(f"Податок: {plot2.calculate_tax(0.8):.2f} грн")




