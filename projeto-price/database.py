import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

os.makedirs(DATA_DIR, exist_ok=True)

DB_PATH = os.path.join(DATA_DIR, 'precos.db')
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    url TEXT,
    site TEXT,
    preco_alvo REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS historico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER,
    preco REAL,
    data TEXT
)
''')

conn.commit()

def cadastrar_produto(nome, url, site, preco_alvo):
    cursor.execute(
        'INSERT INTO produtos (nome, url, site, preco_alvo) VALUES (?, ?, ?, ?)',
        (nome, url, site, preco_alvo)
    )
    conn.commit()

def listar_produtos():
    cursor.execute('SELECT * FROM produtos')
    return cursor.fetchall()