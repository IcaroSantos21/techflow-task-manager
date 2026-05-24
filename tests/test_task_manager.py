import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import task_manager

@pytest.fixture(autouse=True)
def arquivo_temp(tmp_path, monkeypatch):
    """Cria um arquivo temporário para testes e o remove após os testes."""
    arquivo = tmp_path / "tasks_test.json"
    monkeypatch.setattr(task_manager, "DATA_FILE", str(arquivo))
    yield arquivo

# --- TESTES DE CRIAÇÃO DE TAREFA ---
class TestCriarTarefa:
    def test_criar_tarefa_valida(self):
        tarefa = task_manager.criar_tarefa("Configuração servidor", "Setup Inicial")
        assert tarefa["id"] == 1
        assert tarefa["titulo"] == "Configuração servidor"
        assert tarefa["descricao"] == "Setup Inicial"
        assert tarefa["prioridade"] == "media"
        assert tarefa["status"] == "a_fazer"

    def test_criar_tarefa_prioridade_alta(self):
        tarefa = task_manager.criar_tarefa("Bug crítico", "Correção urgente", prioridade="alta")
        assert tarefa["prioridade"] == "alta"

    def test_titulo_vazio_levanta_erro(self):
        with pytest.raises(ValueError, match="titulo"):
            task_manager.criar_tarefa("", "Descrição Qualquer")
        
    def test_prioridade_invalida_levanta_erro(self):
        with pytest.raises(ValueError, match="Prioridade"):
            task_manager.criar_tarefa("Tarefa X", "Descrição Qualquer", prioridade="urgente")

    def test_ids_sequenciais(self):
        t1 = task_manager.criar_tarefa("Tarefa 1", "Descrição 1")
        t2 = task_manager.criar_tarefa("Tarefa 2", "Descrição 2")
        t3 = task_manager.criar_tarefa("Tarefa 3", "Descrição 3")
        assert t1["id"] == 1
        assert t2["id"] == 2
        assert t3["id"] == 3

# --- TESTES DE LISTAGEM DE TAREFAS ---
class TestListarTarefas:
    def test_listar_vazio(self):
        assert task_manager.listar_tarefas() == []

    def test_listar_todas(self):
        task_manager.criar_tarefa("Tarefa A", "Descrição A")
        task_manager.criar_tarefa("Tarefa B", "Descrição B")
        assert len(task_manager.listar_tarefas()) == 2

    def test_filtrar_por_status(self):
        task_manager.criar_tarefa("Tarefa A", "Descrição A")
        t2 = task_manager.criar_tarefa("Tarefa B", "Descrição B")
        task_manager.atualizar_tarefa(t2["id"], status="em_andamento")
        resultado = task_manager.listar_tarefas(status="em_andamento")
        assert len(resultado) == 1
        assert resultado[0]["titulo"] == "Tarefa B"

    def test_filtrar_por_prioridade(self):
        task_manager.criar_tarefa("Tarefa Urgente", "D1", prioridade="alta")
        task_manager.criar_tarefa("Tarefa Normal", "D2", prioridade="baixa")
        altas = task_manager.listar_tarefas(prioridade="alta")
        assert len(altas) == 1
        assert altas[0]["titulo"] == "Tarefa Urgente"

    def test_buscar_por_id_existente(self):
        t = task_manager.criar_tarefa("Minha tarefa", "Descrição")
        encontrada = task_manager.buscar_tarefa_por_id(t["id"])
        assert encontrada is not None
        assert encontrada["titulo"] == "Minha tarefa"
    
    def test_buscar_por_id_inexistente(self):
        assert task_manager.buscar_tarefa_por_id(999) is None

# --- TESTES DE ATUALIZAÇÃO DE TAREFA ---
class TestAtualizarTarefa:
    def test_atualizar_status(self):
        t = task_manager.criar_tarefa("Tarefa", "Descrição")
        atualizada = task_manager.atualizar_tarefa(t["id"], status="em_andamento")
        assert atualizada["status"] == "em_andamento"

    def test_atualizar_multiplos_campos(self):
        t = task_manager.criar_tarefa("Tarefa", "Descrição")
        atualizada = task_manager.atualizar_tarefa(t["id"], titulo="Tarefa Atualizada", prioridade="alta")
        assert atualizada["titulo"] == "Tarefa Atualizada"
        assert atualizada["prioridade"] == "alta"

    def test_status_invalido_levanta_erro(self):
        t = task_manager.criar_tarefa("Tarefa", "Descrição")
        with pytest.raises(ValueError, match="Status"):
            task_manager.atualizar_tarefa(t["id"], status="finalizada")

    def test_campo_invalido_levanta_erro(self):
        t = task_manager.criar_tarefa("Tarefa", "Descrição")
        with pytest.raises(ValueError, match="inválidos"):
            task_manager.atualizar_tarefa(t["id"], campo_desconhecido="valor")

    def test_id_inexistente_retorna_none(self):
        assert task_manager.atualizar_tarefa(999, status="em_andamento") is None

# --- TESTES DE DELEÇÃO DE TAREFA ---
class TestDeletarTarefa:
    def test_deletar_existente(self):
        t = task_manager.criar_tarefa("Tarefa", "Descrição")
        assert task_manager.deletar_tarefa(t["id"]) is True
        assert task_manager.buscar_tarefa_por_id(t["id"]) is None
    
    def test_deletar_inexistente(self):
        assert task_manager.deletar_tarefa(999) is False

    def test_deletar_nao_afeta_outras(self):
        t1 = task_manager.criar_tarefa("Tarefa 1", "Descrição 1")
        t2 = task_manager.criar_tarefa("Tarefa 2", "Descrição 2")
        task_manager.deletar_tarefa(t1["id"])
        restantes = task_manager.listar_tarefas()
        assert len(restantes) == 1
        assert restantes[0]["id"] == t2["id"]