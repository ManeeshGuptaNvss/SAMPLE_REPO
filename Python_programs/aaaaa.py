import sys
if len(sys.argv)<2:
    print('error')
    exit()
def count_words(data):
    words= data.split()
    count= len(words)
    return count
def count_lines(data):
    lines= data.split('\n')
    for l in lines:
        if l is '' :
            lines.remove(l)
    return len(lines)
with open (sys.argv[1],'r') as d:
    text=d.read()
print(count_words(text))
print(count_lines(text))


