import csv
import json

csvfile = open('country_latlon.csv', 'rU')
jsonfile = open('country_latlon.json', 'w')

fieldnames = ("Country","Alpha-2 code","Numeric code","Latitude (average)","Longitude (average)")
reader = csv.DictReader(csvfile, fieldnames)
print reader
index = 0
data = {}
for row in reader:
	if index == 0:
		pass
	else:
		data[row["Country"]] = {"longitude": row["Longitude (average)"], "latitude": row["Latitude (average)"]}
	index += 1
json.dump(data, jsonfile)