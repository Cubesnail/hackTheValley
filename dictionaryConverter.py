swipeDict = {'hgfrerjklo': 'hello'}

f = open ('dictionary.txt', 'r')

for line in f:
    firstspace = line.find(' ', beg=0, end=len(line))

    value = line[0:firstspace]
    key = line[firstspace + 1:len(line)]

    if not swipeDict.has_key(key):
        swipeDict[key] = value;


swipeDict.items()
