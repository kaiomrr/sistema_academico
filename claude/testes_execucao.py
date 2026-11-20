"""Testes básicos executáveis sem bibliotecas externas."""

# [IA] Testes iniciais produzidos com auxílio de inteligência artificial.

import grupo07_projeto as projeto


def verificar(condicao, descricao):
    """Mostra PASSOU ou FALHOU para uma condição de teste."""
    # Autor: Integrante responsável
    resultado = "PASSOU" if condicao else "FALHOU"
    print(f"{resultado}: {descricao}")
    return condicao


def executar_testes():
    """Executa testes de validação e da estrutura pendente."""
    # Autor: Integrante responsável
    resultados = []
    resultados.append(verificar(projeto.validar_nota(10), "nota 10 é válida"))
    resultados.append(verificar(not projeto.validar_nota(11), "nota 11 é inválida"))
    resultados.append(verificar(not projeto.validar_nota(-1), "nota -1 é inválida"))
    resultados.append(verificar(not projeto.validar_faltas(-1), "faltas negativas são inválidas"))
    resultados.append(verificar(projeto.validar_carga_horaria(1), "carga positiva é válida"))
    resultados.append(verificar(not projeto.validar_carga_horaria(0), "carga zero é inválida"))
    resultados.append(verificar(len(projeto.REGRAS_ACADEMICAS) > 0, "configuração acadêmica existe"))
    resultados.append(verificar(not projeto.regras_estao_configuradas(), "regras pendentes são bloqueadas"))
    resultados.append(verificar(projeto.verificar_situacao(projeto.criar_aluno("Teste", [8], 0, 60)) == "REGRAS PENDENTES", "situação não oficial é bloqueada"))
    print(f"\nResumo: {sum(resultados)}/{len(resultados)} testes básicos passaram.")


if __name__ == "__main__":
    executar_testes()
