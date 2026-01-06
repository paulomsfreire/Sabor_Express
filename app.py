import os

restaurantes = ['ABC','XYZ']
#restaurantes = [{nome:'ABC', ativo:False},{nome:'XYZ',ativo:True}]

def exibir_nome_do_programa():
    

    '''
    print("""Sabor Express
      
      """)
    '''  
    

    print('''
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯''')

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print('2. Listar restaurantes')
    print('3. Localizar restaurante')
    print('4. Sair\n')


# opcao_escolhida = int(opcao_escolhida)

#print('Você escolheu a opção', opcao_escolhida)

'''
print(f'Você escolheu a opção {opcao_escolhida}!')

print (type(opcao_escolhida))
'''

def exibir_subtitulo(texto):
    os.system('cls')

    linha = '*' * len(texto)

    print(linha)
    print(f'{texto}')
    print(linha)
    print()

def voltar_ao_menu():
    input("\nDigite uma tecla para voltar ao menu principal.")
    main()


def finalizar_app():
    
    exibir_subtitulo('Encerrando o app')

def opcao_invalida():
    print('Opção inválida!\n')

    voltar_ao_menu()

def cadastrar_novo_restaurante():

    '''Essa rotina serve para inserir restaurantes
    
    Inputs:
    - Nome do restaurante
    
    Outputs:
    - Inclui o restaurante na lista'''
    
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado\n')    
    
    voltar_ao_menu()

def listar_restaurantes_for():

     exibir_subtitulo('Lista de restaurantes')

     for restaurante in restaurantes:        
        print(f'. {restaurante}')

     voltar_ao_menu()

def listar_restaurantes_while():

     exibir_subtitulo('Lista de restaurantes')

     indice = 0
     while indice < len(restaurantes):        
        print(f'. {restaurantes[indice]}')
        indice += 1

     voltar_ao_menu()    
    
def localizar_restaurante():
     exibir_subtitulo('Localizar restaurante')

     nome_restaurante = input('Nome do restaurante a ser localizado: ')

     restaurante_encontrado = False

     for restaurante in restaurantes:
         if nome_restaurante.capitalize() == restaurante.capitalize():
             restaurante_encontrado = True
             break

     '''
     if restaurante_encontrado:
         print('Restaurante existente\n')
     else:
         print('Restaurante inexistente\n')
    '''
     
     print('Restaurante existente\n') if restaurante_encontrado else print('Restaurante inexistente\n')


     voltar_ao_menu()




def escolher_opcao_if():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))    

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            #listar_restaurantes_for()
            listar_restaurantes_while()
        elif opcao_escolhida == 3:
            localizar_retaurante()
        elif opcao_escolhida == 4:
            finalizar_app()   
        else:
            opcao_invalida()
    except:
         opcao_invalida()



def escolher_opcao_match():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                #listar_restaurantes_for()
                listar_restaurantes_while()
            case 3:
                localizar_restaurante()
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
    #escolher_opcao_if()
    escolher_opcao_match()
    

if __name__ == '__main__':
    main()