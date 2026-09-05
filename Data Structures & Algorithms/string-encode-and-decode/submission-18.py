from collections import defaultdict
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        self.dictionary = defaultdict()
        for i, value in enumerate(strs):
            self.dictionary[i] = value

        encoded = ' '.join(self.dictionary[i] for i in self.dictionary)

        return encoded
            
            
    def decode(self, s: str) -> List[str]:
        decoded = []
        for x in self.dictionary:
            decoded.append(self.dictionary[x])
        return decoded