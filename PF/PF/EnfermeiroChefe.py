from Enfermeiro import Enfermeiro
from Administrativo import Administrativo

class EnfermeiroChefe(Enfermeiro, Administrativo):
    def __init__(self, nome, idade, salario, turno, setor, bonus_chefia, horas):
        Enfermeiro.__init__(self, nome, idade, salario, turno)
        Administrativo.__init__(self, nome, idade, salario, setor, horas)
        self._bonus_chefia = bonus_chefia

    @property
    def bonus_chefia(self):
        return self._bonus_chefia
    
    @bonus_chefia.setter
    def bonus_chefia(self, valor):
        if valor > 0:
            self._bonus_chefia = valor
        else:
            print("O bônus tem de ser positivo!")

    def calcular_pagamento(self):
        pagamento_enfermeiro = Enfermeiro.calcular_pagamento(self)
        pagamento_administrativo = Administrativo.calcular_pagamentos(self)
        total = (pagamento_enfermeiro + pagamento_administrativo) / 2 + self.bonus_chefia
        return total
    
    def exibir_informacoes(self):
        print(f"Enfermeiro Chefe {self.nome}, {self.idade} anos:")
        print(f" - Turno: {self.turno}")
        print(f" - Setor: {self.setor}")
        print(f" - Bônus de chefia: {self.bonus_chefia}€")
        print(f" - Total de pacientes sob cuidado: {len(self.pacientes)}")