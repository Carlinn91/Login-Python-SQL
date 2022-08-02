import sqlite3

conn = sqlite3.connect('Usuarios.db')   #variavel pra conexão conn

cursor = conn.cursor()

cursor.execute; ("""
CREATE TABLE IF NOT EXISTS Usuariosok (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL,
);
""")

print("Conectado ao banco de dados")
