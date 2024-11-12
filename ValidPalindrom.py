class ValidPalindrom:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a, b = 0 , 0
        for i in range(int(len(s)/2) + 1):
            while not s[i + a].isalpha():
                a += 1
            while not s[- (1 + i + b)].isalpha():
                b += 1
            print(f"{s[i + a]}, {s[- (1 + i + b)]}, index i: {i}, a: {a}, b: {b}")
            if i + a > len(s) - 1 - i - b:
                break
            if s[i + a] != s[- (1 + i + b)]:
                return False
        return True