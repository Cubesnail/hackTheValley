def getDict():
    swipeDict = {'hgfrerjklo': 'hello'}

    f = open('dictionary.txt', 'r')

    # for line in f:
    #     firstspace = line.find(' ', beg=0, end=len(line))
    #
    #     value = line[0:firstspace].lower
    #     key = line[firstspace + 1:len(line)].lower
    #
    #     if not swipeDict.has_key(key):
    #         swipeDict[key] = value;
    # swipeDict.items()
    while True:
        line = f.readline()
        line = line.strip('\n')
        parsed = line.split(' ')
        if not line:
            break
        else:
            if not parsed[1] in swipeDict.keys():
                swipeDict[parsed[1]] = parsed[0]
    return swipeDict

print(getDict())