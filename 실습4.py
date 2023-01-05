#1
a=input('문자열을 입력하세요 >')
n=0
for s in a :
    if s in 'e':
        print(n+1)

#2
b=input('문자열을 입력하세요 >')
n=0
for lists in b[0:] :
    if lists in {'a', 'i', 'o', 'u', 'e', 'A', 'I', 'O', 'U', 'E' }:
        n=n+1
print(n)        

#3
dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}
dict_variable["나이"] = 24

print(dict_variable["나이"])

#4
name=input('이름을 입력하세요 >')
number=input('전호번호을 입력하세요 >')
residence=input('거주지을 입력하세요 >')

c={'이름':name, '전호번호':number, '거주지':residence}

print(c)

for d in c :
    print(d,':',c[d])

#5
name=input('이름을 입력하세요 >')
number=input('전호번호을 입력하세요 >')
e_mail=input('이메일을 입력하세요 >')
residence=input('거주지을 입력하세요 >')

e={'이름':name}
f={'전호번호':number, '이메일':e_mail, '거주지':residence}
for g in e:
    print( '{', e[g],':',  f, '}')

#6
l=input('문자열을 입력하세요 >')
dict_variable={}

for l2 in l :
    cnt=0
    for l3 in l :
        if l2 in l3 :
            cnt+=1
    dict_variable[l2]=cnt
    

for n,m in dict_variable.items():
    print(n,m)