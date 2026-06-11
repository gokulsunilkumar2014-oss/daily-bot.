import requests
from datetime import datetime

URL = "https://api.open-meteo.com/v1/forecast?latitude=9.93&longitude=76.26&current=temperature_2m"

def main():
    data = requests.get(URL, timeout=30).json()
    temp = data["current"]["temperature_2m"]

    summary = f"""Daily Report
Date: {datetime.now().strftime('%Y-%m-%d')}

Weather Summary
---------------
Temperature: {temp}°C
"""

    with open("daily_report.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print(summary)

if __name__ == "__main__":
    main()
