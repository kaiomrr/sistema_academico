# Simulador de Situação Acadêmica — Projeto 07

Projeto acadêmico da disciplina Programação I — Python, Grupo 07, com `K = 37`.

## Situação atual

O programa possui menu, cadastro, validações, armazenamento em listas e dicionários, turma fictícia, relatórios e funções preparadas para média, frequência, prova final e fronteiras.

As regras acadêmicas oficiais da UNIFSA ainda estão **PENDENTES DE CONFIRMAÇÃO**. Por isso, o programa não apresenta situações acadêmicas como oficiais enquanto a configuração não for preenchida.

## Como executar

No terminal, dentro desta pasta:

```text
python grupo07_projeto.py
```

Não há bibliotecas externas.

## Menu

1. Cadastrar aluno
2. Consultar aluno
3. Listar alunos
4. Relatório geral
5. Nota necessária na prova final
6. Faltas restantes
7. Carregar turma fictícia
8. Verificar fronteiras
0. Sair

## Configuração pendente

Os campos estão no início de `grupo07_projeto.py`, no dicionário `REGRAS_ACADEMICAS`. Devem ser preenchidos somente após consulta ao documento oficial:

- média de aprovação;
- média mínima para prova final;
- média após exame;
- quantidade e pesos das avaliações;
- frequência mínima;
- fórmula da prova final;
- artigos e páginas do regulamento.

Também deve ser alterado `REGRAS_ACADEMICAS_CONFIGURADAS` para `True` somente depois da conferência.

## Personalização K

```text
(37 % 3) + 2 = 3
```

A turma demonstrativa possui 10 alunos simulados. A verificação de fronteira é feita por cálculo e não por marcação manual.

## Limitações atuais

- A simulação acadêmica definitiva depende do regulamento oficial.
- A conversão de faltas e carga horária ainda precisa ser confirmada.
- A turma fictícia só poderá ser ajustada para exatamente três fronteiras após as regras oficiais serem conhecidas.
- Nomes, matrículas, integrantes e referências do regulamento ainda precisam ser preenchidos pelo grupo.

## Estrutura sugerida para o relatório

1. Capa.
2. Introdução.
3. Coleta de dados e evidências reais.
4. Descrição da solução.
5. Funções criadas.
6. Algoritmos principais.
7. Testes de mesa manuscritos.
8. Plano e resultados dos testes.
9. Erros encontrados e corrigidos.
10. Uso de IA.
11. Diário de bordo.
12. Conclusão.

Os integrantes devem preencher somente informações verdadeiras sobre coleta, reuniões, testes e decisões.
