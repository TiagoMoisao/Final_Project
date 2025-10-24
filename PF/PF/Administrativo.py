from Funcionario import Funcionario

class Administrativo(Funcionario):
    def __init__(self, nome, idade, salario, setor, horas):
        Funcionario.__init__(self, nome, idade,"Administrativo", salario)
        self.setor=setor
        self.horas= horas
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, n):
        if n == "":
            print("Nome não pode ser vazio!")
        else:
            self._nome = n

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, i):
        if i >= 0:
            self._idade = i
        else:
            print("Idade não pode ser negativa!")

    @property
    def setor(self):
        return self._setor
    
    @setor.setter
    def setor(self, valor):
        if valor.strip():
            self._setor = valor
        else:
            raise ValueError("Setor inválido.")


    def registar_horas(self, horas):
        if horas > 0:
            self.horas += horas
            print(f"{horas} hora(s) registrada(s) para {self.nome}. Total: {self.horas}.")
        else:
            print("As horas trabalhadas devem ser um valor positivo!")
    
    def calcular_pagamentos(self):
        return self.salario + (self.horas * 10)

    def exibir_informacoes(self):
        print(f"O funcionário {self.nome}, do setor {self.setor}, trabalhou {self.horas} hora(s). Salário total: {self.calcular_pagamentos():.2f}€")



    
        


    

        


