from crypte import*
import sys

#phrase = sys.argv[1]
phrase = "hello"

lst = []

for i in range(20000):
    lst.append(encode_string(phrase))
    
d = dict()  
    
for i in lst:
    if lst.count(i) > 1:
        d[i]=lst.count(i)
    else:
        pass
for i in d:
    print(i, d[i])

