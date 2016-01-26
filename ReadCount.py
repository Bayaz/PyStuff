#ReadCount.py
from sys import argv

print "Type the filename you want to analyze:"
txtFile = raw_input("> ")

data = open(txtFile)

formatData = data.read().replace('\n', ' ')

splitData = formatData.split(' ')

filteredData = filter(None, splitData)

print filteredData

print len(filteredData)

l = [1, 4, 5]

print len(l)