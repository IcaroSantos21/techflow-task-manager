from src.services.tasks_services import TasksService

# Caminho para o arquivo de dados — os testes substituem essa variável via monkeypatch
DATA_FILE = "tasks.json"


def _get_service():
    return TasksService(caminho=DATA_FILE)


def criar_tarefa(titulo, descricao, prioridade="media", responsavel=""):
    tarefa = _get_service().criar_tarefa(titulo, descricao, prioridade=prioridade, responsavel=responsavel)
    return tarefa.to_dict()


def listar_tarefas(status=None, prioridade=None):
    tarefas = _get_service().listar_tarefas(status=status, prioridade=prioridade)
    return [t.to_dict() for t in tarefas]


def buscar_tarefa_por_id(id_tarefa):
    t = _get_service().buscar_tarefa_por_id(id_tarefa)
    return t.to_dict() if t else None


def atualizar_tarefa(id_tarefa, **campos):
    t = _get_service().atualizar_tarefa(id_tarefa, **campos)
    return t.to_dict() if t else None


def deletar_tarefa(id_tarefa):
    return _get_service().deletar_tarefa(id_tarefa)


def gerar_relatorio_produtividade():
    return _get_service().gerar_relatorio_produtividade()
