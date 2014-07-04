import itertools
str =''
num=2
all=[]
mas = ['-','a','b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for n in itertools.product(mas, repeat=3):
    if ((n[0] != '-') and (n[num] != '-')): all.append(''.join(n)+'.ru')
#print all
#
head = open("name.txt", "a+")
for tmp in all:
    head.write(tmp+"\n")
