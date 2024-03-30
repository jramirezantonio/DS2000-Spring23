'''
    Josue Antonio
    DS 2000
    02/27- Spring 2023
    miniviz.py
'''
import math
import matplotlib.pyplot as plt
RENT_FILE = "rent_boston.txt"

with open(RENT_FILE, "r") as infile:
    data = []
    infile.readline()
    for line in infile:
        data.append(line.strip().split(","))

data = data[::-1]
data = data[47:]

dates = []
rents = []
for i in range(len(data)):
    dates.append(data[i][0])
    rents.append(int(data[i][1]))
    
positions = [i for i in range(0,25)]
plt.figure(figsize=(18, 8))
plt.plot(positions, rents, "--", color = "royalblue")
plt.scatter(positions, rents, color = "royalblue", label = "Rents")
plt.hlines(rents[0], -0.25, 0.25, color = "green", label = "Dec. 2020 rent")
plt.hlines(rents[12], 11.75, 12.25, color = "orange", label = "Dec. 2021 rent")
plt.hlines(rents[24], 23.75, 24.25, color = "red", label = "Dec. 2022 rent")
print(rents[0], rents[12], rents[24])
plt.xticks(positions, dates, rotation = 60)
plt.ylim(2466, 3549)
plt.xlabel("Month/Year")
plt.ylabel("Median Rent")
plt.title("Median Rent in Boston since end of 2020")
plt.legend()
