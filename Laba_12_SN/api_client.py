# api_client.py
import requests
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class ApiClient(ABC):
    """Base API client abstract class.""" # [cite: 79]

    def __init__(self, base_url: str):
        self.base_url = base_url

    @abstractmethod
    def fetch(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Abstract method to fetch data.""" # [cite: 81]
        raise NotImplementedError("Subclasses must implement fetch()")

class GuestClient(ApiClient):
    """Guest client. Can only check own IP address (no specific IP param allowed).""" # [cite: 88]

    def fetch(self, params: Dict[str, Any] = None) -> Dict[str, Any]:
        # Гість робить запит без параметрів, отримуючи інфо про себе
        print("Guest: Fetching info about own IP...")
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"status": "fail", "message": str(e)}

class BasicUserClient(ApiClient):
    """Standard user. Can query specific IPs.""" # [cite: 92]

    def fetch(self, params: Dict[str, Any]) -> Dict[str, Any]:
        # Звичайний користувач може передати IP адресу в URL
        target_ip = params.get("ip", "")
        url = f"{self.base_url}/{target_ip}" if target_ip else self.base_url
        
        print(f"User: Fetching info for IP {target_ip if target_ip else 'self'}...")
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"status": "fail", "message": str(e)}

class AdminClient(ApiClient):
    """Admin client with private token simulation and extended fields.""" # [cite: 100]

    def __init__(self, base_url: str, token: str):
        super().__init__(base_url)
        self._token = token  # Інкапсуляція приватного атрибуту [cite: 103]

    def fetch(self, params: Dict[str, Any]) -> Dict[str, Any]:
        # Адмін додає токен (симуляція) та запитує розширені поля
        target_ip = params.get("ip", "")
        url = f"{self.base_url}/{target_ip}" if target_ip else self.base_url
        
        # Симуляція додавання токена в хедери або параметри
        request_params = {
            "key": self._token, 
            "fields": "status,message,country,city,lat,lon,zip,isp,org,as,query" # Розширені дані
        }
        
        print(f"Admin: Fetching extended info with secure token...")
        try:
            response = requests.get(url, params=request_params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"status": "fail", "message": str(e)}