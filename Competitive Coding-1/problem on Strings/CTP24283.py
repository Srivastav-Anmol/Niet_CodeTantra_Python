def isSuper(s):
    char=[""]
    for i in range(97,123):
        char.append(chr(i))
    for i in s:
        if s.count(i)!=char.index(i):
            return False
    return True
print("true" if isSuper(s) else "false")