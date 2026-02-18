import json
import matplotlib.pyplot as plt

with open("covid.json", "r") as file:
    data = json.load(file)

dates = []
daily_cases = []
daily_deaths = []

for entry in data:
    dates.append(entry["Date"])

    cases = entry["Daily Confirmed Cases"]
    deaths = entry["Daily  deaths"]

    daily_cases.append(cases)
    daily_deaths.append(deaths)

plt.plot(dates, daily_cases)
plt.plot(dates, daily_deaths)

plt.xlabel("Date")
plt.ylabel("Count")
plt.title("Daily COVID Cases and Deaths")
plt.xticks(rotation=45)
plt.legend(["Daily Cases", "Daily Deaths"])

plt.tight_layout()
plt.show()
