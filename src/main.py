import sys
import os

# Garante que o Python encontre a pasta 'src' para os imports, independente de onde o terminal foi aberto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.services.tasks_services import TasksService

def exibir_menu():
    print("\n" + "="*35)
    print("Bem-Vindo ao TechFlow Task Manager!")
    print("\nMenu:")
    print("1. Criar Tarefa")
    print("2. Listar Tarefas")
    print("3. Buscar Tarefa por ID")
    print("4. Atualizar Tarefa")
    print("5. Deletar Tarefa")
    print("6. Gerar Relatório de Produtividade")
    print("0. Sair")
    print("\n" + "="*35)

def main():

    tasks_service = TasksService(caminho="tasks.json")

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (0-6): ").strip()
        print("="*35)
        
        match escolha:
            case "1":
                titulo = input("Título: ")
                descricao = input("Descrição: ")
                prioridade = input("Prioridade (alta, media, baixa): ")
                responsavel = input("Responsável: ")
                try:
                    tarefa = tasks_service.criar_tarefa(titulo, descricao, prioridade, responsavel)
                    print(f"Tarefa criada com ID: {tarefa.id}")
                except ValueError as e:
                    print(f"Erro: {e}")
            case "2":
                status = input("Filtrar por status (a_fazer, em_andamento, concluida) ou deixe vazio: ")
                prioridade = input("Filtrar por prioridade (alta, media, baixa) ou deixe vazio: ")
                tarefas = tasks_service.listar_tarefas(status=status or None, prioridade=prioridade or None)
                for t in tarefas:
                    print(f"{t.id}: {t.titulo} - {t.status} - {t.prioridade}")
            case "3":
                id_tarefa = int(input("ID da tarefa: "))
                tarefa = tasks_service.buscar_tarefa_por_id(id_tarefa)
                if tarefa:
                    print(f"{tarefa.id}: {tarefa.titulo} - {tarefa.status} - {tarefa.prioridade}")
                else:
                    print("Tarefa não encontrada.")
            case "4":
                id_tarefa = int(input("ID da tarefa a atualizar: "))
                campos = {}
                campos["titulo"] = input("Novo título (deixe vazio para manter): ").strip() or None
                campos["descricao"] = input("Nova descrição (deixe vazio para manter): ").strip() or None
                campos["prioridade"] = input("Nova prioridade (alta, media, baixa) ou deixe vazio para manter: ").strip() or None
                campos["status"] = input("Novo status (a_fazer, em_andamento, concluida) ou deixe vazio para manter: ").strip() or None
                campos["responsavel"] = input("Novo responsável (deixe vazio para manter): ").strip() or None
                try:
                    tarefa_atualizada = tasks_service.atualizar_tarefa(id_tarefa, **{k:v for k,v in campos.items() if v is not None})
                    if tarefa_atualizada:
                        print("Tarefa atualizada com sucesso.")
                    else:
                        print("Tarefa não encontrada.")
                except ValueError as e:
                    print(f"Erro: {e}")
            case "5":
                id_tarefa = int(input("ID da tarefa a deletar: "))
                if tasks_service.deletar_tarefa(id_tarefa):
                    print("Tarefa deletada com sucesso.")
                else:
                    print("Tarefa não encontrada.")
            case "6":
                relatorio = tasks_service.gerar_relatorio_produtividade()
                print(f"Total de tarefas: {relatorio['total']}")
                print(f"Tarefas a fazer: {relatorio['a_fazer']}")
                print(f"Tarefas em andamento: {relatorio['em_andamento']}")
                print(f"Tarefas concluídas: {relatorio['concluida']}")
            case "0":
                print("Saindo... Até mais!")
                break

if __name__ == "__main__":
    main()