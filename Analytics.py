import csv
from datetime import datetime
from dateutil import parser

with open('TBF_Data.csv') as f:
    reader = csv.reader(f)
    tbf_data = list(reader)

dT = tbf_data[1][2]
dE = tbf_data[1][6]

d1 = parser.parse(dT).replace(tzinfo=None)
d2 = parser.parse(dE)
print(d1.date())
print(d2.date())


checkedInDayOf = 0
totalDayOf = 0
yieldRateDayOf = 0

checkedInBefore = 0
totalDayOfBefore = 0
yieldRateBefore = 0


for index,line in enumerate(tbf_data):
    if index != 0:
        dT = parser.parse(line[2]).replace(tzinfo=None)
        dE = parser.parse(line[6])
        status = line[7]
        if dT.date() == dE.date():
            totalDayOf += 1
            if status == "Attending":
                pass
            else:
                checkedInDayOf += 1
        else:
            totalDayOfBefore += 1
            if status == "Attending":
                pass
            else:
                checkedInBefore += 1


print("Yield rate of tickets bought on the day of: " + str((checkedInDayOf/totalDayOf)*100) + "%" )
print("Yield rate of tickets bought before the event: " + str((checkedInBefore/totalDayOfBefore)*100) + "%" )




#dateTicket = datetime.strptime(dT, "")
