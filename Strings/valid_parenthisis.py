def isValid(s):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in pairs:
            if not stack:
                return False
            if stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            return False

    return len(stack) == 0