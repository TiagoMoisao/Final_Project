from Pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, idade, numero_utente):
        Pessoa.__init__(self,nome, idade)
        self.numero_utente=numero_utente
        self.historico_medico = []
        self.medico_atendentes = []
        
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
    def numero_utente(self):
        return self._numero_utente
    
    @numero_utente.setter
    def numero_utente(self, u):
        if u >= 0:
            self._numero_utente = u
        else:
            print("Numero de utente não pode ser negativo!")  


    def adicionar_registro(self, descricao):
        self.historico_medico.append(descricao)

    def adicionar_medico(self, medico):
        if medico not in self.medico_atendentes:
            self.medico_atendentes.append(medico)

    def mostrar_historico(self):
            print(f"Histórico médico de {self.nome}:")
            if not self.historico_medico:
                print("Nenhum registro encontrado.")
            else:
                for i, registro in enumerate(self.historico_medico, start=1):
                    print(f"{i}. {registro}")

            print("\nMédicos que atenderam:")
            if not self.medico_atendentes:
                print("Nenhum médico atendeu ainda.")
            else:
                for medico in self.medico_atendentes:
                    print(f"- {medico.nome} ({medico.especialidade})")
        
    def exibir_informacoes(self):
        print(f"O{self.nome}, tem {self.idade} anos e o seu número de utente é {self.numero_utente}.")

