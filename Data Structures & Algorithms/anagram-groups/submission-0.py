class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        respuesta = []
        for i in strs:
            agregado = False
            if respuesta == []:
                respuesta.append([i])
            else:
                for sublista in respuesta:
                    for j in sublista:
                        if "".join(sorted(i)) == "".join(sorted(j)):
                            sublista.append(i)
                            agregado = True
                            break
                    if agregado:
                        break
                if agregado == False:
                        respuesta.append([i])
        return respuesta
                    