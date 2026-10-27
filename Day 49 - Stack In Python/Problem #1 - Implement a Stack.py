def push_stack(stack , value):
    stack.append(value)
    return stack

stack=[]
stack=push_stack(stack , 20)
stack=push_stack(stack , 30)
stack=push_stack(stack , 40)
print(stack)


