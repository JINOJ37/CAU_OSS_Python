# %% Homework #2

# 사용자에게 연산방법을 문자열로 입력을 받은 후
# 정수 2개를 입력받아 연산을 수행하는 프로그램

def arithmetic_ops(op): # 연산 수행 함수
    num1 = int(input("input 1st number:"))
    num2 = int(input("input 2nd number:"))
    return num1, num2, op(num1, num2)

def add(a, b): # +함수
    return a+b
def sub(a, b): # -함수
    return a+b

while True:
    op = input("input operation:")
    if op == "end":
        break   # "반복을 종료"
    elif op == "+":
        num1, num2, ret = arithmetic_ops(add) # op가 +일 때
    elif op == "-":
        num1, num2, ret = arithmetic_ops(sub) # op가 -일 때
    elif op == "*":
        num1, num2, ret = arithmetic_ops(lambda x,y:x*y) # op가 *일 때
    elif op == "/":
        num1, num2, ret = arithmetic_ops(lambda x,y:x/y) # op가 /일 때
    elif op == "%":
        num1, num2, ret = arithmetic_ops(lambda x,y:x%y) # op가 %일 때
    else:
        print("Invalid operation")
        continue # Invalid operation이므로 연산결과를 출력하지 않고 "넘어간다".
    print(f"{num1}{op}{num2} = {ret}")  # 연산 결과 출력

print("Exit program")