from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    @abstractmethod
    def ligar(self):
        pass