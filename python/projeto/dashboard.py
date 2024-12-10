# Geração de gráficos com informações de empresas com maior custo de energia

from flask import Flask, jsonify
from flask_cors import CORS
import matplotlib.pyplot as plt
import io
import base64
import cx_Oracle

app = Flask(__name__)
CORS(app)  # Permitir requisições de diferentes origens

# Configuração do banco de dados
db_user = "rm557252"
db_password = "040996"
db_dsn = "oracle.fiap.com.br:1521/orcl"

@app.route('/', methods=['GET'])
def bem_vindo():
    return jsonify({"mensagem": "Bem-vindo a API de Geracao de Graficos!"})

@app.route('/dashboard', methods=['GET'])
def gerar_grafico():
    try:
        # Conexão com o banco de dados
        connection = cx_Oracle.connect(db_user, db_password, db_dsn)
        cursor = connection.cursor()

        # Consulta ao banco
        cursor.execute("""
            SELECT NOME, KWH 
            FROM TB_ENERGSYSTEM_EMPRESA
            ORDER BY KWH DESC
            FETCH FIRST 5 ROWS ONLY
        """)
        resultados = cursor.fetchall()
        connection.close()

        if not resultados:
            return jsonify({"erro": "Nenhum dado encontrado no banco de dados"}), 404

        # Preparar os dados para o gráfico
        empresas = [row[0] for row in resultados]
        consumos = [row[1] for row in resultados]

        # Gerar gráfico
        plt.figure(figsize=(8, 6))
        plt.bar(empresas, consumos, color='blue')
        plt.xlabel("Empresas")
        plt.ylabel("Consumo (kWh)")
        plt.title("Top 5 Empresas por Consumo de Energia")
        plt.xticks(rotation=45)

        # Converter gráfico para base64
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        grafico_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close()

        return jsonify({"grafico": grafico_base64})
    except cx_Oracle.DatabaseError as db_err:
        return jsonify({"erro": f"Erro no banco de dados: {str(db_err)}"}), 500
    except Exception as e:
        return jsonify({"erro": f"Erro inesperado: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
