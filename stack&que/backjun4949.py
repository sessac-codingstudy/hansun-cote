import sys

input = sys.stdin.readline


def check(sentence):
    stk = []
    for ch in sentence:
        if ch == ")":
            if stk and stk[-1] == "(":
                stk.pop()
            else:
                return False
        elif ch == "]":
            if stk and stk[-1] == "[":
                stk.pop()
            else:
                return False
        elif ch == "[" or ch == "(":
            stk.append(ch)
        else:
            continue
    return not stk


while True:
    sentence = input().rstrip()
    if sentence == ".":
        break
    if check(sentence):
        print("yes")
    else:
        print("no")
