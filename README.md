# TechFlow Solutions — Sistema de Gerenciamento de Tarefas

[![CI - Testes Automatizados](https://github.com/IcaroSantos21/techflow-task-manager/actions/workflows/ci.yml/badge.svg)](https://github.com/IcaroSantos21/techflow-task-manager/actions)

## Objetivo do Projeto

Sistema de gerenciamento de tarefas desenvolvido para uma startup de logística,
permitindo acompanhar o fluxo de trabalho em tempo real, priorizar tarefas
críticas e monitorar o desempenho da equipe.

Projeto da disciplina de **Engenharia de Software** — UniFECAF.

---

## Escopo Inicial

- Criação de tarefas com título, descrição, prioridade e responsável
- Listagem e filtragem por status e prioridade
- Atualização de status: A Fazer → Em Andamento → Concluída
- Exclusão de tarefas
- Persistência de dados em arquivo JSON

---

## Mudança de Escopo

**Quando:** Sprint 2

**O que mudou:** Adição da funcionalidade de Relatório de Produtividade.

**Justificativa:** Durante a revisão com o cliente, identificou-se a necessidade
de monitorar o desempenho da equipe com dados quantitativos para apresentação
em reuniões semanais de gestão. O cliente solicitou um relatório que mostrasse:

- Total de tarefas cadastradas
- Distribuição por status (A Fazer, Em Andamento, Concluída)
- Distribuição por prioridade (Alta, Média, Baixa)
- Taxa de conclusão percentual do projeto

**Impacto:** A função `gerar_relatorio()` foi adicionada ao `task_manager.py`
com testes automatizados. O Kanban foi atualizado com o novo card.

---

## Metodologia Ágil

O projeto utiliza **Kanban** gerenciado pelo GitHub Projects, com as colunas:

| Coluna | Descrição |
|---|---|
| To Do | Tarefas planejadas, ainda não iniciadas |
| In Progress | Tarefas em desenvolvimento |
| Done | Tarefas entregues e validadas |

---

## Estrutura do Repositório
```
techflow-task-manager/
├── src/
│   └── task_manager.py      # Módulo principal — lógica CRUD
├── tests/
│   └── test_task_manager.py # Testes automatizados com Pytest
├── docs/                    # Documentação do projeto
├── .github/
│   └── workflows/
│       └── ci.yml           # Pipeline de integração contínua
└── README.md
```
---

## Como Executar

```bash
# Clone o repositório
git clone https://github.com/IcaroSantos21/techflow-task-manager.git
cd techflow-task-manager

# Instale as Dependenciass
pip install requirements.txt

# Execute os testes
pytest tests/ -v
```

---

## Tecnologias

- **Python 3** — linguagem principal
- **Pytest** — testes automatizados
- **GitHub Projects** — gestão Kanban
- **GitHub Actions** — integração contínua

---

## Equipe

Desenvolvido por: Ícaro Santos  
Disciplina: Engenharia de Software — UniFECAF