class NotFound(Exception):
    def __init__(self, nome: str):
        self.nome = nome