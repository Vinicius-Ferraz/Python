import os

restaurantes = [{'nome':'Praça','categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema','categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina','categoria':'Italiana', 'ativo':False}
                ]

def exibir_nome_do_programa():
    print(""""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')
    
def voltar_ao_menu_principal():
    input('Pressione ENTER para voltar ao menu principal ')
    main()
    
def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()
    
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()
 
def cadastrar_novo_restaurante():
    exibir_subtitulo('C̳a̳d̳a̳s̳t̳r̳o̳ d̳e̳ r̳e̳s̳t̳a̳u̳r̳a̳n̳t̳e̳')
    nome_do_restaurante = input('Digite o nome do restaurante que gostaria de cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo('Os restaurantes cadastrados são: ')
      
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')
           
    voltar_ao_menu_principal()
    
# Escolher opções via If/Else
# def escolher_opcoes():
#     opcao_escolhida = int(input('Escolha uma opção: '))

#     if opcao_escolhida == 1:
#         print('Cadastrar restaurante')
#     elif opcao_escolhida == 2:
#         print('Listar restaurantes')
#     elif opcao_escolhida == 3:
#         print('Ativar restaurante')
#     elif opcao_escolhida == 4:
#         finalizar_app())
#     else:
#         opcao_invalida()
    
    
#Escolher opções via Match Case   
def escolher_opcoes():   
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))        
        match opcao_escolhida:
            case 1:
                print('Cadastrar restaurante')
                cadastrar_novo_restaurante()
            case 2:
                print('Listar restaurantes')
                listar_restaurantes()
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()