# 개수 세기
zork = 0
print('Before', zork)
numbers = [9, 41, 12, 3, 74, 15]
for thing in numbers :
    zork = zork + 1
    print(zork, thing)
print('After', zork)
# Before 0
# 1 9
# 2 41
# 3 12
# 4 3
# 5 74
# 6 15
# After 6

# 합계
zork = 0
print('Before', zork)
numbers = [9, 41, 12, 3, 74, 15] 
for thing in numbers :
    zork = zork + thing
    print(zork, thing)
print('After', zork)
# Before 0
# 9 9
# 50 41
# 62 12
# 65 3
# 139 74
# 154 15
# After 154

# 평균
count = 0 # 평균을 전체 원소의 수로 나누기 위해 total number를 확인
sum = 0
print('Before', count, sum)
numbers = [9, 41, 12, 3, 74, 15] 
for value in numbers :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)
# Before 0 0
# 1 9 9
# 2 50 41
# 3 62 12
# 4 65 3
# 5 139 74
# 6 154 15
# After 6 154 25.666666666666668

# 필터링
print('Before')
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers :
    if value > 20:
        print('Large number', value)
print('After')
# Before
# Large number 41
# Large number 74
# After

# 특정 값 검색
found = False
print('Before', found)
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers :
    if value == 3 :
        found = True
        print(found, value)
        break # 특정 값을 찾았을때 해당 루프를 종료
print('After', found)
# Before False
# True 3
# After True

# 가장 작은 값
smallest = None
print('Before')
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)
# 9 9
# 9 41
# 9 12
# 3 3
# 3 74
# 3 15
# After 3

#실습문제
num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    if sval =='done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    # print(fval)
    num = num + 1
    tot = tot + fval

# print('All Done')
print(tot,num,tot/num)