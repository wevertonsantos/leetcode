s = "MCMXCIV"
def romanToInt(s: str) -> int:
    sum = 0
    next_roman = 0
    previous_roman = 0
    roman_int = {"I": 1, "V": 5, "X": 10,"L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(s)):
        if not s[i] == s[-1]:
            if roman_int[s[i]] < roman_int[s[i + 1]]:
                sum += roman_int[s[i + 1]] - roman_int[s[i]]
                next_roman = roman_int[s[i + 1]]
                previous_roman = roman_int[s[i - 1]]
            elif roman_int[s[i]] > roman_int[s[i + 1]]:
                sum += roman_int[s[i]]
        else:
            sum += roman_int[s[i]] - next_roman
            next_roman = 0
    print(sum)

romanToInt(s)