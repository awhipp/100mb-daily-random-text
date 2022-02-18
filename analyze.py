##
#   This analyze function will be set on a monthly cadence to analyze the word counts for the previous month
##

import os 
import json
import datetime
import numpy as np
import matplotlib.pyplot as plt

# Get Previous Month
today = datetime.date.today()
analysis_string = today.strftime("%B %d of %Y Analysis")
image_string = today.strftime("analysis-%Y%m%d.png")
previous_analysis = 'previous_analysis.json'


path = './releases'
isExist = os.path.exists(path)

if not isExist:
  os.makedirs(path)

total_count = {}

print(analysis_string)

def letter_count(line):
    count = {}
    for i in line:
        count[i] = count.get(i,0)+1
    return count

previous_analysis_exists = os.path.exists(previous_analysis)

if previous_analysis_exists:
    with open(previous_analysis, 'r') as f:
        total_count = json.load(f)

for filename in os.listdir(path):
    f = os.path.join(path, filename)
    if os.path.isfile(f) and '.txt' in f:
        print('Analyzing %s' % f)
        with open(f, 'r') as data:
            initial_count = letter_count(data.readline())
            for letter in initial_count:
                total_count[letter] = total_count.get(letter, 0) + initial_count.get(letter)

print('New Counts --')
print(total_count)

with open(previous_analysis, 'w') as outfile:
    json.dump(total_count, outfile)

xAxis = [key for key, value in total_count.items()]
yAxis = [value for key, value in total_count.items()]
yAxis, xAxis = zip(*sorted(zip(yAxis, xAxis)))

yMin = np.min(yAxis)
yMax = np.max(yAxis)
yDiff = (yMax - yMin) / 6
yMin -= yDiff
yMax += yDiff

## BAR GRAPH ##
dpi = 96
fig = plt.figure(figsize=(3000/dpi, 2000/dpi), dpi=dpi)
plt.bar(xAxis, yAxis)
ax = plt.gca()
ax.set_ylim([yMin, yMax])
plt.title(analysis_string)
plt.xlabel('Character')
plt.ylabel('Frequency')


for i in range(len(xAxis)):
    plt.text(i, yAxis[i] + 100, "{:,}".format(yAxis[i]), rotation=90)

plt.savefig('%s/%s' % (path, analysis_string), bbox_inches='tight')