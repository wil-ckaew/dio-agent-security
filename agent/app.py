import sqlite3

def fazer_login(usuario, senha):
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()
    # VULNERÁVEL: concatena entrada do usuário
    query = f"SELECT * FROM usuarios WHERE username = '{usuario}' AND password = '{senha}'"
    cursor.execute(query)
    resultado = cursor.fetchone()
    conexao.close()
    return "Acesso Permitido" if resultado else "Acesso Negado"
