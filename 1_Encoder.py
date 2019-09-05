    def duplicate_encode(word):
        ans = ""
        word = word.lower()
        for char in word:
            temp = word.count(char)
            if temp == 1:
                ans = ans + "("
            elif temp >= 1:
                ans = ans + ")"
        return ans