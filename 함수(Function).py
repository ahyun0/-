# 함수(Function)
# 반족적으로 호출해야 하는 코드를 하나의 블럭으로 만들어 재사용률을 높이는 것
def greeting():
    print("Hello World")

greeting() # Hellw World 출력

# 매개변수(Parameters)'
def greeting(lang):
    print(lang)

greeting("Hello World") # Hello World가 출력

# 변환값(Return Value)
def greet():
    return "Hello"

print(greet(), "Connect") # Hello Connect로 출력
print(greet(), "Python") # Hello Python으로 출력

# Multiple 매개변수/인자
def add(left, right):
    return left + right

print(add(1,2)) # 3으로 출력

#실습문제
# def 함수 만들기: 기억장치로 실행되지 않으며 아래에서 입력해줘야 도출 - def 변수명()
def computepay(hours, rate) :
    # print("In computepay", hours, rate)
    if hours > 40 :
        reg = rate * hours
        otp =(hours - 40.0) * (rate * 0.5)
        pay = hours + rate
    else:
        pay = hours * rate
    # print("Rrturning", pay)
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr)

print("Pay:",xp)