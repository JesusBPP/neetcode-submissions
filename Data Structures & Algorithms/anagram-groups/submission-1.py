class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        respuesta = defaultdict(list)
        for i in strs:
            respuesta["".join(sorted(i))].append(i)
        return list(respuesta.values())
                    