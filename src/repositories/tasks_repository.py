class TasksRepository:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def carregar_tarefas(self):
        """Carrega as tarefas do arquivo JSON."""
        if not os.path.exists(self.caminho_arquivo):
            return []
        with open(self.caminho_arquivo, 'r', encoding="utf-8") as file:
            return json.load(file)

    def salvar_tarefas(self, tarefas):
        """Salva as tarefas no arquivo JSON."""
        with open(self.caminho_arquivo, 'w', encoding="utf-8") as file:
            json.dump(tarefas, file, indent=2, ensure_ascii=False)
    