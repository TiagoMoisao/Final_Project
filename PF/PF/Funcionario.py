from Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)
        self.cargo= cargo
        self.salario= salario


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
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, s):
        if s >= 0:
            self._salario = s
        else:
            print("O salário não pode ser negativo!")
        
    def exibir_informacoes(self):
        print(f"O {self.nome} tem {self.idade} anos, é {self.cargo} e o seu salário é {self.salario}")

    def aplicar_aumento(self, percentual):
        self.salario=self.salario*(percentual/100)
        return self.salario
