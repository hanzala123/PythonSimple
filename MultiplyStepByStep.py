frst = input('First Number: ')
sec = input('Second number: ')
a = '' * 10
ans  = int(frst) * int(sec)
num = int(frst)
print('{:>8}'.format(str(frst)))
tmp = len(str(frst))-len(str(sec))
fl = " " * tmp
print('{:>8}'.format('X'+ fl + str(sec)))

print('-' * 10)
last = ''
out = []
for i,j in enumerate(reversed(sec)):
    pl = 'X' * i
    last = str(int(j)* num)
    print('{:>8}'.format(last + pl))
        

for i in out:
    print(i)
print('-'*10)
print('{:>8}'.format(ans))

