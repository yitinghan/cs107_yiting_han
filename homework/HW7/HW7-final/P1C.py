from Markov import Markov

city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}

day = 7
trials = 100
res = dict()

print("Number of Occurrences in seven days")
print("----------------------------------")

for i in city_weather.keys():
    markov_obj = Markov(city_weather[i])
    markov_obj.load_data()
    predictions = markov_obj.get_weather_for_day(day, trials)
    cur = dict()
    max_occ = 0
    max_weather = ""
    for j in predictions:
        cur[j] = cur.get(j, 0) + 1
        if cur[j] > max_occ:
            max_occ = cur[j]
            max_weather = j
    res[i] = max_weather
    print(cur)

print("Most likely weather in seven days")
print("----------------------------------")
for i in city_weather.keys() :
    print(i + ": " + res[i])


