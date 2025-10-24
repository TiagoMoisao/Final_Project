from Paciente import Paciente
from Medico import Medico
from Enfermeiro import Enfermeiro
from Administrativo import Administrativo
from EnfermeiroChefe import EnfermeiroChefe
from SalaConsulta import SalaConsulta
from SalaCirurgia import SalaCirurgia

pacientes = []
medicos = []
enfermeiros = []
administrativos = []
chefes = []
salas_consulta = []
salas_cirurgia = []


def criar_paciente():
    nome = input("Nome do paciente: ").strip()
    idade = int(input("Idade: "))
    numero = int(input("Número de utente: "))
    p = Paciente(nome, idade, numero)
    pacientes.append(p)
    print(f"Paciente {nome} criado com sucesso!")


def criar_medico():
    nome = input("Nome do médico: ").strip()
    idade = int(input("Idade: "))
    cargo = input("Cargo: ").strip()
    salario = float(input("Salário base: "))
    especialidade = input("Especialidade: ").strip()
    m = Medico(nome, idade, cargo, salario, especialidade)
    medicos.append(m)
    print(f"Médico {nome} ({especialidade}) criado com sucesso!")


def criar_enfermeiro():
    nome = input("Nome do enfermeiro: ").strip()
    idade = int(input("Idade: "))
    salario = float(input("Salário base: "))
    turno = input("Turno (dia/noite): ").strip().lower()
    while turno not in ["dia", "noite"]:
        print("Turno inválido. Por favor, escreva 'dia' ou 'noite'.")
        turno = input("Turno (dia/noite): ").strip().lower()
    e = Enfermeiro(nome, idade, salario, turno)
    enfermeiros.append(e)
    print(f"Enfermeiro {nome} criado com sucesso!")


def criar_administrativo():
    nome = input("Nome do administrativo: ").strip()
    idade = int(input("Idade: "))
    salario = float(input("Salário base: "))
    setor = input("Setor: ").strip()
    horas = int(input("Número de horas semanais: "))
    a = Administrativo(nome, idade, salario, setor, horas)
    administrativos.append(a)
    print(f"Administrativo {nome} criado com sucesso!")


def criar_enfermeiro_chefe():
    nome = input("Nome do enfermeiro-chefe: ").strip()
    idade = int(input("Idade: "))
    salario = float(input("Salário base: "))
    turno = input("Turno (dia/noite): ").strip().lower()
    setor = input("Setor: ").strip()
    bonus = float(input("Bônus de chefia: "))
    horas = int(input("Número de horas semanais: "))
    ec = EnfermeiroChefe(nome, idade, salario, turno, setor, bonus, horas)
    chefes.append(ec)
    print(f"Enfermeiro Chefe {nome} criado com sucesso!")


def criar_sala_consulta():
    numero = int(input("Número da sala: "))
    capacidade = int(input("Capacidade: "))

    if not medicos:
        print("Nenhum médico disponível. Crie um primeiro.")
        return

    print("Selecione o médico responsável:")
    for i, m in enumerate(medicos, start=1):
        print(f"{i}. {m.nome} ({m.especialidade})")

    try:
        idx = int(input("Escolha: ")) - 1
        if idx < 0 or idx >= len(medicos):
            print("Escolha inválida. Nenhuma sala criada.")
            return
        medico_responsavel = medicos[idx]
        sc = SalaConsulta(numero, capacidade, medico_responsavel)
        salas_consulta.append(sc)
        print(f"Sala de consulta {numero} criada com o Dr(a). {medico_responsavel.nome} como responsável.")
    except ValueError:
        print("Entrada inválida. A sala não foi criada.")


def criar_sala_cirurgia():
    numero = int(input("Número da sala: "))
    capacidade = int(input("Capacidade: "))
    s = SalaCirurgia(numero, capacidade)
    salas_cirurgia.append(s)
    print(f"Sala de cirurgia {numero} criada!")


# ------------------------- Funções de interação -------------------------
def agendar_consulta():
    if not pacientes or not salas_consulta:
        print("Crie pelo menos um paciente e uma sala de consulta antes.")
        return

    print("Selecione a sala:")
    for i, s in enumerate(salas_consulta, start=1):
        print(f"{i}. Sala {s.numero} ({s.medico_responsavel.nome})")
    try:
        sala = salas_consulta[int(input("Escolha: ")) - 1]
    except (ValueError, IndexError):
        print("Escolha inválida.")
        return

    print("Selecione o paciente:")
    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. {p.nome}")
    try:
        paciente = pacientes[int(input("Escolha: ")) - 1]
        sala.agendar_consulta(paciente)
    except (ValueError, IndexError):
        print("Escolha inválida.")


def adicionar_equipamento():
    if not salas_cirurgia:
        print("Nenhuma sala de cirurgia disponível.")
        return
    print("Selecione a sala:")
    for i, s in enumerate(salas_cirurgia, start=1):
        print(f"{i}. Sala {s.numero}")
    try:
        sala = salas_cirurgia[int(input("Escolha: ")) - 1]
        eq = input("Nome do equipamento: ").strip()
        sala.adicionar_equipamento(eq)
    except (ValueError, IndexError):
        print("Escolha inválida.")


def listar_todos():
    print("\nMédicos: ")
    for m in medicos:
        m.exibir_informacoes()
    print("\nEnfermeiros: ")
    for e in enfermeiros:
        e.exibir_informacoes()
    print("\nAdministrativos: ")
    for a in administrativos:
        a.exibir_informacoes()
    print("\nEnfermeiros Chefes: ")
    for c in chefes:
        c.exibir_informacoes()
    print("\nPacientes: ")
    for p in pacientes:
        p.exibir_informacoes()
    print("\nSalas de Consulta: ")
    for s in salas_consulta:
        s.detalhar_sala()
    print("\nSalas de Cirurgia: ")
    for s in salas_cirurgia:
        s.detalhar_sala()
    print()


def menu():
    while True:
        print("""HOSPITAL MANAGEMENT SYSTEM
                1. Criar Paciente
                2. Criar Médico
                3. Criar Enfermeiro
                4. Criar Administrativo
                5. Criar Enfermeiro Chefe
                6. Criar Sala de Consulta
                7. Criar Sala de Cirurgia
                8. Agendar Consulta
                9. Adicionar Equipamento a Sala Cirurgia
                10. Listar Todos os Registos
                0. Sair
                """)
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            criar_paciente()
        elif opcao == "2":
            criar_medico()
        elif opcao == "3":
            criar_enfermeiro()
        elif opcao == "4":
            criar_administrativo()
        elif opcao == "5":
            criar_enfermeiro_chefe()
        elif opcao == "6":
            criar_sala_consulta()
        elif opcao == "7":
            criar_sala_cirurgia()
        elif opcao == "8":
            agendar_consulta()
        elif opcao == "9":
            adicionar_equipamento()
        elif opcao == "10":
            listar_todos()
        elif opcao == "0":
            print("Programa encerrado. Até breve!")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu()
