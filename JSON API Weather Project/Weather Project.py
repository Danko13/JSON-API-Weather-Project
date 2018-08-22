import json, requests

# Compute location from command line arguments.

location = input('Enter a city: ')
location = location.split()

if len(location) > 1:
    location = location[0] + '+' + location[1]
else:
    location = location[0]
print(location)

#TO DO: Download the JSON data from OpenWeatherMap.org's API.
api_addres = 'http://api.openweathermap.org/data/2.5/forecast?appid=04adbc9402e6cf225dc8f3ca64d9aa50&q='
url = api_addres + location

print(url)
response = requests.get(url)
response.raise_for_status()

#TO DO: Load JSON data into a Python variable

weatherData = json.loads(response.text)

# print weather descriptions.

w = weatherData['list']
print (w[0]['main']['temp'])
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])