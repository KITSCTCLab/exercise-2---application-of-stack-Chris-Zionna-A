postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
operators=["+","-","*","/","^"]
Opand=0
Optor=0
for token in tokens:
    if token in operators:
        Optor+=1
    else:
        Opand+=1
result=0.0
if Opand==(Optor+1):
    operands=[]
    for token in tokens:
        if token in operators:
            rightOp=operands.pop()
            leftOp=operands.pop()
            result=str(eval(leftOp+token+rightOp))
            operands.append(result)
        else:
            operands.append(token)
    print(int(operands.pop()))
else:
    print('Invalid postfix expression')
