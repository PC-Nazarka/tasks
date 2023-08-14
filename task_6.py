def check(string: str):
    stack = []
    parentheses = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    for s in string:
        if s in parentheses:
            stack.append(s)
        else:
            last = stack.pop() if stack else ""
            if parentheses.get(last, "") != s:
                return False
    return not stack

print(check("[][](){}"))
print(check("[][]({}"))
