from sys import stdin

brackets = {"(": ")", "[": "]"}

while True:
    stack = []
    check = True
    string = stdin.readline()
    if string == ".":
        break

    for char in string:
        if char in brackets.keys():
            stack.append(char)

        elif char in brackets.values():
            if stack:
                if char == brackets[stack.pop()]:
                    continue

            check = False
            break

    if check and not stack:
        print("yes")
    else:
        print("no")
