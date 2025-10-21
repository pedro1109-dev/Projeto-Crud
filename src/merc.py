from connection import get_connet
#importando a biblioteca de criptografia
from passlib.hash import pbkdf2_sha256 as sha256
import os

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_produtos(desc, preço, quant):
    limpar()
    try:
        conn = get_connet()
        cursor = conn.cursor()
        #chamando codigo em sql
        cursor.execute('INSERT INTO TB_PRODUTOS(desc, preço, quant) VALUES (?, ?, ?)',
                       (desc, preço, quant)
        )

        conn.commit()
        print("Produto cadastrado com sucesso!")
        
    except Exception as e:
        print(f"Falha ao cadastrar produto: {e}")

def listar_produtos():
    limpar()
    try:
        conn = get_connet()
        cursor = conn.cursor()
        #Chamando codigo em sql
        cursor.execute('SELECT DESC, PREÇO, QUANT  FROM TB_PRODUTOS')
        produtos = cursor.fetchall()

        if produtos:
            print(f'{30*'-'}Lista de produtos{30*'-'}')
            for u in produtos:
                print(f'| {u}')
        else:
            print('Nenhum produto encontrado!')

    except Exception as e:
        print(f"Falha ao criar tabela: {e}")


def criar_tabela_produtos():
    try:
        conn = get_connet()
        cursor = conn.cursor()
    #Chamdno codigo em sql
        cursor.execute('''
        CREATE TABLE TB_PRODUTOS(
            ID INTEGER PRIMARY KEY,
            DESC VARCHAR(120) NOT NULL,
            PREÇO DECIMAL(120) NOT NULL,
            QUANT INTENGER(200) NOT NULL
        );
        ''')
    except Exception as e:
        print(f"Falha ao criar tabela: {e}")


def editar_produt():
    limpar()
    try:
        conn = get_connet()
        cursor = conn.cursor()
        #Chamando codigo em sql
        cursor.execute('SELECT DESC, PREÇO, QUANT FROM TB_PRODUTOS')
        produtos = cursor.fetchone()
        new = input('Digite o produto que deseja atualizar: ')
        if produtos:
            for new in produtos:
                print(f'Produto encontrado!! {new}')
                print(f'{30*'='} ATUALIZANDO {30*'='}')
                nova_desc = input(' Digite a nova descrição do produto :  ')
                novo_preco = float(input('Digite o novo preço : '))
                nova_qunat = int(input('Digite a nova quantidade do produto : '))
                id = input('Digite o ID do produto : ')
                if nova_desc:
                    cursor.execute('UPDATE SET DESC = %s, WHERE ID = %s', 
                                   (nova_desc, id))
                if novo_preco:
                    cursor.execute('UPDATE SET PREÇO = %s, WHERE ID = %s', 
                                   (novo_preco, id))
                if nova_qunat :
                    cursor.execute('UPDATE SET QUANT = %s, WHERE ID = %s', 
                                   (nova_qunat, id))
        else:
            print('Nenhum us encontrado!')

    except Exception as e:
        print(f"Falha ao editar tabela: {e}")

def vender(id_produto, quant_saida):
    limpar()
    try:
        conn = get_connet()
        cursor = conn.cursor()
        quant = cursor.execute('SELECT QUANT FROM TB_PRODUTOS WHERE ID = ?',
                                (id_produto))
        if quant > 0:
            if quant > quant_saida:
                quant_restante = quant - quant_restante
                cursor.execute('UPDATE SET QUANT = ?, WHERE ID = ?',
                               (quant_restante, id_produto))
            else:
                print('A quantidade exigida é menor da qual reside no mercado!')
        else:
            print('O produto acabou!!')




    except Exception as e:
        print(f"Falha ao editar tabela: {e}")

        
