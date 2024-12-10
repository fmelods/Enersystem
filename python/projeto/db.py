# Conexão com o banco de dados Oracle

import oracledb

try:
    connection = oracledb.connect(
        user="rm556099", 
        password="311004", 
        dsn="oracle.fiap.com.br:1521/orcl" 
    )
    print("Conexão bem-sucedida!")
    connection.close()
except oracledb.DatabaseError as e:
    error, = e.args
    print(f"Erro ao conectar ao banco: {error.message}")
