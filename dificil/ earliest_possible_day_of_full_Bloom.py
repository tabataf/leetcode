# 2136 . Dia mais cedo possível de plena floração
# Você tem nsementes de flores. Cada semente deve ser plantada antes de começar a crescer e depois florescer. Plantar uma semente leva tempo, assim como o crescimento de uma semente. Você recebe dois arrays inteiros indexados por 0plantTime e growTime, de comprimento ncada:

# plantTime[i]é o número de dias completos que você leva para plantar a semente. Todos os dias, você pode trabalhar no plantio de exatamente uma semente. Você não precisa trabalhar para plantar a mesma semente em dias consecutivos, mas o plantio de uma semente não está completo até que você tenha trabalhado dias para plantá-la no total.ithplantTime[i]
# growTime[i]é o número de dias completos que a semente leva para crescer depois de totalmente plantada. Após o último dia de crescimento, a flor desabrocha e permanece desabrochada para sempre.ith
# Desde o início do dia 0, você pode plantar as sementes em qualquer ordem.

# Retorne o mais cedo possível quando todas as sementes estiverem florescendo .

import functools 

class Solution:
    def earliestFullBloom(plantTime: list[int], growTime: list[int]) -> int:
        def comparacao(a, b):
            flor1 = max(a[0] + b[0] + b[1], a[0] + a[1])
            flor2 = max(b[0] + a[0] + a[1], b[0] + b[1])

            return flor1 - flor2

        r=sorted(zip(plantTime, growTime), key=functools.cmp_to_key(comparacao))

        flor_mais_rapida= 0
        flor_atual = 0

        for p, g in r:
            flor_mais_rapida=max(flor_mais_rapida, flor_atual + p + g)
            flor_atual +=p
        return flor_mais_rapida

# teste
plantTime = [1,4,3]
growTime = [2,3,1]
print(Solution.earliestFullBloom(plantTime, growTime))