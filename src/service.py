#importando a conexão
from connection import get_connet
#importando a biblioteca de criptografia
from passlib.hash import pbkdf2_sha256 as sha256

#Criar usuario
def criar_usuario(nome, email, senha):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        #chamando codigo em sql
        cursor.execute('INSERT INTO TB_USUARIO(nome, email, senha) VALUES (?, ?, ?)',
                       (nome, email, senha)
        )

        conn.commit()
        print("Usuário cadastrado com sucesso!")
                    

    except Exception as e:
        print(f"Falha ao criar tabela: {e}")
#Listando usuario
def listar_usuario():
    try:
        conn = get_connet()
        cursor = conn.cursor()
        #Chamando codigo em sql
        cursor.execute('SELECT NOME, EMAIL, SENHA FROM TB_USUARIO')
        usuarios = cursor.fetchall()

        if usuarios:
            print(f'{30*'-'}Lista de usuarios{30*'-'}')
            for u in usuarios:
                print(f'| {u}')
        else:
            print('Nenhum usuário encontrado!')

    except Exception as e:
        print(f"Falha ao criar tabela: {e}")

def excluir_usuario(id):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM TB_USUARIO WHERE ID=?
        """, (id,))

        conn.commit()


    except Exception as e:
        print(f"Falha ao criar tabela: {e}")

def editar_usuario(id):
    ...

def listar_usuario_email(email):
    ...

def listar_usuario_id(id):
    ...
#Criando tabela
def criar_tabela():
    try:
        conn = get_connet()
        cursor = conn.cursor()
    #Chamdno codigo em sql
        cursor.execute('''
        CREATE TABLE TB_USUARIO(
            ID INTEGER PRIMARY KEY,
            NOME VARCHAR(120) NOT NULL,
            EMAIL VARCHAR(120) UNIQUE,
            SENHA VARCHAR(255)
        );
        ''')
    except Exception as e:
        print(f"Falha ao criar tabela: {e}")
    
if __name__=='__main__':
    #criar_tabela()
    nome = input('Digite o nome: ').strip().title()
    email = input('Digite um email: ').strip()
    senha = input('Digite uma senha: ').strip()
    senha = sha256.hash(senha)
    criar_usuario(nome, email, senha)
    excluir_usuario(6)
    excluir_usuario(7)
    excluir_usuario(8)
    excluir_usuario(9)
    excluir_usuario(10)
    excluir_usuario(11)
    excluir_usuario(12)
    listar_usuario()

    
    