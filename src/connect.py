import sqlite3

def get_connet():
    try:
        conexao = sqlite3.connect('controle_produto.db')
        print("Conexão bem sucedida!")
        return conexao
    except sqlite3.Error as e:
        print("Falha na conexão")
        return None

if __name__=='__main__':
    get_connet()