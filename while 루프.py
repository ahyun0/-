# while 루프
# 반복적으로 작업할 수 있음. 하지만 무한루프에 빠질 수 있으니 주의
n = 5

while n > 0:
    print(n)
    n = n - 1

print('Blastoff!')
print(n)

# break
# 루프 실행 종료
while True:
    line = input('> ') 
    if line == 'done':
        break
    print(line)
print('Done!')
# > hello there로 입력
# hello there로 출력됨
# > done로 입력
# Done!으로 출력됨

# continue
# 루프 종료 후 루프가 시작된 지점부터 다시 실행
while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')
# > hello there 입력
# hello there로 출력
# # don't print this '#'을 입력하게 되면 continue를 만나게 되고 continue는 loop의 시작점으로 다시 돌아가서 loop를 실행
# > done 입력
# Done!으로 출력 done을 입력하게 되면 break를 만나게 되고 break는 loop끝나는 점 바로 다음에 오는 코드를 실행

