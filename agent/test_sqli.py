import sqlite3

con = sqlite3.connect('usuarios.db')
con.execute("INSERT INTO usuarios (username, password) VALUES ('admin', 'senha123')")
con.commit()

# Payload classico SQLite: ' OR 1=1 --  (espaco depois do -- para comentario)
payload = "' OR 1=1 -- "
senha = "qualquer"

# VERSAO VULNERAVEL (app.py)
query = f"SELECT * FROM usuarios WHERE username = '{payload}' AND password = '{senha}'"
print("=== VULNERAVEL (app.py) ===")
print("QUERY:", query)
con2 = sqlite3.connect('usuarios.db')
cur = con2.cursor()
cur.execute(query)
linhas = cur.fetchall()
print("RESULTADO:", linhas)
print("Bypass autenticacao:", "SIM - acesso permitido sem senha" if linhas else "Nao")
print()

# VERSAO CORRIGIDA (app_corrigido.py)
print("=== CORRIGIDA (app_corrigido.py) ===")
query2 = "SELECT * FROM usuarios WHERE username = ? AND password = ?"
cur2 = con2.cursor()
cur2.execute(query2, (payload, senha))
linhas2 = cur2.fetchall()
print("QUERY:", query2)
print("PARAMS:", (payload, senha))
print("RESULTADO:", linhas2)
print("Bypass autenticacao:", "SIM" if linhas2 else "NAO - parametros tratados como dados")
print()

# Login real do admin na versao corrigida
print("=== CORRIGIDA: login REAL admin ===")
cur3 = con2.cursor()
cur3.execute(query2, ("admin", "senha123"))
print("RESULTADO:", cur3.fetchall())
print("Acesso:", "Permitido" if cur3.fetchall() else "Negado")
con2.close()
