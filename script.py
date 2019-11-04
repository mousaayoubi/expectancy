import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")

#print(data.head())

#Store life expectancy in a variable
life_expectancy = data["Life Expectancy"]

#Find quartiles of the data
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.5, 0.75])
print(life_expectancy_quartiles)

#Plot histogram
#plt.hist(life_expectancy)
#plt.show()

#Store GDP in a variable
gdp = data["GDP"]
print(gdp)

#Find median of GDP
median_gdp = np.quantile(gdp, 0.5)
print(median_gdp)

#Find all countries with gdp lower than the median
low_gdp = data[data['GDP'] <= median_gdp]
high_gdp = data[data['GDP'] > median_gdp]

#Find low gdp life expectancy quartiles
low_gdp_quartiles = np.quantile(low_gdp["Life Expectancy"], [0.25, 0.5, 0.75])
print(low_gdp_quartiles)

#Find high gdp life expectancy quartiles
high_gdp_quartiles = np.quantile(high_gdp["Life Expectancy"], [0.25, 0.5, 0.75])
print(high_gdp_quartiles)

plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()