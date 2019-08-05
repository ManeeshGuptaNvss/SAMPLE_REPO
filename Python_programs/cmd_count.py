import sys
def count_words(data):
    s=data.split(' ')
    sa=len(s)
    return sa
def count_lines(data):
    s=data.split('\n')
    for l in s:
        if not l:
            s.remove(l)
    return len(s)
file_name= sys.argv[1]
with open (file_name,'r') as dat:
    
    text= dat.read()
print(count_words(text))
print(count_lines(text))
