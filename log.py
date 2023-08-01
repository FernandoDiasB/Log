import stdiomask
from os import system
from time import sleep

# MENU

def menu():
    print(''' Bem vindo(a) 
          Digite: 
          [C] para cadastro 
          [L] para Loguin 
          [E] para editar 
          [S] para sair''')
    opcao = input('Digite a opção desejada: ').upper()
    return opcao

def fazerLogin():
    login = input('Digite seu login: ')
    senha = stdiomask.getpass('Digite a senha: ', mask='*')
    return (login, senha)

def verificarUsuario(login, senha):
    usuario = []
    try:
        with open('cadastrados.txt', 'r+', encoding='Utf-8', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(",")
                usuario.append(linha.split())

            for usuarios in usuario:
                nome = usuarios[0]
                password = usuario[1]
                if login == nome and senha == password:
                    return True
    except FileNotFoundError:
        return False


while True:
    system('cls')
    opcao = menu()

    if opcao == 'C':
        login, senha = fazerLogin()

        if login == senha:
            print('Loguin e senha devem ser diferentes.')
            sleep(3)
            continue
        if len(login) < 1:
            print('Voce precisa digitar alguma coisa')
            sleep(3)
            continue
        if len(senha) < 1:
            print('Voce precisa digitar alguma coisa')
            sleep(3)
            continue

        user = verificarUsuario(login, senha)
        if user == True:
            print('Esse usuário já existe')
            sleep(2)
            continue
        
        

        else:
            with open('cadastrados.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                arquivo.writelines(f'{login} {senha}\n')
            print('Registro efetuado com sucesso.')
            sleep(2)
            break

