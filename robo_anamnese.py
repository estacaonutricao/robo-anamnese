class AnamneseProcessor:
    def __init__(self, dados):
        self.dados = dados

    def gerar_relatorio(self):
        return {
            "mensagem": "Anamnese processada com sucesso!",
            "dados_recebidos": self.dados
        }
