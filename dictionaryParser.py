def Parser():
    swipeDict = {}

    f = open('fullwords.txt', 'r')
    end = open('newDict.txt', 'w')

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
        if not line:
            break
        else:
            if not line.lower() in swipeDict.keys():
                swipeDict[line.lower()] = line.lower()
                end.write(line.lower() + " " + line.lower() + "\n")
    return swipeDict

def saver(swipeDict):
    end = open('dictionary.txt', 'w')
    for word in swipeDict:
        end.write(word + " " + swipeDict[word] + "\n")
    print('Done')
print(Parser())