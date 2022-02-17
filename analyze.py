##
#   This analyze function will be set on a monthly cadence to analyze the word counts for the previous month
##

import os 
import datetime
import matplotlib.pyplot as plt

# Get Previous Month
today = datetime.date.today()
analysis_string = today.strftime("%B %d of %Y Analysis")
image_string = today.strftime("analysis-%Y%m%d.png")


path = './releases'
isExist = os.path.exists(path)

if not isExist:
  os.makedirs(path)

directory = 'files'
total_count = {}

print(analysis_string)

def letter_count(line):
    count = {}
    for i in line:
        count[i] = count.get(i,0)+1
    return count

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        print('Analyzing %s' % f)
        with open(f, 'r') as data:
            initial_count = letter_count(data.readline())
            for letter in initial_count:
                total_count[letter] = total_count.get(letter, 0) + initial_count.get(letter)

print(total_count)

xAxis = [key for key, value in total_count.items()]
yAxis = [value for key, value in total_count.items()]
# yAxis, xAxis = zip(*sorted(zip(yAxis, xAxis)))

## BAR GRAPH ##
dpi = 96
fig = plt.figure(figsize=(3000/dpi, 2000/dpi), dpi=dpi)
plt.bar(xAxis, yAxis)
plt.title(analysis_string)
plt.xlabel('Character')
plt.ylabel('Frequency')


for i in range(len(xAxis)):
    plt.text(i, yAxis[i] + 1000, "{:,}".format(yAxis[i]), rotation=45)

plt.savefig('%s/%s' % (path, analysis_string))