from Sala import Sala

class SalaCirurgia(Sala):
    def __init__(self, numero, capacidade):
        super().__init__(numero, capacidade)
        self.equipamentos = []
    
    def adicionar_equipamento(self, equipamento):
        if isinstance(equipamento, str) and equipamento.strip():
            self.equipamentos.append(equipamento.strip())
            print(f"Equipamento '{equipamento}' adicionado à sala {self.numero}.")
        else:
            print("Nome de equipamento inválido!")

    def detalhar_sala(self):
        print(f"Sala Nº{self.numero} (Cirurgia)")
        print(f"Capacidade: {self.capacidade}")
        print("Equipamentos disponíveis:")
        if not self.equipamentos:
            print(" - Nenhum equipamento registado.")
        else:
            for i, eq in enumerate(self.equipamentos, start=1):
                print(f" {i}. {eq}")