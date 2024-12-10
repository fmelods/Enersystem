# CRUD para a tabela de empresas

import cx_Oracle

# Função para inserir uma nova empresa
def inserir_empresa(cursor, nome_empresa, estado, id_tipo_energia, custo_kwh):
    try:
        sql = """
        INSERT INTO tb_enersystem_empresa (id_empresa, nome_empresa, estado, id_tipo_energia, custo_kwh)
        VALUES (seq_empresa.NEXTVAL, :nome_empresa, :estado, :id_tipo_energia, :custo_kwh)
        """
        cursor.execute(sql, {'nome_empresa': nome_empresa, 'estado': estado, 'id_tipo_energia': id_tipo_energia, 'custo_kwh': custo_kwh})
    except Exception as e:
        print(f"Erro ao inserir empresa: {e}")
        raise

# Função para listar empresas
def listar_empresas(cursor):
    try:
        cursor.execute("SELECT NOME_EMPRESA, ESTADO, CUSTO_KWH FROM TB_ENERSYSTEM_EMPRESA")
        empresas = cursor.fetchall()
        return [{"nome_empresa": emp[0], "estado": emp[1], "custo_kwh": emp[2]} for emp in empresas]
    except Exception as e:
        print(f"Erro ao listar empresas: {e}")
        raise

# Função para atualizar uma empresa
def atualizar_empresa(cursor, id_empresa, nome_empresa, estado, id_tipo_energia, custo_kwh):
    try:
        sql = """
        UPDATE tb_enersystem_empresa
        SET nome_empresa = :nome_empresa, estado = :estado, id_tipo_energia = :id_tipo_energia, custo_kwh = :custo_kwh
        WHERE id_empresa = :id_empresa
        """
        cursor.execute(sql, {'nome_empresa': nome_empresa, 'estado': estado, 'id_tipo_energia': id_tipo_energia, 'custo_kwh': custo_kwh, 'id_empresa': id_empresa})
    except Exception as e:
        print(f"Erro ao atualizar empresa: {e}")
        raise

# Função para excluir uma empresa
def excluir_empresa(cursor, id_empresa):
    try:
        sql = "DELETE FROM tb_enersystem_empresa WHERE id_empresa = :id_empresa"
        cursor.execute(sql, {'id_empresa': id_empresa})
    except Exception as e:
        print(f"Erro ao excluir empresa: {e}")
        raise
