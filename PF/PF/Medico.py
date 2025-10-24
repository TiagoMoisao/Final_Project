from Funcionario import Funcionario


class Medico(Funcionario):
    def __init__(self, nome, idade, cargo, salario, especialidade):
        super().__init__(nome, idade, cargo, salario)
        self.especialidade = especialidade
        self.pacientes_atendidos = [] 

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
    def especialidade(self):
        return self._especialidade
    
    @especialidade.setter
    def especialidade(self, e):
        if e == "":
            print("Especialidade não pode ser vazio!")
        else:
            self._especialidade = e

    def adicionar_paciente(self, paciente):
        if paciente not in self.pacientes_atendidos:
            self.pacientes_atendidos.append(paciente)
            paciente.adicionar_medico(self)

    def listar_pacientes(self):
        print(f"Pacientes atendidos pelo Dr(a). {self.nome}:")
        if not self.pacientes_atendidos:
            print("Nenhum paciente atendido ainda.")
        else:
            for p in self.pacientes_atendidos:
                print(f"- {p.nome} ({p.numero_utente})")
    
    def calcular_pagamento(self, valor_por_paciente: float = 50.0) -> float:
        pacientes = getattr(self, "pacientes", [])
        num_pacientes = len(pacientes)
        salario_base = getattr(self, "salario", 0.0)
        adicional = valor_por_paciente * num_pacientes
        total = salario_base + adicional
        return total
    
    def exibir_informacoes(self):
        print(f"Dr(a). {self.nome}, {self.idade} anos, especialidade: {self.especialidade}")
    