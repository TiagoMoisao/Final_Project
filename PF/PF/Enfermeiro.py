from Funcionario import Funcionario

class Enfermeiro(Funcionario):
    def __init__(self, nome, idade, salario, turno):
        Funcionario.__init__(self, nome, idade,"Enfermeiro", salario)
        self.turno=turno
        self.pacientes = []
    
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
    def turno(self):
        return self._turno
    
    @turno.setter
    def turno(self, t):
        if not t:  # vazio
            print("Aviso: turno não especificado. Definido como 'indefinido'.")
            self._turno = "indefinido"
        else:
            t = t.strip().lower()

        if t in ["dia", "noite"]:
            self._turno = t
        else:
            print("Turno inválido. Use 'dia' ou 'noite'. Definido como 'indefinido'.")
            self._turno = "indefinido"

    def adicionar_paciente(self, paciente):
        if paciente not in self.pacientes:
            self.pacientes.append(paciente)

    def listar_pacientes(self):
        print(f"\nPacientes sob os cuidados do enfermeiro {self.nome}:")
        if not self.pacientes:
            print("Nenhum paciente.")
        else:
            for i, paciente in enumerate(self.pacientes, start=1):
                print(f"{i}. {paciente.nome} ({paciente.numero_utente})")

    def calcular_pagamento(self):
        adicional = 0.20 if self._turno == "noite" else 0.0
        pagamento_total = self.salario + (self.salario * adicional)
        return pagamento_total
        
    def exibir_informacoes(self):
        print(f"O enfermeiro {self.nome} trabalha no turno da {self.turno} e tem {len(self.pacientes)} paciente(s) sob sua responsabilidade.")