import sqlite3

def fazer_login(usuario, senha):
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()
    # CORRIGIDO: consulta parametrizada
    query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"
    cursor.execute(query, (usuario, senha))
    resultado = cursor.fetchone()
    conexao.close()
    return "Acesso Permitido" if resultado else "Acesso Negado"
