# Você recebe cordas jewelsrepresentando os tipos de pedras que são joias e stonesrepresentando as pedras que você possui. Cada personagem stonesé um tipo de pedra que você possui. Você quer saber quantas das pedras que você tem também são joias.
# As letras diferenciam maiúsculas de minúsculas, por isso "a"é considerado um tipo de pedra diferente de "A".

class Solution:
    def numJewelsInStones(joia: str, pedra: str) -> int:
        colecao = 0
        for x in joia:
            for y in pedra:
                if x == y:
                    colecao += 1
            return colecao

#teste
P="A"
J="aAAbbbb"
print(Solution.numJewelsInStones(P, J))
