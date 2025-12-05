

import json
import time
import requests
from typing import Any, Callable, Dict, List, Optional

def measure_time(func: Callable) -> Callable:
   
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"[TIME] {func.__name__} executed in {elapsed:.3f} seconds")
        return result
    return wrapper


def log_action(func: Callable) -> Callable:
    
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"[LOG] Starting: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished: {func.__name__}")
        return result
    return wrapper


URL: str = "https://api.saveecobot.com/output.json"
OUTPUT: str = "saveecobot.geojson"


def to_float(v: Any) -> Optional[float]:
    """Перетворює значення у float, якщо можливо."""
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


@measure_time
@log_action
def fetch_data(url: str) -> List[Dict[str, Any]]:
   
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    return response.json()


def to_feature(item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Конвертує один запис станції у GeoJSON Feature."""
    lon = to_float(item.get("longitude"))
    lat = to_float(item.get("latitude"))

    if lon is None or lat is None:
        return None

    return {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [lon, lat]},
        "properties": {
            "id": item.get("id"),
            "cityName": item.get("cityName"),
            "stationName": item.get("stationName"),
            "localName": item.get("localName"),
            "platformName": item.get("platformName"),
            "timezone": item.get("timezone"),
            "pollutants": item.get("pollutants", []),
        },
    }


def to_geojson(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Перетворює список станцій у GeoJSON FeatureCollection."""
    features = list(filter(None, map(to_feature, data)))
    return {"type": "FeatureCollection", "features": features}


def save_geojson(geojson_data: Dict[str, Any], path: str) -> None:
    """Зберігає GeoJSON у файл."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(geojson_data, f, ensure_ascii=False, indent=2)
    print(f"[SAVE] GeoJSON saved to {path}")

if __name__ == "__main__":
    data = fetch_data(URL)         
    geojson = to_geojson(data)
    save_geojson(geojson, OUTPUT)

