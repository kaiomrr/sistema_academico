"""Projeto 07 - Simulador de Situação Acadêmica - UNIFSA.

Fonte das regras: UNIFSA, Procedimentos Acadêmicos, seção "Rendimentos",
itens 1 a 5. Disponível em:
https://unifsa.com.br/site/servico/procedimentos-academicos/

A página consultada não possui paginação; por isso, os comentários citam a
seção e o item do regulamento, em vez de um número de página.

Os dados da turma fictícia são simulados e não representam alunos reais.
"""

import math

# Registro da revisão da IA: a versão anterior deixava as regras como None e
# não garantia a quantidade de fronteiras definida por K. Percebemos o erro
# porque o relatório mostrava "REGRAS PENDENTES" e a contagem não coincidia
# com (K % 3) + 2. A correção foi configurar as regras oficiais e gerar os
# dados fictícios a partir da quantidade calculada.


# K é o número de personalização do grupo. Alterá-lo muda a quantidade de
# alunos-fronteira esperada: exatamente (K mod 3) + 2.
K = 37
QUANTIDADE_ALUNOS_FICTICIOS = 10
QUANTIDADE_FRONTEIRAS_ESPERADA = (K % 3) + 2

# Estas constantes ficam concentradas para permitir uma alteração simples ao
# vivo. Exemplo: trocar MEDIA_APROVACAO para 6.0 muda a regra de aprovação.
# Fonte: UNIFSA, seção Rendimentos, item 1(b): aprovação por média >= 7,0.
MEDIA_APROVACAO = 7.0
# Fonte: UNIFSA, seção Rendimentos, item 3(b): exame com MA >= 4,0 e < 7,0.
MEDIA_MINIMA_PROVA_FINAL = 4.0
# Fonte: UNIFSA, seção Rendimentos, item 4: média final do exame >= 6,0.
MEDIA_FINAL_APROVACAO = 6.0
# Fonte: UNIFSA, seção Rendimentos: são computadas três notas.
QUANTIDADE_AVALIACOES = 3
# Fonte: UNIFSA, seção Rendimentos: frequência mínima obrigatória de 75%.
FREQUENCIA_MINIMA = 75.0

# A lista representa a turma; cada aluno é um dicionário porque os campos
# possuem nomes diferentes e podem ser consultados/atualizados diretamente.
alunos = []

SITUACOES = (
    "APROVADO",
    "PROVA FINAL",
    "REPROVADO POR NOTA",
    "REPROVADO POR FALTA",
)


def ler_inteiro(mensagem, minimo=None):
    """Lê um inteiro e repete a pergunta quando a entrada é inválida."""
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}.")
            else:
                return valor
        except ValueError:
            # Se o usuário digitar uma letra, int() gera ValueError e esta
            # linha informa o erro sem encerrar o programa.
            print("Entrada inválida. Digite um número inteiro.")


def ler_decimal(mensagem, minimo=None, maximo=None):
    """Lê um número decimal aceitando vírgula ou ponto."""
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if minimo is not None and valor < minimo:
                print(f"O valor não pode ser menor que {minimo}.")
            elif maximo is not None and valor > maximo:
                print(f"O valor não pode ser maior que {maximo}.")
            else:
                return valor
        except ValueError:
            # Esta é a linha que trata letras digitadas em uma nota/carga.
            print("Entrada inválida. Digite um número.")


def validar_nota(nota):
    """Valida o intervalo oficial de notas."""
    # Fonte: UNIFSA, seção Rendimentos: avaliações de 0 a 10.
    return isinstance(nota, (int, float)) and 0 <= nota <= 10


def validar_faltas(faltas):
    """Valida que faltas sejam inteiras e não negativas."""
    # Fonte: UNIFSA, seção Rendimentos, itens 1(a), 3(a) e 5(a): controle de
    # frequência e faltas obrigatórios. O valor negativo não é uma falta válida.
    return isinstance(faltas, int) and faltas >= 0


def validar_carga_horaria(carga_horaria):
    """Valida uma carga horária positiva."""
    return isinstance(carga_horaria, (int, float)) and carga_horaria > 0


def truncar_uma_casa(valor):
    """Apura a nota na primeira casa decimal, sem arredondamento."""
    # Fonte: UNIFSA, seção Rendimentos: notas apuradas na primeira casa
    # decimal sem arredondamento.
    return math.floor(valor * 10) / 10


def criar_aluno(nome, notas, faltas, carga_horaria):
    """Cria o dicionário padronizado de um aluno."""
    if len(notas) != QUANTIDADE_AVALIACOES:
        raise ValueError("A turma deve possuir exatamente três notas.")
    if not all(validar_nota(nota) for nota in notas):
        raise ValueError("Todas as notas devem estar entre 0 e 10.")
    if not validar_faltas(faltas):
        raise ValueError("Faltas não podem ser negativas.")
    if not validar_carga_horaria(carga_horaria):
        raise ValueError("A carga horária deve ser positiva.")
    return {
        "nome": nome.strip(),
        "notas": notas[:],
        "media": None,
        "faltas": faltas,
        "carga_horaria": carga_horaria,
        "frequencia": None,
        "situacao": "",
        "nota_prova_final_necessaria": None,
        "faltas_restantes": None,
        "fronteira": False,
    }


def cadastrar_aluno():
    """Cadastra um aluno com três notas, faltas e carga horária."""
    while True:
        nome = input("Nome do aluno: ").strip()
        if nome:
            break
        print("O nome não pode ficar vazio.")

    notas = []
    for numero in range(QUANTIDADE_AVALIACOES):
        notas.append(ler_decimal(f"Nota {numero + 1}: ", 0, 10))
    faltas = ler_inteiro("Quantidade de faltas: ", minimo=0)
    carga_horaria = ler_decimal("Carga horária da disciplina: ", 0.01)
    aluno = criar_aluno(nome, notas, faltas, carga_horaria)
    atualizar_dados_aluno(aluno)
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso.")


def calcular_media(notas):
    """Calcula MA como média simples das três notas, sem arredondar."""
    # Fonte: UNIFSA, seção Rendimentos: são três notas e a MA é a média
    # aritmética simples entre N1, N2 e N3.
    return truncar_uma_casa(sum(notas) / QUANTIDADE_AVALIACOES)


def verificar_frequencia(faltas, carga_horaria):
    """Calcula frequência, limite e quantidade de faltas restantes."""
    if not validar_faltas(faltas) or not validar_carga_horaria(carga_horaria):
        raise ValueError("Faltas ou carga horária inválidas.")

    # Fonte: UNIFSA, seção Rendimentos, itens 1(a), 3(a) e 5(a): frequência
    # mínima de 75%. No simulador, uma falta corresponde a uma hora-aula.
    frequencia = max(0.0, (carga_horaria - faltas) / carga_horaria * 100)
    limite_faltas = carga_horaria * (1 - FREQUENCIA_MINIMA / 100)
    faltas_restantes = max(0, math.floor(limite_faltas - faltas + 1e-9))
    faltas_acima_limite = max(0, math.ceil(faltas - limite_faltas - 1e-9))
    return {
        "frequencia": frequencia,
        "limite_faltas": limite_faltas,
        "faltas_restantes": faltas_restantes,
        "faltas_acima_limite": faltas_acima_limite,
        "no_limite": abs(faltas - limite_faltas) < 1e-9,
    }


def verificar_situacao(aluno):
    """Classifica o aluno conforme nota e frequência."""
    frequencia = verificar_frequencia(aluno["faltas"], aluno["carga_horaria"])
    media = aluno["media"]

    # Fonte: UNIFSA, seção Rendimentos, item 5(a): falta de 75% reprova,
    # independentemente da média. A frequência é verificada primeiro.
    if frequencia["frequencia"] < FREQUENCIA_MINIMA:
        return "REPROVADO POR FALTA"
    # Fonte: UNIFSA, seção Rendimentos, item 1: MA >= 7,0 aprova por média.
    if media >= MEDIA_APROVACAO:
        return "APROVADO"
    # Fonte: UNIFSA, seção Rendimentos, item 3: 4,0 <= MA < 7,0 permite exame.
    if media >= MEDIA_MINIMA_PROVA_FINAL:
        return "PROVA FINAL"
    # Fonte: UNIFSA, seção Rendimentos, item 5(b): MA inferior a 4,0 reprova.
    return "REPROVADO POR NOTA"


def calcular_nota_prova_final(media_atual):
    """Calcula EF mínima ou retorna None quando ela é matematicamente impossível."""
    # Fonte: UNIFSA, seção Rendimentos, item 4: MF = (MA + EF) / 2 e MF >= 6,0.
    nota = 2 * MEDIA_FINAL_APROVACAO - media_atual
    if nota <= 0:
        return 0.0
    if nota > 10:
        return None
    return truncar_uma_casa(nota)


def calcular_faltas_restantes(aluno):
    """Retorna quantas faltas ainda podem ser registradas."""
    # Fonte: UNIFSA, seção Rendimentos, itens 1(a), 3(a) e 5(a): mínimo de 75%.
    return verificar_frequencia(
        aluno["faltas"], aluno["carga_horaria"]
    )["faltas_restantes"]


def verificar_fronteira(aluno):
    """Identifica média exatamente no limite ou falta exatamente no limite."""
    # Fonte: UNIFSA, seção Rendimentos, itens 1(b), 3(b) e 5(a): limites de
    # média e frequência usados para a personalização da turma.
    frequencia = verificar_frequencia(aluno["faltas"], aluno["carga_horaria"])
    media_no_limite = abs(aluno["media"] - MEDIA_APROVACAO) < 1e-9
    falta_no_limite = frequencia["no_limite"]
    return media_no_limite or falta_no_limite


def atualizar_dados_aluno(aluno):
    """Atualiza todos os dados calculados do aluno."""
    aluno["media"] = calcular_media(aluno["notas"])
    frequencia = verificar_frequencia(aluno["faltas"], aluno["carga_horaria"])
    aluno["frequencia"] = frequencia["frequencia"]
    aluno["faltas_restantes"] = frequencia["faltas_restantes"]
    aluno["situacao"] = verificar_situacao(aluno)
    aluno["nota_prova_final_necessaria"] = calcular_nota_prova_final(aluno["media"])
    aluno["fronteira"] = verificar_fronteira(aluno)


def formatar_aluno(aluno):
    """Exibe os principais dados de um aluno."""
    print("Nome:", aluno["nome"])
    print("Notas:", aluno["notas"])
    print(f"Média: {aluno['media']:.1f}")
    print("Faltas:", aluno["faltas"])
    print(f"Frequência: {aluno['frequencia']:.2f}%")
    print("Situação:", aluno["situacao"])
    print("Nota mínima na prova final:", aluno["nota_prova_final_necessaria"])
    print("Faltas restantes:", aluno["faltas_restantes"])
    print("Fronteira:", "SIM" if aluno["fronteira"] else "NÃO")


def encontrar_aluno():
    """Localiza um aluno pelo nome."""
    nome = input("Nome para consulta: ").strip().lower()
    return next((a for a in alunos if a["nome"].lower() == nome), None)


def consultar_aluno():
    if not alunos:
        print("Turma sem alunos cadastrados.")
        return
    aluno = encontrar_aluno()
    if aluno is None:
        print("Aluno não encontrado.")
    else:
        formatar_aluno(aluno)


def listar_alunos():
    if not alunos:
        print("Turma sem alunos cadastrados.")
        return
    for indice, aluno in enumerate(alunos, start=1):
        print(f"{indice} - {aluno['nome']} - {aluno['situacao']}")


def gerar_relatorio_turma():
    """Exibe contagem por situação, média geral e maior média."""
    if not alunos:
        print("Turma sem alunos cadastrados.")
        return
    contagem = {situacao: 0 for situacao in SITUACOES}
    for aluno in alunos:
        contagem[aluno["situacao"]] += 1
    maior = max(alunos, key=lambda aluno: aluno["media"])
    media_geral = sum(aluno["media"] for aluno in alunos) / len(alunos)
    print("\nRELATÓRIO GERAL DA TURMA")
    print("Total de alunos:", len(alunos))
    for situacao in SITUACOES:
        print(f"{situacao}: {contagem[situacao]}")
    print(f"Média geral: {media_geral:.1f}")
    print("Aluno com maior média:", maior["nome"])
    print("Casos de fronteira:", sum(a["fronteira"] for a in alunos))
    print("Casos esperados pelo K:", QUANTIDADE_FRONTEIRAS_ESPERADA)


def dados_ficticios():
    """Monta 10 alunos com exatamente a quantidade de fronteiras definida por K."""
    quantidade_fronteiras = (K % 3) + 2
    # As duas primeiras posições sempre são fronteiras: média 7,0 e limite de
    # faltas. As posições seguintes recebem média 7,0 até atingir K mod 3 + 2.
    dados = [
        ("Ana Simulada", [7.0, 7.0, 7.0], 0, 60),
        ("Bruno Simulado", [6.0, 6.0, 6.0], 15, 60),
        ("Carla Simulada", [7.0, 7.0, 7.0], 1, 60),
        ("Diego Simulado", [9.0, 8.0, 9.0], 60, 60),
        ("Elisa Simulada", [5.0, 5.0, 5.0], 0, 60),
        ("Fábio Simulada", [10.0, 9.0, 10.0], 1, 60),
        ("Gabriela Simulada", [2.0, 3.0, 3.0], 0, 60),
        ("Heitor Simulada", [4.0, 4.0, 4.0], 0, 60),
        ("Íris Simulada", [6.0, 5.0, 5.0], 0, 60),
        ("João Simulada", [8.0, 8.0, 8.0], 2, 60),
    ]
    # Os índices 0, 1, 2 e 4 são candidatos a fronteira; assim também é
    # possível atender K mod 3 = 2, cujo resultado esperado é 4.
    fronteiras_base = [0, 1, 2, 4]
    for posicao, indice in enumerate(fronteiras_base):
        nota_fronteira = posicao < quantidade_fronteiras
        notas = [7.0, 7.0, 7.0] if nota_fronteira else [8.0, 8.0, 8.0]
        dados[indice] = (dados[indice][0], notas, dados[indice][2], dados[indice][3])
    return dados


def carregar_turma_ficticia():
    """Carrega e calcula os 10 alunos simulados."""
    alunos.clear()
    for nome, notas, faltas, carga_horaria in dados_ficticios():
        aluno = criar_aluno(nome, notas, faltas, carga_horaria)
        atualizar_dados_aluno(aluno)
        alunos.append(aluno)
    encontrados = sum(a["fronteira"] for a in alunos)
    print(f"Turma fictícia carregada com {len(alunos)} alunos.")
    print(f"Fronteiras encontradas: {encontrados}/{QUANTIDADE_FRONTEIRAS_ESPERADA}")


def consultar_prova_final():
    if not alunos:
        print("Turma sem alunos cadastrados.")
        return
    aluno = encontrar_aluno()
    if aluno is None:
        print("Aluno não encontrado.")
    elif aluno["nota_prova_final_necessaria"] is None:
        print("É impossível atingir média final 6,0 com nota máxima 10.")
    else:
        print(f"Nota mínima necessária: {aluno['nota_prova_final_necessaria']:.1f}")


def consultar_faltas():
    if not alunos:
        print("Turma sem alunos cadastrados.")
        return
    aluno = encontrar_aluno()
    if aluno is None:
        print("Aluno não encontrado.")
    else:
        print("Faltas restantes:", calcular_faltas_restantes(aluno))


def executar_testes_obrigatorios():
    """Executa os quatro casos exigidos no enunciado."""
    casos = []

    # Caso 1: aluno exatamente na média mínima de aprovação (item 1(b)).
    aluno = criar_aluno("Teste Média", [7, 7, 7], 0, 60)
    atualizar_dados_aluno(aluno)
    casos.append(("média exatamente 7,0", aluno["situacao"] == "APROVADO"))

    # Caso 2: nota suficiente, mas frequência abaixo de 75% (item 5(a)).
    aluno = criar_aluno("Teste Falta", [8, 8, 8], 16, 60)
    atualizar_dados_aluno(aluno)
    casos.append(("aprovado por nota e reprovado por falta", aluno["situacao"] == "REPROVADO POR FALTA"))

    # Caso 3: validação de nota fora de 0..10 e falta negativa.
    casos.append(("nota inválida", not validar_nota(11)))
    casos.append(("falta negativa", not validar_faltas(-1)))

    # Caso 4: MA=0 exige EF=12, impossível porque a nota máxima é 10.
    aluno = criar_aluno("Teste Impossível", [0, 0, 0], 0, 60)
    atualizar_dados_aluno(aluno)
    casos.append(("prova final impossível", aluno["nota_prova_final_necessaria"] is None))

    for descricao, passou in casos:
        print(f"{'OK' if passou else 'FALHOU'} - {descricao}")
    return all(passou for _, passou in casos)


def alterar_k():
    """Permite demonstrar como K altera a quantidade de fronteiras."""
    global K, QUANTIDADE_FRONTEIRAS_ESPERADA
    novo_k = ler_inteiro("Digite o novo K: ", minimo=0)
    K = novo_k
    QUANTIDADE_FRONTEIRAS_ESPERADA = (K % 3) + 2
    print("K alterado.")
    print("A nova quantidade esperada de fronteiras é", QUANTIDADE_FRONTEIRAS_ESPERADA)


def exibir_menu():
    print("\n--- SIMULADOR DE SITUAÇÃO ACADÊMICA UNIFSA ---")
    print("1 - Cadastrar aluno")
    print("2 - Consultar aluno")
    print("3 - Listar alunos")
    print("4 - Relatório geral da turma")
    print("5 - Calcular nota necessária na prova final")
    print("6 - Consultar faltas restantes")
    print("7 - Carregar turma fictícia")
    print("8 - Executar testes obrigatórios")
    print("9 - Alterar K")
    print("0 - Sair")
    return input("Digite sua opção: ").strip()


def main():
    """Executa o menu principal."""
    # Teste de mesa do laço principal (exemplo para apresentar):
    # entrada | opcao | ação                         | volta ao laço?
    #    7    |  "7"  | carrega 10 alunos fictícios  | sim
    #    4    |  "4"  | imprime o relatório          | sim
    #    0    |  "0"  | encerra o programa           | não
    # Quando a entrada solicitada pelo professor for informada, substitua a
    # sequência acima pelos valores recebidos e repita as mesmas colunas.
    while True:
        opcao = exibir_menu()
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            consultar_aluno()
        elif opcao == "3":
            listar_alunos()
        elif opcao == "4":
            gerar_relatorio_turma()
        elif opcao == "5":
            consultar_prova_final()
        elif opcao == "6":
            consultar_faltas()
        elif opcao == "7":
            carregar_turma_ficticia()
        elif opcao == "8":
            executar_testes_obrigatorios()
        elif opcao == "9":
            alterar_k()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
