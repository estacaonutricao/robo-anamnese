import os
from flask import Flask, request, jsonify
from robo_anamnese import AnamneseProcessor  # Importa o robô criado anteriormente

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
