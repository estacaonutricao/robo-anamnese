class AnamneseProcessor:
    def __init__(self, dados):
        self.dados = dados

    def gerar_relatorio(self):
        # Aqui você pode processar os dados como necessário
        return {"mensagem": "Relatório gerado com sucesso!", "dados_recebidos": self.dados}
