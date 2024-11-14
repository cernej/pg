import time
import requests

if __name__ == "__main__":
    start = time.time()

    response = requests.get("https://www.seznam.cz")
    print(response.content)

    end = time.time()

    print(f"program bezel {end - start} sekund")