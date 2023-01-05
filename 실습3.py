# 1
a=int(input('정수를 입력하세요 >'))
b=-a
if a<0 :
    print(b)
else:
    print(a)


# 2
number_list = [1, 2, 3, 4, 5]
cnt=0
for numbers in  number_list:
    cnt=cnt+1
print(cnt)

# 3
number_list = [1, 2, 3, 4, 5]
cnt=0
for numbers in number_list:
    cnt=numbers+cnt   
print(cnt)

number_list = [-1, -2, -3, -4, -5]
cnt=0
for numbers in number_list:
    cnt=numbers+cnt
print(cnt)



# 4
number_list = [2, 4, 6]
cnt=0
for numbers in number_list:
    cnt=numbers+cnt  
print(cnt/3)

number_list = [2, 3, 5, 7]
cnt=0
for numbers in number_list :
    cnt=numbers+cnt  
print(cnt/4)


# 5
number_list = [1, 2, 3, 4, 5]
cnt=1
for numbers in number_list:
    cnt=numbers*cnt  
print(cnt)

number_list = [-1, -2, 3]
cnt=1
for numbers in number_list:
    cnt=numbers*cnt  
print(cnt)


# 6
number_list = [1, 2, 3, 4, 5]
mix=number_list[0]
for numbers in number_list:
    if numbers>mix :
       mix=numbers
print(mix)


# 7
number_list = [1, 2, 3, 4, 5]
min=number_list[0]
for numbers in number_list :
    if numbers<min :
       min=numbers
print(min)    