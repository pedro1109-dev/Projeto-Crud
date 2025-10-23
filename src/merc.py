from connect import get_connet
#importando a biblioteca de criptografia
import os

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_produtos(desc, preço, quant):
    limpar()
    try:
        conn = get_connet()
        cursor = conn.cursor()
        #chamando codigo em sql
        cursor.execute('INSERT INTO TB_PRODUTOS(desc, preco, quant) VALUES (?, ?, ?)',
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
        cursor.execute('SELECT DESC, PRECO, QUANT  FROM TB_PRODUTOS')
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
            PRECO FLOAT(10,2)
            QUANT INTEGER NOT NULL
        );
        ''')
    except Exception as e:
        print(f"Falha ao criar tabela: {e}")


def editar_produt(nova_descricao, novo_preco, id_editar):
    limpar()
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute(
        'UPDATE TB_PRODUTOS SET DESC=?, PRECO=? WHERE ID=?',
        (nova_descricao, novo_preco, id_editar)
        )   
        conn.commit()
        if cursor.rowcount > 0:
            print("Produto editado com sucesso!")
        else:
            print("Produto não encontrado.")

    except Exception as e:
        print(f'Falha ao editar produto: {e}')
    finally:
        conn.close()

def vender(id_produto, quant_saida):
    limpar()
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('SELECT QUANT FROM TB_PRODUTOS WHERE ID = ?',(id_produto,))
        quant = cursor.fetchone()
        if not quant:
            print('Produto nçao encontrado ')
        quant = quant[0]
        if quant >= 0 :
            if quant >= quant_saida:
                quant_restante = quant - quant_saida
                cursor.execute('UPDATE TB_PRODUTOS SET QUANT = ? WHERE ID = ?',
                               (quant_restante, id_produto,))
            else:
                print('A quantidade exigida é maior da qual reside no mercado!')
        else:
            print('O produto acabou!!')
        conn.commit()



    except Exception as e:
        print(f"Falha ao vender produto: {e}")

        
