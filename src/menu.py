
from user import criar_tabela
from user import criar_usuario
from user import listar_usuario
from user import excluir_usuario
from merc import criar_tabela_produtos
from merc import cadastrar_produtos
from merc import editar_produt
from merc import vender
from merc import listar_produtos
#importando a biblioteca de criptografia
import pwinput

def sair():
    exit()

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
                id_editar = input("Digite o ID do produto : ")
                nova_descricao = input("Digite a nova descrição do produto : ")
                novo_preco = input("Digite o novo preço do produto : ")
                editar_produt(id_editar, nova_descricao, novo_preco)
            case '7' :
                id_produto = input("Digite o ID do produto : ")
                quant_saida = int(input("Digite a quantidade que deseja retirar : "))
                vender(id_produto, quant_saida)
            case '8':
                criar_tabela()
            case '9':
                break