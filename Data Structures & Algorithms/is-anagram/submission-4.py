class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagrama1 = {}
        anagrama2 = {}
        if len(s) != len(t):
            return False
        for caracter1, caracter2 in zip(s, t):
            if (anagrama1.get(caracter1, "000") == "000"):
                anagrama1[caracter1] = 1
            else:
                anagrama1[caracter1] += 1
            if (anagrama2.get(caracter2, "000") == "000"):
                anagrama2[caracter2] = 1
            else:
                anagrama2[caracter2] += 1
        if anagrama1.keys() == anagrama2.keys():
            for key in anagrama1:
                if anagrama1[key] != anagrama2[key]:
                    return False
            return True
        else: return False