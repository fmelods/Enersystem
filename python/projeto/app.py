# API ENERSYSTEM

from flask import Flask, jsonify, request
import oracledb
from crud import inserir_empresa, listar_empresas, atualizar_empresa, excluir_empresa

app = Flask(__name__)

ERROR_DB_CONNECTION = "Erro ao conectar ao banco de dados"

def get_db_connection():
    try:
        connection = oracledb.connect(
            user="rm556099", 
            password="311004", 
            dsn="oracle.fiap.com.br:1521/orcl"
        )
        return connection
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None

@app.route('/')
def hello_world():
    return jsonify({"mensagem": "Bem-vindo a API da Enersystem!"}), 200

# MÉTODO POST
@app.route('/crud/empresa', methods=['POST'])
def cadastrar_empresa():
    try:
        data = request.get_json()
        nome_empresa = data.get('nome_empresa')
        estado = data.get('estado')
        id_tipo_energia = data.get('id_tipo_energia')
        custo_kwh = data.get('custo_kwh')
        
        if not nome_empresa or not estado or not id_tipo_energia or custo_kwh is None:
            return jsonify({"erro": "Todos os campos são obrigatórios!"}), 400
        
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            inserir_empresa(cursor, nome_empresa, estado, id_tipo_energia, custo_kwh)
            connection.commit()
            cursor.close()
            connection.close()
            return jsonify({"mensagem": "Empresa cadastrada com sucesso!"}), 201
        else:
            return jsonify({"erro": ERROR_DB_CONNECTION}), 500
    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"erro": "Erro ao cadastrar a empresa"}), 500

# MÉTODO GET
@app.route('/consulta/empresas', methods=['GET'])
def consultar_empresas_api():
    try:
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id_empresa, nome_empresa, estado, custo_kwh FROM tb_enersystem_empresa")
            empresas = cursor.fetchall()
            connection.close()

            empresas_list = [
                {
                    'id_empresa': empresa[0],
                    'nome_empresa': empresa[1],
                    'estado': empresa[2],
                    'custo_kwh': empresa[3]
                } for empresa in empresas
            ]
            return jsonify(empresas_list), 200
        else:
            return jsonify({"erro": ERROR_DB_CONNECTION}), 500
    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"erro": "Erro ao consultar as empresas"}), 500

# MÉTODO PUT
@app.route('/crud/empresa/<int:id_empresa>', methods=['PUT'])
def atualizar_empresa(id_empresa):
    try:
        data = request.get_json()
        print(f"Dados recebidos para atualização: {data}")  # Log para verificar os dados recebidos
        nome_empresa = data.get('nome_empresa')
        estado = data.get('estado')
        id_tipo_energia = data.get('id_tipo_energia')
        custo_kwh = data.get('custo_kwh')

        if not nome_empresa or not estado or not id_tipo_energia or custo_kwh is None:
            print("Faltando campos obrigatórios!")  # Log de erro
            return jsonify({"erro": "Todos os campos são obrigatórios!"}), 400

        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()

            cursor.execute("""
                UPDATE tb_enersystem_empresa
                SET nome_empresa = :nome_empresa,
                    estado = :estado,
                    id_tipo_energia = :id_tipo_energia,
                    custo_kwh = :custo_kwh
                WHERE id_empresa = :id_empresa
            """, {
                'nome_empresa': nome_empresa,
                'estado': estado,
                'id_tipo_energia': id_tipo_energia,
                'custo_kwh': custo_kwh,
                'id_empresa': id_empresa
            })
            
            connection.commit()
            cursor.close()
            connection.close()

            return jsonify({"mensagem": "Empresa atualizada com sucesso!"}), 200
        else:
            return jsonify({"erro": "Erro ao conectar ao banco de dados"}), 500

    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"erro": "Erro ao atualizar a empresa"}), 500

# MÉTODO DELETE
@app.route('/crud/empresa/<int:id_empresa>', methods=['DELETE'])
def deletar_empresa_api(id_empresa):
    try:
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            excluir_empresa(cursor, id_empresa)
            connection.commit()
            cursor.close()
            connection.close()
            return jsonify({"mensagem": "Empresa deletada com sucesso!"}), 200
        else:
            return jsonify({"erro": ERROR_DB_CONNECTION}), 500
    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"erro": "Erro ao deletar a empresa"}), 500

if __name__ == '__main__':
    app.run(debug=True)
