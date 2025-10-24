from Sala import Sala
from Medico import Medico
from Paciente import Paciente

class SalaConsulta(Sala):
    def __init__(self, numero, capacidade,medico_responsavel):
        super().__init__(numero, capacidade)
        self.medico_responsavel = medico_responsavel
        self.consultas = []
    
    @property
    def medico_responsavel(self):
        return self._medico_responsavel

    @medico_responsavel.setter
    def medico_responsavel(self, medico):
        if medico is None:
            self._medico_responsavel = None
        elif isinstance(medico, Medico):
            self._medico_responsavel = medico
        else:
            print("O responsável tem de ser um médico válido.")

    def agendar_consulta(self, paciente):
        if not isinstance(paciente, Paciente):
            print("Apenas instâncias de Paciente podem ser agendadas.")
            return
        if len(self.consultas) < self.capacidade:
            self.consultas.append(paciente)
            print(f"Consulta marcada para {paciente.nome} na sala {self.numero}.")
        else:
            print("A sala atingiu a capacidade máxima de consultas!")

    def detalhar_sala(self):
        print(f"Sala Nº{self.numero} (Consulta)")
        print(f"Capacidade: {self.capacidade}")
        print(f"Médico responsável: {self.medico_responsavel.nome}")
        print("Pacientes agendados:")
        if not self.consultas:
            print(" - Nenhum paciente agendado.")
        else:
            for i, p in enumerate(self.consultas, start=1):
                print(f" {i}. {p.nome} ({p.numero_utente})")




    
    