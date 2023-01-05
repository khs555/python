n = int(input('정수를 입력하세요 >'))

if n  <= 0:
    print('False')
else:
    print('True')



n1 = int(input('첫 번째 정수를 입력하세요 >'))
n2 = int(input('두 번째 정수를 입력하세요 >'))

if n1>n2 :
    print(n1)
elif n2>n1 :
    print(n2)
else: 
    print('False')


n3 = int(input('정수를 입력하세요 >'))

if 1 <n3< 10 :
    print('True')
else:
    print('False')


n4 = int(input('정수를 입력하세요 >'))

if n4>0 and n4%2==0 :
    print('True')
else:
    print('False')


n5 = int(input('정수를 입력하세요 >'))

if n5>100 :
    print('에러')
elif n5<0 :
    print('에러')
elif n5>=60 :
    print('합격')
elif n5<60 :
    print('불합격')


a = input('문자열을 입력하세요 >')

for word in a[::-1]:
    print(word)


n6 = int(input('첫 번째 정수를 입력하세요 >'))
n7 = int(input('두 번째 정수를 입력하세요 >'))

if n6>n7 :
    for a in range(n7+1,n6):
        print(a)    
elif n7>n6 :
    for b in range(n6+1,n7):
        print(b) 
else: 
    print('False')



n8 = int(input('첫 번째 정수를 입력하세요 >'))
n9 = int(input('두 번째 정수를 입력하세요 >'))

if n8>n9 :
    for c in range(n8-1,n9,-1) :
        print(c)
elif n8<n9 :
    for d in range(n9-1,n8,-1) :
        print(d)        
else: 
    print('False')


n10 = int(input('정수를 입력하세요 >'))
if n10<1 :
    print('Flase')
elif n10%2==0 :
    for e in range(1,n10,2) :
        print(e)
else:
    for f in range(1,n10,2):
        print(f)


for n11 in range(2,10):
    for n12 in range(2,10):
        print(n11,'x',n12,'=',n11*n12) 

