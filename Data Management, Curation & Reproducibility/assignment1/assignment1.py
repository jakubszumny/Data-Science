import requests
import json
import pandas as pd
import hashlib
import matplotlib

with open("fred_apikey.txt", "r") as f:
    apikey = f.readline().strip()

series = "SP500"
start = "2019-01-01"
end = "2024-01-01"
url = (f"https://api.stlouisfed.org/fred/series/observations?"
      f"series_id={series}&api_key={apikey}"
      f"&observation_start={start}&observation_end={end}&file_type=json")

response = requests.get(url)
response.raise_for_status()

json_data = response.json()

with open("assignment1/sp500.json", "w") as f:
    f.write(json.dumps(json_data, indent=4))

df = pd.json_normalize(json_data, 'observations')

print(df.head())
print(df.dtypes)

df = df.drop(["realtime_start", "realtime_end"], axis=1)
df = df.dropna()
df = df[df.value != "."]

print(df.head())

df.to_csv("assignment1/data/sp500.csv", lineterminator= '\n')

df["date"] = pd.to_datetime(df["date"])
df["value"] = pd.to_numeric(df["value"])

df = df.set_index(["date"])
plt = df.plot(title="S&P 500 (2019-2024)", legend=False)
plt.set_xlabel("Date")
plt.set_ylabel("Index Value")
plt.get_figure().savefig("assignment1/results/sp500.png")

with open("assignment1/data/sp500.csv", "rb") as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()

with open("assignment1/data/sp500.sha", "w") as f:
    f.write(sha256hash)

import datetime
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:$S")

url = (f"https://api.stlouisfed.org/fred/series/observations?"
      f"series_id={series}&api_key={'api_key'}"
      f"&observation_start={start}&observation_end={end}&file_type=json")

entry = f"""@misc{{{"Federal Reserve Economic Data".replace(' ', '_')}_{"2024"},
  author = "Federal Reserve Economic Data",
  title = "S&P 500 Index",
  publisher = "Federal Reserve Economic Data (FRED)",
  year = "2024",
  note = f"Retrieved on {date}",
  url = {url}
}}
"""

with open("assignment1/data_citation.bib", "w") as f:
    f.write(entry)