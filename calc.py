#Calculator with basic functions
num1 = float(input('Input first number: '))
num2 = float(input('Input second number: '))
oper = input('Input operation. (*, /, +, -): ')
while oper != '*' and oper != '/' and oper != '+' and oper != '-':
        oper = input('Please input valid operation. (* / + -)')
if oper == '*':
    ans = num1 * num2
elif oper == '/':
    if num2 != 0:
        ans = num1 / num2
    else:
        ans = "Cannot divide by zero."
elif oper == '+':
    ans = num1 + num2
else:
    ans = num1 - num2
print(num1, oper, num2,'=', ans)