from pathlib import Path
import csv

import matplotlib.pyplot as plt
from datetime import datetime

path = Path('Data_Analysis/weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and high and low temperatures from the data.
dates, highs, lows = [], [], []
for row in reader:
    high = int(row[4])
    low = int(row[5])
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    highs.append(high)
    lows.append(low)
    dates.append(current_date)

# Plot the high temperatures.
plt.style.use(plt.style.available[0])
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.6)
ax.plot(dates, lows, c='blue', alpha=0.6)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily high and low temperatures, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()