# 1603- Projetar um sistema de estacionamento para um estacionamento. O estacionamento possui três tipos de vagas: grande, média e pequena, com um número fixo de vagas para cada tamanho.

# Implemente a ParkingSystemclasse:

# ParkingSystem(int big, int medium, int small)Inicializa o objeto da ParkingSystemclasse. O número de vagas para cada vaga de estacionamento é fornecido pelo construtor.
# bool addCar(int carType)Verifica se existe vaga de estacionamento carTypepara o carro que deseja entrar no estacionamento. carTypepodem ser de três tipos: grande, médio ou pequeno, que são representados por 1, 2e 3respectivamente. Um carro só pode estacionar em uma vaga própriacarType . Se não houver espaço disponível, retorne false, caso contrário, estacione o carro naquele espaço de tamanho e retorne true.


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.lot = {}  
        self.lot[1] = big
        self.lot[2] = medium
        self.lot[3] = small
        
    def addCar(self, carType: int) -> bool:
        if self.lot.get(carType) > 0: 
            self.lot[carType] -= 1
            return True
        else:
            return False