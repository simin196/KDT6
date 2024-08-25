import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data= csv.reader(f)

print(data)