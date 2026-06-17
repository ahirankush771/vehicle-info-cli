import requests
import sys
import json
from urllib.parse import quote

API_BASE = "https://num-tg-info-api.vercel.app/info"

def get_vehicle_info(vehicle_number: str):
    try:
        url = f"{API_BASE}?vehicle={quote(vehicle_number.strip().upper())}"
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return data
    except requests.exceptions.RequestException as e:
        print(f"❌ API Error: {e}")
        return None
    except json.JSONDecodeError:
        print("❌ Invalid JSON response from API")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: vehicle-info <vehicle-number>")
        print("Example: vehicle-info TS09AB1234")
        sys.exit(1)
    
    vehicle = sys.argv[1]
    print(f"🔍 Looking up vehicle: {vehicle.upper()}")
    get_vehicle_info(vehicle)

if __name__ == "__main__":
    main()
