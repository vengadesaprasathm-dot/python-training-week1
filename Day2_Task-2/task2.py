
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("API_KEY")

# 1. Send API key
try:
    r = requests.get("https://httpbin.org/headers",
                     headers={"X-API-Key": key}, timeout=5)
    r.raise_for_status()
    print("Server received key:", r.json().get("headers", {}).get("X-Api-Key"))
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Connection error")

# 2. Test timeout
try:
    r = requests.get("https://httpbin.org/delay/10", timeout=3)
    r.raise_for_status()
except requests.exceptions.Timeout:
    print("Timeout after 3 seconds: please try again")
except requests.exceptions.ConnectionError:
    print("Connection error")

# 3. Handle server error 500
try:
    r = requests.get("https://httpbin.org/status/500", timeout=5)
    r.raise_for_status()
except requests.exceptions.HTTPError:
    print("Server error 500 handled")
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Connection error")

# 4. Nested JSON and save to file
data = {"user": {"name": "Priya", "address": {"city": "Chennai"}}}
result = {
    "name": data.get("user", {}).get("name"),
    "city": data.get("user", {}).get("address", {}).get("city")
}

with open("result.json", "w") as f:
    json.dump(result, f, indent=4)

print("JSON saved successfully")
