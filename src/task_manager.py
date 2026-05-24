"""
Sistema de Gerenciamento de Tarefas - TechFlow Solutions
Disciplina: Engenharia de Software
Descrição: CRUD completo para gerenciamento de tarefas com prioridades e status.
"""

import json
import os
from datetime import datetime

# caminho do arquivo de dados
DATA_FILE = os.path.join(os.path.dirname(__file__), 'tasks.json')

def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding="utf-8") as file:
        return json.load(file)

def salvar_tarefas(tarefas):
    """Salva as tarefas no arquivo JSON."""
    with open(DATA_FILE, 'w', encoding="utf-8") as file:
        json.dump(tarefas, file, indent=2, ensure_ascii=False)

def gerar_id(tarefas):
    """Gera um ID único para cada tarefa."""
    if not tarefas:
        return 1
    return max(tarefa['id'] for tarefa in tarefas) + 1

# --- CRIAR TAREFA ---
def criar_tarefa(titulo, descricao, prioridade="media", responsavel=""):
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

    tarefas = carregar_tarefas()
    nova_tarefa = {
        "id": gerar_id(tarefas),
        "titulo": titulo.strip(),
        "descricao": descricao.strip(),
        "prioridade": prioridade,
        "status": "a_fazer",
        "responsavel": responsavel.strip(),
        "data_criacao": datetime.now().isoformat(),
        "data_atualizacao": datetime.now().isoformat()
    }
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    return nova_tarefa

# --- LER TAREFAS ---
def listar_tarefas(status=None, prioridade=None):
    """
    Lista tarefas com filtros opcionais.
    status: 'a_fazer', 'em_andamento', 'concluida'
    prioridade: 'alta', 'media', 'baixa'
    """
    tarefas = carregar_tarefas()
    if status:
        tarefas = [t for t in tarefas if t['status'] == status]
    if prioridade:
        tarefas = [t for t in tarefas if t['prioridade'] == prioridade]
    return tarefas

def buscar_tarefa_por_id(tarefa_id):
    """Busca uma tarefa pelo ID."""
    tarefas = carregar_tarefas()
    for tarefa in tarefas:
        if tarefa['id'] == tarefa_id:
            return tarefa
    return None

# --- ATUALIZAR TAREFA ---
def atualizar_tarefa(id_tarefa, **campos):
    """
    Atualiza os campos de uma tarefa.
    Campos permitidos: titulo, descricao, prioridade, status, responsavel
    """
    campos_permitidos = ['titulo', 'descricao', 'prioridade', 'status', 'responsavel']
    status_validas = ["a_fazer", "em_andamento", "concluida"]
    prioridades_validas = ['alta', 'media', 'baixa']

    campos_invalidos = set(campos.keys()) - campsos_permitidos
    if campos_invalidos:
        raise ValueError(f"Campos inválidos: {campos_invalidos}. Campos permitidos: {campos_permitidos}")

    if 'status' in campos and campos['status'] not in status_validas:
        raise ValueError(f"Status inválido. Use: {status_validas}")

    if "prioridade" in campos and campos["prioridade"] not in prioridades_validas:
        raise ValueError(f"Prioridade inválida. Use: {prioridades_validas}")

    tarefas = carregar_tarefas()
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            for campo, valor in campos.items():
                tarefa[campo] = valor
            tarefa["data_atualizacao"] = datetime.now().isoformat()
            salvar_tarefas(tarefas)
            return tarefa
        return None

# --- DELETAR TAREFA ---
def deletar_tarefa(id_tarefa):
    """
    Remove uma tarefa pelo ID.
    Retorna True se deletada, False se não encontrada.
    """
    tarefas = carregar_tarefas()
    novas_tarefas = [t for t in tarefas if t["id"] != id_tarefa]
    if len(novas_tarefas) == len(tarefas):
        return False  # tarefa não encontrada
    salvar_tarefas(novas_tarefas)
    return True