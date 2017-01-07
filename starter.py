dict = []
result = {}
start = open('wordlist.txt','r')
while True:
    line = start.readline()
    line = line.strip('\n')
    if not line:
        break
    else:
        dict.append(line)
print(dict)
end = open('dictionary.txt','w')
i = 0

while i < len(dict):
    word = dict[i]
    result[word] = input(word + ": ")
    if result[word] == "QUIT":
        break
    elif result[word] == "":
        i += 1
    else:
        end.write(word+" "+result[word]+"\n")