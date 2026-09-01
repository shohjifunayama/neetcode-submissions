class Solution:

    def encode(self, strs: List[str]) -> str:
        strings = []
        for term in strs:
            N = len(term)
            strings.append("#" + f"{N:03}" + term)

        return "".join(strings)
        
    def decode(self, s: str) -> List[str]:
        decoded = []
        while len(s) > 0:
            N = int(s[1:4])
            term = s[4:N+4]
            s = s[N+4:] if len(s) >= N+4 else ""
            decoded.append(term)
        return decoded