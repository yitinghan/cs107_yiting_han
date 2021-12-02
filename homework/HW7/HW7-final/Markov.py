import numpy as np
from numpy.lib.function_base import select


class MarkovIterator:

    def __init__(self, mc, day_zero_weather):
        self.mc = mc
        self.current_weather = day_zero_weather

    def __iter__(self):
        return self

    def __next__(self):
        probabilities = [self.mc.get_prob(self.current_weather, next_weather) for next_weather in self.mc.weather_to_index.keys()]
        weather_list = list(self.mc.weather_to_index.keys())
        self.current_weather = np.random.choice(a=weather_list, p=probabilities)
        return self.current_weather

class Markov:
    def __init__(self, day_zero_weather=None): # You will need to modify this header line later in Part C
        self.data = [[]]
        self.weather_to_index = {"sunny":0, "cloudy":1, "rainy":2, "snowy":3, "windy":4, "hailing":5}
        self.day_zero_weather = day_zero_weather
        self._current_day = 0
        self._current_day_weather = day_zero_weather
   
    def load_data(self, file_path='./weather.csv'):
        self.data =  np.genfromtxt(file_path, delimiter=",")

    def get_prob(self, current_day_weather, next_day_weather): 
        return self.data[self.weather_to_index[current_day_weather]][self.weather_to_index[next_day_weather]]

    def __iter__(self):
        return MarkovIterator(self, self.day_zero_weather)

    def _reset(self):
        self._current_day = 0
        self._current_day_weather = self.day_zero_weather
    
    def _simulate_weather_for_day(self, day):
        self._reset()
        if day == 0:
            return self.day_zero_weather
        else:
            for i in range(day):
                self._current_day_weather = next(self.__iter__())
                self._current_day += 1
            
            prediciton = self._current_day_weather
            return prediciton
              

    def get_weather_for_day(self, day, trials=100):
        predictions = [self._simulate_weather_for_day(day) for i in range(trials)]
        return predictions
        

