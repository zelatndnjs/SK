def calculator(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b
    else:
        print("잘못된 수식 입력!")

a,b,op = input().split()
a,b = int(a),int(b)
print(calculator(a,b,op))