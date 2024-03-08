def consecutiveString(S):
    stack=[]
    for char in S:
        if not stack or stack[-1]!=char:
            stack.append(char)
        elif len(stack)<2 or stack[-2]!=char:
            stack.append(char)
    return ''.join(stack)

print(consecutiveString(S))