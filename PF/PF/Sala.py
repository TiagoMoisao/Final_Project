from abc import ABC, abstractmethod

class Sala(ABC):
    def __init__(self, numero, capacidade):
        self.numero=numero
        self.capacidade=capacidade

    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, num):
        if num > 0:
            self._numero = num
        else:
            print("O número da sala deve ser positivo!")
        
    @property
    def capacidade(self):
        return self._capacidade
    
    @capacidade.setter
    def capacidade(self, cap):
        if cap > 0:
            self._capacidade = cap
        else:
            print("A capacidade deve ser maior que zero!")
    
    @abstractmethod
    def detalhar_sala(self):
        pass