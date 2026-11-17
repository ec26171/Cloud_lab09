import requests
from pprint import pprint

crime_url_template = 'https://data.police.uk/api/crimes-street/all-crime?date={date}&lat={lat}&lng={lng}'

my_latitude = '52.629729'
my_longitude = '-1.131592'
my_date = '2026-01'

crime_url = crime_url_template.format(lat = my_latitude, lng = my_longitude, date = my_date)

#resp = requests.get('https://data.police.uk/api/crimes-street/all-crime?date=2024-01&lat=52.629729&lng=-1.131592')
resp = requests.get(crime_url)

if resp.ok:
  crimes= resp.json()
else:
  print(resp.reason)

categories_url_template = 'https://data.police.uk/api/crime-categories?date={date}'

resp2 = requests.get(categories_url_template.format(date = my_date))

if resp2.ok:
  categories_json = resp2.json()
else:
  print(resp2.reason)

categories = {categ["url"]:categ["name"] for categ in categories_json}

crime_category_stats = dict.fromkeys(categories.keys(), 0)
crime_category_stats.pop("all-crime")


for crime in crimes:
  crime_category_stats[crime["category"]] += 1
pprint(crime_category_stats)

crime_outcome_stats = {'None': 0}
for crime in crimes:
  outcome = crime["outcome_status"]
if not outcome:
  crime_outcome_stats['None'] += 1
elif outcome['category'] not in crime_outcome_stats.keys():
  crime_outcome_stats.update({outcome['category']:1})
else:
  crime_outcome_stats[outcome['category']] += 1
pprint(crime_outcome_stats)
