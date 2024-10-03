# 다중 분기(Multi-way decisions)
# 필요에 의해 elif 예약어를 통해 조건문 추가
x = 21

if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
elif x < 20 :
    print('Big')
elif x < 40 :
    print('Large')
elif x < 100 :
    print('Huge')
else :
    print('Ginormous') # Large가 출력

# try/except
# 발생할 수 있는 에러에 대해 대처가 가능하도록 해줌
astr = "123"

try:
    print("Hello")
    isInt = int(astr)
    print("World")
except: # try 부분에서 에러가 발생하면 except 부분을 실행, 에러가 발생하지 않으면 실행하지 않음
    isInt = "Integer로 변환할 수 없습니다."

print('Done', isInt)

#실습문제
sh = input("근무시간: ")
sr = input("시급: ")
# 예외처리-try에서 실행할 수 없는 값이 나왔을 때 execpt로 넘어감
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("숫자로 입력해주세요.")
    # 끝내고 싶을 때 사용
    quit()

# print(fh, fr)
if fh > 40 :
    reg = fr * fh
    otp =(fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("총 급여:",xp)