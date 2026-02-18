import json
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

with open("covid.json", "r") as file:
    data = json.load(file)

dates = []
daily_cases = []
daily_deaths = []

for entry in data:
    dates.append(datetime.strptime(entry["Date"], "%Y/%m/%d"))

    cases = entry["Daily Confirmed Cases"]
    deaths = entry["Daily  deaths"]

    daily_cases.append(cases)
    daily_deaths.append(deaths)

plt.figure(figsize=(10, 5))
plt.plot(dates, daily_cases)
plt.plot(dates, daily_deaths)

plt.xlabel("Date")
plt.ylabel("Count")
plt.title("Daily COVID Cases and Deaths")

plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

plt.xticks(rotation=45)
plt.legend(["Daily Cases", "Daily Deaths"])

plt.tight_layout()
plt.show()
