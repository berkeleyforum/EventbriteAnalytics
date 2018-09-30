import csv
import matplotlib.pyplot as plt
from dateutil import parser

with open('TBF_Data.csv') as f:
    reader = csv.reader(f)
    tbf_data = list(reader)

yieldRates = [46.10745614035088, 40.96190616267098, 40.01522732216663, 38.996558594457525, 38.77223914088796, 38.28684095224186, 37.163529339628425, 36.80112044817927, 36.77562747330189, 36.76274708295594, 36.71793805861567, 36.6618601297765, 36.78318135764944, 36.8334414126802, 36.89842209072978, 36.90411634212472, 36.90229715074436, 36.900478138709516, 36.900478138709516, 36.90176943171177]

def getYieldRates():
    checkedInDayOf, totalDayOf, yieldRateDayOf = 0, 0, 0
    for i in range(1, 21):
        for index,line in enumerate(tbf_data):
            if index != 0:
                dT = parser.parse(line[2]).replace(tzinfo=None)
                dE = parser.parse(line[6])
                status = line[7]
                if abs((dT-dE).days) == i:
                    totalDayOf += 1
                    if status == "Checked In":
                        checkedInDayOf += 1

        yieldRates.append((checkedInDayOf / totalDayOf) * 100)

x_pos = [x for x in range(1,21)]

plt.plot(x_pos, yieldRates)
plt.xticks(x_pos)
plt.xlabel("Ticket bought days before")
plt.ylabel("Yield Rate Percentage")
plt.show()