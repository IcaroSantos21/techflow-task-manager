# Documentação do Projeto — TechFlow Solutions

## Descrição
Sistema de gerenciamento de tarefas desenvolvido para uma startup de logística,
aplicando metodologias ágeis e boas práticas de Engenharia de Software.

## Funcionalidades
- **CREATE:** Criar tarefas com título, descrição, prioridade e responsável
- **READ:** Listar e buscar tarefas com filtros por status e prioridade
- **UPDATE:** Atualizar campos e avançar status no fluxo Kanban
- **DELETE:** Remover tarefas do sistema
- **RELATÓRIO:** Gerar relatório de produtividade com taxa de conclusão

## Status do Fluxo Kanban
| Status | Descrição |
|---|---|
| a_fazer | Tarefa criada, aguardando início |
| em_andamento | Tarefa em desenvolvimento |
| concluida | Tarefa finalizada e validada |

## Prioridades
| Prioridade | Uso |
|---|---|
| alta | Tarefas críticas e urgentes |
| media | Tarefas normais do fluxo |
| baixa | Tarefas secundárias |

## Testes
21 testes unitários cobrindo todas as operações CRUD e o relatório.
Executados automaticamente via GitHub Actions a cada push na branch main.
