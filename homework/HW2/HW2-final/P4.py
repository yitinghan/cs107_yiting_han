import numpy as np 
import matplotlib.pyplot as plt
import datetime

def clock(length):
    def clockhand(angle):
        x = length * np.cos(np.pi / 180 * angle)
        y = length * np.sin(np.pi / 180 * angle)
        return x, y
    return clockhand

currentDT = datetime.datetime.now()
hour = currentDT.hour
minute = currentDT.minute
second = currentDT.second

# Calculate theta in degrees for each hand
theta_hour = 90 - 30 * hour - minute / 2
theta_minute = 90 - 6 * minute
theta_second = 90 - 6 * second

# Specify the length of hour, minute and second hands
hour_length = 2
minute_length = 5
second_length = 10

hour_hand = clock(hour_length)
x_hour, y_hour = hour_hand(theta_hour)

minute_hand = clock(minute_length)
x_minute, y_minute = minute_hand(theta_minute)

second_hand = clock(second_length)
x_second, y_second = second_hand(theta_second)

# Plot the clock

plt.plot([0, x_hour], [0, y_hour], linewidth=6)
plt.plot([0, x_minute], [0, y_minute], linewidth=4)
plt.plot([0, x_second], [0, y_second], linewidth=1)
plt.xticks([])
plt.yticks([])
plt.axis([-10, 10, -10, 10])
plt.show()
