"""
Nome do Projeto: Simulador de Situação Acadêmica
Grupo: [Nome do grupo]
Integrantes: [Nomes dos integrantes]
Matrículas: [Matrículas dos integrantes]
Valor de K: 37
"""


# [IA] Gerado com auxílio do GitHub Copilot
# Autor: [Nome]
def ler_float(mensagem, minimo, maximo):
    """Lê um número decimal e repete a leitura enquanto ele for inválido."""
    while True:
        try:
            valor = float(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            print(f"Digite um valor entre {minimo:.1f} e {maximo:.1f}.")
        except ValueError:
            print("Entrada inválida. Digite um número decimal.")


# [IA] Gerado com auxílio do GitHub Copilot
# Autor: [Nome]
def ler_int(mensagem, minimo):
    """Lê um número inteiro e impede valores menores que o mínimo informado."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo:
                return valor
            print(f"Digite um valor maior ou igual a {minimo}.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


# [IA] Gerado com auxílio do GitHub Copilot
# Autor: [Nome]
def cadastrar_aluno(turma):
    """Coleta os dados de um aluno e adiciona seu cadastro à turma."""
    nome = input("Nome do aluno: ").strip()
    quantidade_notas = ler_int("Quantidade de notas: ", 1)

    notas = []
    for indice in range(quantidade_notas):
        nota = ler_float(f"Nota {indice + 1} (0.0 a 10.0): ", 0.0, 10.0)
        notas.append(nota)

    faltas = ler_int("Quantidade de faltas: ", 0)
    carga_horaria = ler_int("Carga horária (em horas): ", 0)

    aluno = {
        "nome": nome,
        "notas": notas,
        "faltas": faltas,
        "carga_horaria": carga_horaria,
    }
    turma.append(aluno)
    print("Aluno cadastrado com sucesso.")


# [IA] Gerado com auxílio do GitHub Copilot
# Regimento UNIFSA, seção Rendimentos: a média é a média aritmética das notas.
def calcular_media(notas):
    """Calcula a média aritmética das notas do aluno."""
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


# [IA] Gerado com auxílio do GitHub Copilot
# Regimento UNIFSA, seção Rendimentos, itens 1, 3 e 5: aplica frequência e notas.
def verificar_situacao(aluno):
    """Informa a situação acadêmica, priorizando a reprovação por falta."""
    media = calcular_media(aluno["notas"])
    limite_faltas = aluno["carga_horaria"] * 0.25

    if aluno["faltas"] > limite_faltas:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    if media >= 4.0:
        return "Prova final"
    return "Reprovado por nota"


# [IA] Gerado com auxílio do GitHub Copilot
# Regimento UNIFSA, seção Rendimentos, item 4: (média + PF) / 2 deve ser 6,0.
def calcular_nota_pf(media_parcial):
    """Calcula a nota mínima necessária na prova final."""
    nota_necessaria = 12.0 - media_parcial
    if nota_necessaria > 10.0:
        return None
    return max(0.0, nota_necessaria)


# [IA] Gerado com auxílio do GitHub Copilot
# Regimento UNIFSA, seção Rendimentos, item 1(a): frequência mínima de 75%.
def calcular_faltas_restantes(faltas, carga_horaria):
    """Calcula quantas faltas ainda podem ocorrer sem ultrapassar 25%."""
    limite_faltas = int(carga_horaria * 0.25)
    return max(0, limite_faltas - faltas)


# [IA] Gerado com auxílio do GitHub Copilot
# Autor: [Nome]
def listar_turma(turma):
    """Exibe no terminal os dados básicos de todos os alunos cadastrados."""
    if not turma:
        print("Nenhum aluno cadastrado.")
        return

    print("\n--- Turma ---")
    for indice, aluno in enumerate(turma, start=1):
        notas = ", ".join(f"{nota:.1f}" for nota in aluno["notas"])
        print(
            f"{indice}. {aluno['nome']} | Notas: {notas} | "
            f"Faltas: {aluno['faltas']} | Carga horária: {aluno['carga_horaria']}h"
        )


# [IA] Gerado com auxílio do GitHub Copilot
# Autor: [Nome]
def gerar_relatorio(turma):
    """Gera o relatório da turma com situações e resumo geral."""
    if not turma:
        print("Nenhum aluno cadastrado para gerar relatório.")
        return

    cabecalho = (
        f"{'Nome':<18} {'Média':>6} {'Faltas/Limite':>15} "
        f"{'Situação':<20} {'Nota PF':>10} {'Faltas rest.':>13}"
    )
    print("\n--- Relatório acadêmico ---")
    print(cabecalho)
    print("-" * len(cabecalho))

    contagem = {
        "Aprovado": 0,
        "Prova final": 0,
        "Reprovado por nota": 0,
        "Reprovado por falta": 0,
    }
    soma_medias = 0.0
    maior_media = -1.0
    aluno_maior_media = None

    for aluno in turma:
        media = calcular_media(aluno["notas"])
        limite_faltas = int(aluno["carga_horaria"] * 0.25)
        situacao = verificar_situacao(aluno)
        nota_pf = calcular_nota_pf(media)
        nota_pf_texto = (
            f"{nota_pf:.2f}" if situacao == "Prova final" and nota_pf is not None
            else "Impossível" if situacao == "Reprovado por nota"
            else "-"
        )
        faltas_restantes = calcular_faltas_restantes(
            aluno["faltas"], aluno["carga_horaria"]
        )
        print(
            f"{aluno['nome']:<18.18} {media:>6.2f} "
            f"{aluno['faltas']:>6}/{limite_faltas:<8} "
            f"{situacao:<20.20} {nota_pf_texto:>10} "
            f"{faltas_restantes:>13}"
        )

        contagem[situacao] += 1
        soma_medias += media
        if media > maior_media:
            maior_media = media
            aluno_maior_media = aluno

    print("\n--- Resumo da turma ---")
    for situacao, quantidade in contagem.items():
        print(f"{situacao}: {quantidade}")
    print(f"Média geral: {soma_medias / len(turma):.2f}")
    print(
        f"Maior média: {aluno_maior_media['nome']} "
        f"({maior_media:.2f})"
    )


# [IA] Gerado com auxílio do GitHub Copilot
def consultar_situacao(turma):
    """Exibe os cálculos acadêmicos de um aluno selecionado."""
    if not turma:
        print("Nenhum aluno cadastrado.")
        return

    listar_turma(turma)
    indice = ler_int("Número do aluno: ", 1)
    if indice > len(turma):
        print("Número de aluno inválido.")
        return

    aluno = turma[indice - 1]
    media = calcular_media(aluno["notas"])
    nota_pf = calcular_nota_pf(media)
    print(f"\nAluno: {aluno['nome']}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {verificar_situacao(aluno)}")
    if nota_pf is None:
        print("Nota mínima na prova final: impossível atingir 6,0.")
    elif media < 7.0:
        print(f"Nota mínima na prova final: {nota_pf:.2f}")
    faltas_restantes = calcular_faltas_restantes(
        aluno["faltas"], aluno["carga_horaria"]
    )
    print(
        f"Faltas restantes: {faltas_restantes}"
    )


# [IA] Gerado com auxílio do GitHub Copilot
# Autor: [Nome]
def exibir_menu():
    """Executa o menu principal do simulador até que o usuário escolha sair."""
    global turma

    while True:
        print("\n=== Simulador de Situação Acadêmica ===")
        print("1 - Cadastrar aluno")
        print("2 - Listar turma")
        print("3 - Gerar relatório")
        print("4 - Consultar situação individual")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno(turma)
        elif opcao == "2":
            listar_turma(turma)
        elif opcao == "3":
            gerar_relatorio(turma)
        elif opcao == "4":
            consultar_situacao(turma)
        elif opcao == "5":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Escolha uma opção de 1 a 5.")


# [IA] Gerado com auxílio do GitHub Copilot
turma = []


# [IA] Gerado com auxílio do GitHub Copilot
if __name__ == "__main__":
    exibir_menu()
