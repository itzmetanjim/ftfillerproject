print("implementation of the shunting yard algorithm:")
stack1=[] #operand stack
stack2=[] #operator stack
operators=["+","-","*","/","(","^",")"]
green="\033[92m"
blue="\033[94m"
reset="\033[0m"
input1=input(green+"enter the expression you want to evaluate: "+blue)
input1=input1.replace(" ","")
import re

def to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []
    tokens = re.findall(r'\d+|[+*/()-]', expression)

    for token in tokens:
        if token.isdigit():
            output.append(int(token))
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(token, 0)):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())
    return output
def evaluate(postfix):
    stack = []
    for token in postfix:
        if isinstance(token, int):
            stack.append(token)
        else:
            b, a = stack.pop(), stack.pop()
            ops = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}
            stack.append(ops[token])
    return stack[0]
pf =to_postfix(input1)
result = evaluate(pf)
print(reset+"result: ",result)
