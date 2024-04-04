import os

restaurantes = [{'nome':'Ordones', 'categoria':'Bar', 'ativo':False},
                {'nome':'La Pasta', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Yakisobra', 'categoria':'Japones', 'ativo':True}]

def exibir_nome_programa():
    print(""" 
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀\n""")

def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Alternar estado do Restaurante")
    print("4. Sair\n")

def finalizar_app():
    exibir_subtitulo("Encerrando o Programa")

def voltar_ao_menu_principal():
    input("\nDigite alguma tecla para voltar ao menu")
    main()

def opcao_invalida():
    print("Opção Invalida! \n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes")

    print(f'{"Nome do restaurante".ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativo' if restaurante['ativo'] else 'Desativado'
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante['ativo'] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado.")

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opcao: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()
        
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
      main()
    