from collections import defaultdict
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for i, value in enumerate(strs):
            strs[i] = f"{len(value)}"+ '#' + value

        return ''.join(strs)
            
            
    def decode(self, s: str) -> List[str]:
        decoded = []
        number = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                number.append(s[i])
                i+=1
            elif s[i] == '#':
                i+=1
                number = int(''.join(number))
                word = ''
                for y in range(number):
                    word += s[y+i]
                i+=len(word)
                decoded.append(word)
                number = []
        return decoded
            