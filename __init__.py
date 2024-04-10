from os import system
from platform import system as platform_system
from time import sleep

# Opções que o usuario pode escolher como resposta
OPCOES = {
    'ALTERE': ['ALTERAR', 'ALTERAR O NOME', 'ALTERAR NOME', '1', '[1]', 'ALTERE'],
    'CONFIRME': ['CONFIRMAR NOVAMENTE', 'CONFIRMAR', 'CONFIRME', 'NOVAMENTE', '2', '[2]'],
    'CADASTRAR' : ['[1]', '1', 'CADASTRAR', 'CADASTRAR NOVO', 'CADASTRAR NOVO PROFISSIONAL'],
    'EDITAR' : ['[2]', '2', 'EDITAR', 'EDITAR INFORMAÇÕES', 'EDITAR INFORMACOES', 'EDITAR INFORMAÇOES', 'EDITAR INFORMACÕES']
}

YES_OPTIONS = {'SIM', 'YES'}
NO_OPTIONS = {'NÃO', 'NAO', 'NO'}

# Função responsável por identificar sistema operacional
def which_system():
    sistema = platform_system()
    if sistema == "Windows":
        return "Windows"
    elif sistema == "Darwin":
        return "Mac"
    elif sistema == "Linux":
        return "Linux"
    else:
        return "Sistema não identificado"

# Função responsável por verificar qual o sistema e colocar  comando da biblioteca os compativel
def clear():
    sistema = which_system()
    if sistema == 'Windows':
        return system('cls')
    elif sistema == 'Linux' or sistema == 'Mac':
        return system('clear')

# Função para saber se o usuário quer cadastrar novo profissional ou alterar alguma informação do profissional que já existe
def where_to():
    while True:
        opcao_where_to = str(input('[1] Cadastrar novo profissional\n[2] Editar informações\n\n--> ')).upper().strip()
        if opcao_where_to in OPCOES['CADASTRAR']:
            return True
        elif opcao_where_to in OPCOES['EDITAR']:
            return False
        else:
            clear()
            print('Invalido. Digite novamente.\n')

# Função para saber o que o usuario quer fazer após digitar não para confirmar profissional
def do_what():
    opcao_who = str(input('''O que você quer fazer?
                          
[1] Alterar nome
[2] Confirmar novamente\n\n--> ''')).upper().strip()

    if opcao_who in OPCOES['ALTERE']:
        return 'ALTERE'
    elif opcao_who in OPCOES['CONFIRME']:
        return 'CONFIRME'
    else:
        return 'NOVAMENTE'

# Função para obter a confirmação do usuário
def get_confirmation(name):
    while True:
        clear()
        confirmation = str(input(f'Você confirma o nome do profissional como "{name}"? (SIM/NÃO)\n--> ')).upper().strip()

        if confirmation in YES_OPTIONS:
            return True
        elif confirmation in NO_OPTIONS:
            return False
        else:
            print("Por favor, responda com 'sim' ou 'não'.")
            sleep(1.5)
            input('Pressione <enter>')

# Função para verificar se o nome está com mais de uma palavra
def LastName_RIGHT(name_complete):
    cutting = str(name_complete).split()
    if len(cutting) <= 1:
        return False
    elif len(cutting) > 1:
        return True

# Função principal do programa
def main():
    input('Pressione <enter> para iniciar.')
    clear()

    EXECUTE_WHERETO = where_to()
    if EXECUTE_WHERETO == True:
        while True:
            clear()
            name = str(input('Qual o nome COMPLETO do profissional que deseja cadastrar?\n--> ')).title().strip()
            verify_name = LastName_RIGHT(name)
            name_number = len(str(name).split())

            if not verify_name:
                if name_number < 1:
                    print('Inválido')
                    sleep(1)
                    continue
                else:
                    clear()
                    print(f'O nome {name} não pode conter apenas uma palavra, digite o nome completo.')
                    sleep(1.5)
                    input('Pressione <enter>')
                    continue


            while True:
                confirmation = get_confirmation(name)

                if confirmation:
                    clear()
                    print(f'Profissional: {name}')
                    name = name.upper
                else:
                    action = do_what()
                    if action == 'ALTERE':
                        break
                    elif action == 'CONFIRME':
                        continue
                    elif action == 'NOVAMENTE':
                        continue 
# Execução do programa
if __name__ == "__main__":
    main()
