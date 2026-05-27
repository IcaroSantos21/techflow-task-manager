from datetime import datetime
from src.models.task import Task
from src.repositories.tasks_repository import TasksRepository

class TasksService:
    def __init__(self, caminho="tasks.json"):
        self.repository = TasksRepository(caminho)

    # --- CRIAR TAREFA ---
    def criar_tarefa(self, titulo, descricao, prioridade="media", responsavel=""):
        """
        Cria uma nova tarefa.
        Prioridade: 'alta', 'media', 'baixa'
        status inicial: 'a_fazer'
        """
        prioridades_validas = ['alta', 'media', 'baixa']
        if prioridade not in prioridades_validas:
            raise ValueError(f"Prioridade inválida. Use: {prioridades_validas}")

        if not titulo or not titulo.strip():
            raise ValueError("O titulo de tarefa não pode ser vazio.")

        novo_id = self.repository.gerar_id()

        nova_tarefa = Task(
            id=novo_id,
            titulo=titulo.strip(),
            descricao=descricao.strip(),
            prioridade=prioridade,
            responsavel=responsavel.strip()
        )
        self.repository.salvar(nova_tarefa)
        return nova_tarefa

    # --- LER TAREFAS ---
    def listar_tarefas(self, status=None, prioridade=None):
        """
        Lista tarefas com filtros opcionais.
        status: 'a_fazer', 'em_andamento', 'concluida'
        prioridade: 'alta', 'media', 'baixa'
        """
        tarefas = self.repository.listar_todas()
        if status:
            tarefas = [t for t in tarefas if t.status == status]
        if prioridade:
            tarefas = [t for t in tarefas if t.prioridade == prioridade]
        return tarefas

    def buscar_tarefa_por_id(self, tarefa_id):
        """Busca uma tarefa pelo ID."""
        return self.repository.buscar_por_id(tarefa_id)

    # --- ATUALIZAR TAREFA ---
    def atualizar_tarefa(self, id_tarefa, **campos):
        """
        Atualiza os campos de uma tarefa.
        Campos permitidos: titulo, descricao, prioridade, status, responsavel
        """
        campos_permitidos = {'titulo', 'descricao', 'prioridade', 'status', 'responsavel'}
        status_validas = ["a_fazer", "em_andamento", "concluida"]
        prioridades_validas = ['alta', 'media', 'baixa']

        campos_invalidos = set(campos.keys()) - campos_permitidos
        if campos_invalidos:
            raise ValueError(f"Campos inválidos: {campos_invalidos}. Campos permitidos: {campos_permitidos}")

        if 'status' in campos and campos['status'] not in status_validas:
            raise ValueError(f"Status inválido. Use: {status_validas}")

        if "prioridade" in campos and campos["prioridade"] not in prioridades_validas:
            raise ValueError(f"Prioridade inválida. Use: {prioridades_validas}")

        tarefa = self.repository.buscar_por_id(id_tarefa)
        if not tarefa:
            return None

        for campo, valor in campos.items():
            setattr(tarefa, campo, valor)
        tarefa.data_atualizacao = datetime.now().isoformat()
        self.repository.atualizar(tarefa)
        return tarefa

    # --- DELETAR TAREFA ---
    def deletar_tarefa(self, id_tarefa):
        """
        Remove uma tarefa pelo ID.
        """
        return self.repository.deletar(id_tarefa)

    # --- RELATÓRIOS DE PRODUTIVIDADE (MUDANÇA DE ESCOPO) ---
    def gerar_relatorio_produtividade(self):
        """
        Gera relatório de produtividade da equipe.
        Feature adicionada após mudança de escopo solicitada pelo cliente.
        que precisava monitorar o desempenho da equipe.
        """
        tarefas = self.repository.listar_todas()
        total = len(tarefas)

        if total == 0:
            por_status = {"a_fazer": 0, "em_andamento": 0, "concluida": 0}
            por_prioridade = {"alta": 0, "media": 0, "baixa": 0}
            return {
                "total": 0,
                "a_fazer": 0,
                "em_andamento": 0,
                "concluida": 0,
                "por_status": por_status,
                "por_prioridade": por_prioridade,
                "taxa_conclusao": 0.0,
                "mensagem": "Nenhuma tarefa cadastrada."
            }

        por_status = {
            "a_fazer": len([t for t in tarefas if t.status == 'a_fazer']),
            "em_andamento": len([t for t in tarefas if t.status == 'em_andamento']),
            "concluida": len([t for t in tarefas if t.status == 'concluida'])
        }

        por_prioridade = {
            "alta": len([t for t in tarefas if t.prioridade == 'alta']),
            "media": len([t for t in tarefas if t.prioridade == 'media']),
            "baixa": len([t for t in tarefas if t.prioridade == 'baixa'])
        }

        taxa_conclusao = round((por_status['concluida'] / total) * 100, 1)

        return {
            "total": total,
            "a_fazer": por_status["a_fazer"],
            "em_andamento": por_status["em_andamento"],
            "concluida": por_status["concluida"],
            "por_status": por_status,
            "por_prioridade": por_prioridade,
            "taxa_conclusao": taxa_conclusao
        }