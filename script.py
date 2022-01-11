import codecademylib
import numpy as np

#Using the function np.genfromtxt to read csv file
calorie_stats = np.genfromtxt("cereal.csv", delimiter = ",")
#print(calorie_stats)

#np function to work out the mean
average_calories = np.mean(calorie_stats)
print(average_calories)

#np function to sort the list
calorie_stats_sorted = np.sort(calorie_stats)
#print(calorie_stats_sorted)

#median worked out
median_calories = np.median(calorie_stats)
print(median_calories)

nth_percentile = np.percentile(calorie_stats, 3.3)
#print(nth_percentile)

more_calories = np.mean(calorie_stats > 60) * 100
#print(more_calories)

calorie_std = np.std(calorie_stats)
