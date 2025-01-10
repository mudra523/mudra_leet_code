class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        setR = {}
        setM = {}
        for c in ransomNote:
            if c in setR:
                setR[c] += 1
            else:
                setR[c] = 1
        for c in magazine:
            if c in setM:
                setM[c] += 1
            else:
                setM[c] = 1
        for c in setR:
            if setR[c] > setM.get(c, 0):
                return False
        return True

        