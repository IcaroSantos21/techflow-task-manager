from os import path
import json
from src.models.task import Task

class TasksRepository:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def carregar_tarefas(self):
        """Carrega as tarefas do arquivo JSON."""
        if not path.exists(self.caminho_arquivo):
            return []
        with open(self.caminho_arquivo, 'r', encoding="utf-8") as file:
            dados = json.load(file)

        tarefas_objetos = []
        for t in dados:
            task = Task(
                id=t["id"],
                titulo=t["titulo"],
                descricao=t["descricao"],
                responsavel=t["responsavel"],
                prioridade=t["prioridade"]
            )
            task.status = t["status"]
            task.data_criacao = t["data_criacao"]
            task.data_atualizacao = t["data_atualizacao"]

            tarefas_objetos.append(task)
        return tarefas_objetos

    def salvar_tarefas(self, tarefas_objetos):
        """Salva as tarefas no arquivo JSON."""
        dados_salvar = [t.to_dict() for t in tarefas_objetos]
        with open(self.caminho_arquivo, 'w', encoding="utf-8") as file:
            json.dump(dados_salvar, file, indent=2, ensure_ascii=False)

    def gerar_id(self):
        """Gera um ID único para cada tarefa."""
        tarefas = self.carregar_tarefas()
        if not tarefas:
            return 1
        return max(tarefa.id for tarefa in tarefas) + 1

    def salvar(self, nova_tarefa):
        """Adiciona uma nova tarefa ao arquivo JSON."""
        tarefas = self.carregar_tarefas()
        tarefas.append(nova_tarefa)
        self.salvar_tarefas(tarefas)
        return nova_tarefa

    def listar_todas(self):
        """Retorna todas as tarefas prontas como objetos."""
        return self.carregar_tarefas()

    def buscar_por_id(self, id_tarefa):
        """Busca uma tarefa específica por ID."""
        tarefas = self.carregar_tarefas()
        for t in tarefas:
            if t.id == id_tarefa:
                return t
        return None

    def atualizar(self, tarefa_atualizada):
        """Atualiza os dados de uma tarefa existente no arquivo."""
        tarefas = self.carregar_tarefas()
        for i, t in enumerate(tarefas):
            if t.id == tarefa_atualizada.id:
                tarefas[i] = tarefa_atualizada
                self.salvar_tarefas(tarefas)
                return True
        return False

    def deletar(self, id_tarefa):
        """Remove uma tarefa do arquivo JSON."""
        tarefas = self.carregar_tarefas()
        tarefa_encontrada = False
        
        # Filtra a lista removendo o objeto com o ID correspondente
        novas_tarefas = []
        for t in tarefas:
            if t.id == id_tarefa:
                tarefa_encontrada = True
            else:
                novas_tarefas.append(t)
                
        if tarefa_encontrada:
            self.salvar_tarefas(novas_tarefas)
            return True
        return False
