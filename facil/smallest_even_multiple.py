# 2413 - Dado um inteiro positivon , retorne o menor inteiro positivo que seja múltiplo de ambos 2 e n .

# link do submit: https://leetcode.com/problems/smallest-even-multiple/submissions/888772250/
class Solution:
    def smallestEvenMultiple( n: int) -> int:
# range(de onde começa, onde termina)
        final = n * 2 + 1
        for numero in range (1, final):
            if numero % 2 == 0 and numero % n == 0:
                return numero
        
        return -1

# teste
n= 5
print(Solution.smallestEvenMultiple(n))