# TechFlow Solutions — Sistema de Gerenciamento de Tarefas

[![CI - Testes Automatizados](https://github.com/IcaroSantos21/techflow-task-manager/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/IcaroSantos21/techflow-task-manager/actions/workflows/ci.yml)

## Objetivo do Projeto

Sistema de gerenciamento de tarefas desenvolvido para uma startup de logística, permitindo acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe.

Projeto prático da disciplina de **Engenharia de Software** — UniFECAF.

---

## Escopo Inicial

- Criação de tarefas com título, descrição, prioridade e responsável.
- Listagem e filtragem por status e prioridade.
- Atualização de status e dados da tarefa: A Fazer → Em Andamento → Concluída13, .
- Exclusão de tarefas.
- Persistência de dados em arquivo JSON.

---

## Mudança de Escopo

**Quando:** Sprint 

**O que mudou:** Adição da funcionalidade de Relatório de Produtividade.

**Justificativa:** Durante a reunião de revisão com a startup de logística, identificou-se a necessidade de monitorar o desempenho da equipe com dados quantitativos para apresentação em reuniões semanais de gestão. O cliente solicitou um relatório que mostrasse:

- Total de tarefas cadastradas.
- Distribuição por status (A Fazer, Em Andamento, Concluída).
- Distribuição por prioridade (Alta, Média, Baixa).
- Taxa de conclusão percentual do projeto.

]**Impacto:** O método `generar_relatorio_produtividade()` foi adicionado à camada de serviços (`TasksService`) com a respectiva interface de exibição no menu principal (`main.py`). O quadro Kanban foi atualizado com o novo card correspondente.
---

## Metodologia Ágil

O projeto utiliza a metodologia **Kanban** gerenciada pela aba *Projects* do GitHub, com cartões que mimetizam o ciclo de vida do desenvolvimento41, 42]:

| Coluna | Descrição |
|---|---|
| To Do | Tarefas planejadas, aguardando início de desenvolvimento. |
| In Progress | Tarefas em desenvolvimento ativo4. |
| Done | Tarefas entregues, testadas e validadas. |

---

## Arquitetura do Sistema

Para garantir as boas práticas de Engenharia de Software, o sistema foi refatorado do modelo procedural estruturado para **Orientação a Objetos (POO)** utilizando o padrão de **Arquitetura em Camadas**, dividindo de forma clara as responsabilidades do software:

- **Models:** Definição da entidade de negócio (`Tarefa`) e suas propriedades nativas.
- **Repositories:** Camada responsável estritamente pela persistência de dados (leitura e escrita do arquivo JSON).
- **Services:** Concentra as regras de negócio do sistema, validações e geração de relatórios.
- **Main:** Camada de apresentação/interface por linha de comando (CLI) com o usuário.

---

## Estrutura do Repositório
```
techflow-task-manager/
├── .github/
│   └── workflows/
│       └── ci.yml           # Pipeline de integração contínua (GitHub Actions) 
├── src/
│   ├── models/
│   │   └── task.py          # Classe/Modelo da entidade Tarefa
│   ├── repositories/
│   │   └── tasks_repository.py # Persistência e manipulação do arquivo JSON
│   ├── services/
│   │   └── tasks_services.py   # Regras de negócio e Relatório de Produtividade
│   ├── init.py
│   └── main.py              # Interface interativa via terminal (Ponto de entrada)
├── tests/
│   └── test_tasks.py        # Testes automatizados unitários (Pytest) ├── docs/                    # Documentação e artefatos de Engenharia de Software 
└── README.md  
```
---

## Como Executar

### Pré-requisitos
Certifique-se de ter o **Python 3** instalado em sua máquina.

```bash
# 1. Clone o repositório
git clone [https://github.com/IcaroSantos21/techflow-task-manager.git](https://github.com/IcaroSantos21/techflow-task-manager.git)
cd techflow-task-manager

# 2. Instale as dependências de testes (Pytest)
pip install -r requirements.txt

# 3. Execute o aplicativo de gerenciamento
python src/main.py

# 4. Execute os testes automatizados
pytest -v 
```

## Controle de Qualidade e Integração Contínua (CI)
O projeto conta com testes unitários para validação de entradas inválidas e consistência do fluxo de dados. Através do GitHub Actions, foi estruturado um pipeline automatizado que executa o pytest a cada push realizado no repositório, garantindo a integridade do código e prevenindo regressões.
### Tecnologias Utilizadas
- Python 3 — Linguagem de programação robusta aplicada ao desenvolvimento do core do sistema.
- Pytest — Framework adotado para a escrita e execução de testes automatizados.
- GitHub Projects — Ferramenta de gestão visual do fluxo Kanban.
- GitHub Actions — Plataforma de automação para CI/CD.
### Equipe e Instituição
#### Desenvolvedor: Ícaro Rodrigues Santos
#### Instituição: UniFECAF
#### Curso: Análise e Desenvolvimento de Sistemas
#### Disciplina: Engenharia de Software