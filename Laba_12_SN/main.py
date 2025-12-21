# main.py
from api_client import GuestClient, BasicUserClient, AdminClient
from validator import ApiResponseValidator
from geojson_converter import GeoJsonConverter

def main():
    BASE_URL = "http://ip-api.com/json"

    print("--- Scenario 1: Guest (Own IP) ---")
    guest = GuestClient(BASE_URL)
    data_guest = guest.fetch() # Поліморфізм: виклик без параметрів
    
    val_guest = ApiResponseValidator()
    val_guest.data = data_guest
    if val_guest.has_required_keys(["lat", "lon", "city"]):
        print("Guest data valid.")
    else:
        print("Guest data invalid.")

    print("\n--- Scenario 2: Admin (Specific IP + Token) ---")
    # Використовуємо AdminClient для демонстрації інкапсуляції
    admin = AdminClient(BASE_URL, token="SECRET_KEY_123") # [cite: 102]
    
    # Google Public DNS IP для тесту
    target_params = {"ip": "8.8.8.8"} 
    
    # 1. Отримання даних
    raw_data = admin.fetch(target_params) # [cite: 188]
    print(f"Raw response: {raw_data}")

    # 2. Валідація
    validator = ApiResponseValidator() # [cite: 191]
    try:
        validator.data = raw_data
        
        required_keys = ["lat", "lon", "country", "isp"]
        if validator.has_required_keys(required_keys) and validator.validate_coordinates():
            print("Validation passed.")
            
            # 3. Конвертація
            converter = GeoJsonConverter(validator.data) # [cite: 196]
            feature = converter.to_feature(lon_key="lon", lat_key="lat")
            
            # 4. Збереження
            filename = "google_dns_loc.geojson"
            converter.save(filename, feature) # [cite: 197]
            print(f"Process completed. Data saved to {filename}")
        else:
            print("Validation failed. Check API response.")
            
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()