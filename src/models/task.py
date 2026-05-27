from datetime import datetime

class Task():
    def __init__(self,id: int, titulo: str, descricao: str, responsavel: str, prioridade: str = "media"):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.responsavel = responsavel

        self.status = "a_fazer"
        self.data_criacao = datetime.now().isoformat()
        self.data_atualizacao = datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "responsavel": self.responsavel,
            "status": self.status,
            "data_criacao": self.data_criacao,
            "data_atualizacao": self.data_atualizacao
        }