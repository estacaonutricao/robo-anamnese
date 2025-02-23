import os
from flask import Flask, request, jsonify
from robo_anamnese import AnamneseProcessor  # Importa o robô criado anteriormente

app = Flask(__name__)

# Rota para testar se o servidor está online
@app.route('/')
def home():
    return "Servidor rodando com sucesso!"

# Rota para processar a anamnese
@app.route('/processar_anamnese', methods=['POST'])
def processar_anamnese():
    try:
        dados = request.json  # Recebe os dados do Typeform via Webhook

        if not dados:
            return jsonify({"erro": "Nenhum dado recebido"}), 400

        # Processa os dados com o robô
        anamnese = AnamneseProcessor(dados)
        relatorio = anamnese.gerar_relatorio()

        return jsonify({"relatorio": relatorio})  # Retorna o relatório formatado

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# ✅ Rota para listar todas as rotas disponíveis no servidor
@app.route('/listar_rotas', methods=['GET'])
def listar_rotas():
    rotas = [rule.rule for rule in app.url_map.iter_rules()]
    return jsonify({"rotas_disponiveis": rotas})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
