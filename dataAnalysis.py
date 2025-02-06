from openpyxl import *
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('Google-Playstore.csv', usecols=['Maximum Installs','Installs','Minimum Installs','Rating'])
df['Rating'] = df['Rating'].replace("+","")
df['Rating'].apply(pd.to_numeric)
df['Rating']
maxInstalls = df['Maximum Installs']
rating = df['Rating'].dropna(how='all')

print('\n Rating: \n')

checkThis = rating

mean = np.mean(checkThis)
median = np.median(checkThis)
min = np.min(checkThis)
max = np.max(checkThis)
mode = stats.mode(checkThis)[0]
standard_deviation = np.std(checkThis)
variance = np.var(checkThis)
expected_value = np.mean(checkThis)

print(f'Mean average: {mean}')
print(f'Median: {median}')
print(f'Minimum: {min}')
print(f'Maximum: {max}')
print(f'Mode: {mode}')
print(f'Standard deviation: {standard_deviation}')
print(f'Dispersion: {variance}')
print(f'Expected value: {expected_value}')

if stats.normaltest(checkThis).pvalue < 0.05:
    print("is normally distributed")
else:
    print("isn't normally distributed")


print('\n Installs: \n')

checkThis = maxInstalls

mean = np.mean(checkThis)
median = np.median(checkThis)
min = np.min(checkThis)
max = np.max(checkThis)
mode = stats.mode(checkThis)[0]
standard_deviation = np.std(checkThis)
variance = np.var(checkThis)
expected_value = np.mean(checkThis)

print(f'Mean average: {mean}')
print(f'Median: {median}')
print(f'Minimum: {min}')
print(f'Maximum: {max}')
print(f'Mode: {mode}')
print(f'Standard deviation: {standard_deviation}')
print(f'Dispersion: {variance}')
print(f'Expected value: {expected_value}')

if stats.normaltest(checkThis).pvalue < 0.05:
    print("is normally distributed")
else:
    print("isn't normally distributed")
