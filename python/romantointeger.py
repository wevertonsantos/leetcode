s = "III"
def romanToInt(s: str) -> int:
    sum = 0
    for i in range(len(s)):
        if s[i] == "I":
            if s[i + 1] == "V":
                sum += 4
            elif s[i + 1] == "X":
                sum += 9
            else:
                sum += 1
        elif s[i] == "V":
            if not s[i - 1] == "I":
                sum += 5
        elif s[i] == "X":
            if s[i + 1] == "L":
                sum += 40
            elif s[i + 1] == "C":
                sum += 90
            else:
                sum += 10
        elif s[i] == "L":
            if not s[i - 1] == "X":
                sum += 50
        elif s[i] == "C":
            if s[i + 1] == "D":
                sum += 400
            elif s[i + 1] == "M":
                sum += 900
            elif not s[i - 1] == "X":
                sum += 100
        elif s[i] == "D":
            if not s[i - 1] == "C":
                sum += 500
        elif s[i] == "M":
            if not s[i - 1] == "C":
                sum += 1000
    return sum

print(romanToInt(s))