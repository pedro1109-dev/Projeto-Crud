#importando a conexão
from connection import get_connet
from merc import cadastrar_produtos
from merc import listar_produtos
from merc import criar_tabela_produtos
from merc import editar_produt
from merc import vender
#importando a biblioteca de criptografia
import pwinput
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
#Criar usuario
def criar_usuario(nome, email, senha):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        #chamando codigo em sql
        cursor.execute('INSERT INTO TB_USUARIO(nome, email, senha) VALUES (?, ?, ?)',
                       (nome, email, senha,)
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

def menu():
    print(f'{30*'-'}MENU{30*'-'}')
    print()
    print('1-Criar usuário')
    print('2-Listar')
    print('3-Criar tabela de produtos')
    print('4-Cadastrar produtos')
    print('5-Listar Produtos')
    print('6-Editar produtos ')
    print('7- Vender')
    print()

    
if __name__=='__main__':
    while True:
        menu()
        opcao = input('Digite a opção que deseja utilizar : ')
        match opcao :
            case '1':
                nome = input('Digite o nome: ').strip().title()
                email = input('Digite um email: ').strip()
                senha = pwinput.pwinput('Digite uma senha: ').strip()
                criar_usuario(nome, email, senha)
            case'2':
                listar_usuario()
            case '3':
                criar_tabela_produtos()
            case '4':
                desc = input('Digite a descrição do produto : ').strip()
                preco = float(input('Digite o preço do produto : '))
                quant = int(input('Digite a quantidade do produto : '))
                cadastrar_produtos(desc, preco, quant)
            case '5':
                listar_produtos()
            case '6':
                editar_produt()
            case '7' :
                vender()
            case '8':
                criar_tabela()
            case '9':
                break

    
    