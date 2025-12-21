import requests

def test_api():
    # Базовий URL для ip-api
    # Якщо не вказати IP, поверне дані про поточну мережу
    url = "http://ip-api.com/json/"
    
    # Параметри: запитуємо конкретні поля (status, message, country, city, lat, lon, query)
    # ip-api використовує параметр 'fields' для фільтрації відповіді (опціонально)
    params = {
        "fields": "status,message,country,city,lat,lon,query"
    }

    try:
        print(f"Sending GET request to {url}...")
        r = requests.get(url, params=params)
        
        # Перевірка статус-коду
        if r.status_code == 200:
            data = r.json() # Отримання JSON [cite: 55]
            print("Response received successfully:")
            print(f"IP: {data.get('query')}")
            print(f"Location: {data.get('city')}, {data.get('country')}")
            print(f"Coordinates: Lat {data.get('lat')}, Lon {data.get('lon')}") # Виведення ключових значень [cite: 56]
            print("-" * 20)
            print("Full JSON:", data)
        else:
            print(f"Error: Status code {r.status_code}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_api()