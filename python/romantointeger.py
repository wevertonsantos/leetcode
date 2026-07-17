s = "IV"
def romanToInt(s: str) -> int:
    sum = 0
    next_roman = 0
    roman_int = {"I": 1, "V": 5, "X": 10,"L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(s)):
        if i <= (len(s) - 2):
            if roman_int[s[i]] < roman_int[s[i + 1]]:
                sum += roman_int[s[i + 1]] - roman_int[s[i]]
                next_roman = roman_int[s[i + 1]]
            else:
                sum += roman_int[s[i]] - next_roman
                next_roman = 0
    print(sum)

romanToInt(s)

'''
faço o for na string
ai faço, se a letra atual I da string é menor que o proximo valor da string (assim pra demais letras)
ai faço, se for o último valor da string eu somo com len(s) - 2
'''