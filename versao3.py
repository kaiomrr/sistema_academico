"""
Nome do Projeto: Simulador de Situação Acadêmica
Versão: 3.0
Data: 19/11/2026
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
# Regimento UNIFSA, seção Rendimentos: a Média de Aproveitamento é a média aritmética das notas.
# Autor: [Nome]
def calcular_media(notas):
    """Calcula a média aritmética das notas de aproveitamento."""
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


# [IA] Gerado com auxílio do GitHub Copilot
# Regimento UNIFSA, seção Rendimentos, item 1(b): aprovação por média exige média igual a 7,0.
# Regimento UNIFSA, seção Rendimentos, item 3(b): exame final exige média entre 4,0 e 7,0.
# Regimento UNIFSA, seção Rendimentos, item 5: frequência inferior a 75% causa reprovação.
# Autor: [Nome]
def verificar_situacao(aluno):
    """Determina a situação acadêmica, priorizando a reprovação por faltas."""
    media = calcular_media(aluno["notas"])
    limite_faltas = aluno["carga_horaria"] * 0.25

    if aluno["faltas"] > limite_faltas:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado por média"
    if media >= 4.0:
        return "Em exame final"
    return "Reprovado por nota"


# [IA] Gerado com auxílio do GitHub Copilot
# Regimento UNIFSA, seção Rendimentos, item 4: média final (MA + EF) / 2 deve ser 6,0.
# Autor: [Nome]
def calcular_nota_pf(media_parcial):
    """Calcula a nota mínima no exame final ou informa quando ela é impossível."""
    nota_necessaria = 12.0 - media_parcial
    if nota_necessaria > 10.0:
        return None
    return max(0.0, nota_necessaria)


# [IA] Gerado com auxílio do GitHub Copilot
# Regimento UNIFSA, seção Rendimentos, item 1(a): é necessária frequência mínima de 75%.
# Autor: [Nome]
def calcular_faltas_restantes(faltas, carga_horaria):
    """Calcula quantas faltas ainda podem ocorrer sem ultrapassar 25%."""
    limite_faltas = int(carga_horaria * 0.25)
    return max(0, limite_faltas - faltas)


# [IA] Gerado com auxílio do GitHub Copilot
# Autor: [Nome]
def carregar_turma_k37():
    """Retorna uma turma fictícia de dez alunos para testes da versão 2."""
    return [
        {"nome": "Ana Lima", "notas": [7.0, 7.0, 7.0], "faltas": 4, "carga_horaria": 60},
        {"nome": "Bruno Alves", "notas": [8.0, 8.0, 8.0], "faltas": 15, "carga_horaria": 60},
        {"nome": "Carla Souza", "notas": [7.0, 7.0, 7.0], "faltas": 15, "carga_horaria": 60},
        {"nome": "Diego Costa", "notas": [9.0, 8.5, 9.0], "faltas": 2, "carga_horaria": 60},
        {"nome": "Elisa Rocha", "notas": [6.0, 5.5, 6.0], "faltas": 3, "carga_horaria": 60},
        {"nome": "Felipe Nunes", "notas": [3.0, 3.5, 3.0], "faltas": 4, "carga_horaria": 60},
        {"nome": "Gabriela Reis", "notas": [8.0, 7.5, 8.0], "faltas": 16, "carga_horaria": 60},
        {"nome": "Henrique Melo", "notas": [5.0, 5.5, 5.0], "faltas": 2, "carga_horaria": 60},
        {"nome": "Isabela Dias", "notas": [2.0, 3.0, 3.5], "faltas": 1, "carga_horaria": 60},
        {"nome": "Joao Martins", "notas": [7.5, 8.0, 7.5], "faltas": 5, "carga_horaria": 60},
    ]


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
    """Gera um relatório inicial com a média das notas de cada aluno."""
    if not turma:
        print("Nenhum aluno cadastrado para gerar relatório.")
        return

    print("\n--- Relatório acadêmico ---")
    for aluno in turma:
        media = calcular_media(aluno["notas"])
        print(
            f"Aluno: {aluno['nome']} | Média: {media:.2f} | "
            f"Situação: {verificar_situacao(aluno)}"
        )


# [IA] Gerado com auxílio do GitHub Copilot
# Autor: [Nome]
def gerar_relatorio_turma(turma):
    """Exibe uma tabela completa e um resumo estatístico da turma."""
    if not turma:
        print("Nenhum aluno cadastrado para gerar relatório.")
        return

    cabecalho = (
        f"{'Nome':<18} {'Média':>6} {'Faltas/Limite':>15} "
        f"{'Situação':<22} {'Nota PF necessária':>19} {'Faltas restantes':>17}"
    )
    print("\n--- Relatório completo da turma ---")
    print(cabecalho)
    print("-" * len(cabecalho))

    contagem = {
        "Aprovado por média": 0,
        "Em exame final": 0,
        "Reprovado por falta": 0,
        "Reprovado por nota": 0,
    }
    soma_medias = 0.0
    maior_media = -1.0
    aluno_maior_media = None

    for aluno in turma:
        media = calcular_media(aluno["notas"])
        limite_faltas = int(aluno["carga_horaria"] * 0.25)
        situacao = verificar_situacao(aluno)
        nota_pf = calcular_nota_pf(media)
        faltas_restantes = calcular_faltas_restantes(
            aluno["faltas"], aluno["carga_horaria"]
        )

        if situacao == "Em exame final":
            nota_pf_texto = (
                f"{nota_pf:.2f}" if nota_pf is not None else "Impossível"
            )
        elif situacao == "Reprovado por nota":
            nota_pf_texto = "Impossível"
        else:
            nota_pf_texto = "-"

        print(
            f"{aluno['nome']:<18.18} {media:>6.2f} "
            f"{aluno['faltas']:>6}/{limite_faltas:<8} "
            f"{situacao:<22.22} {nota_pf_texto:>19} "
            f"{faltas_restantes:>17}"
        )

        contagem[situacao] += 1
        soma_medias += media
        if media > maior_media:
            maior_media = media
            aluno_maior_media = aluno

    media_geral = soma_medias / len(turma)
    print("\n--- Resumo da turma ---")
    for situacao, quantidade in contagem.items():
        print(f"{situacao}: {quantidade}")
    print(f"Média geral da turma: {media_geral:.2f}")
    print(
        f"Aluno com maior média: {aluno_maior_media['nome']} "
        f"({maior_media:.2f})"
    )


# [IA] Gerado com auxílio do GitHub Copilot
# Autor: [Nome]
def consultar_situacao(turma):
    """Exibe a situação acadêmica detalhada de um aluno escolhido."""
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
    faltas_restantes = calcular_faltas_restantes(
        aluno["faltas"], aluno["carga_horaria"]
    )
    print(f"\nAluno: {aluno['nome']}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {verificar_situacao(aluno)}")
    print(f"Faltas restantes: {faltas_restantes}")
    if nota_pf is None:
        print("Nota para exame final: impossível atingir 6,0.")
    elif media < 7.0:
        print(f"Nota mínima no exame final: {nota_pf:.2f}")


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
        print("4 - Carregar turma de teste K=37")
        print("5 - Consultar situação individual")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno(turma)
        elif opcao == "2":
            listar_turma(turma)
        elif opcao == "3":
            gerar_relatorio_turma(turma)
        elif opcao == "4":
            turma = carregar_turma_k37()
            print("Turma de teste carregada com 10 alunos.")
        elif opcao == "5":
            consultar_situacao(turma)
        elif opcao == "6":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Escolha uma opção de 1 a 6.")


# [IA] Gerado com auxílio do GitHub Copilot
turma = []


# [IA] Gerado com auxílio do GitHub Copilot
if __name__ == "__main__":
    exibir_menu()
