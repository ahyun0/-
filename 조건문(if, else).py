# if 문
x = 5
if x < 10 : # if는 예약어로, if 다음에 나오는 조건문의 True, False 판단
    print('smaller') # 만약 True인 경우 smaller 출력

y = 11
if y < 10 :
    print('smaller')
else : # 첫 번째 if 문의 조건이 거짓인 경우 else문 이하의 코드가 실행
    print('bigger') # 첫 번째 if 문이 거짓이기 때문에 smaller는 출력되지 않고 bigger만 출력

# 실습문제
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
# print(fh, fr)
if fh > 40 :
    # print("Overtime")
    reg = fr * fh
    otp =(fh - 40.0) * (fr * 0.5)
    # print(reg,otp)
    xp = reg + otp
else:
    # print("Regular")
    xp = fh * fr
print("Pay:",xp)