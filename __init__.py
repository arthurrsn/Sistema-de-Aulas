# Opções que o usuario pode escolher como resposta
OPCOES = {
    'ALTERE': ['ALTERAR', 'ALTERAR O NOME', 'ALTERAR NOME', '1', '[1]', 'ALTERE'],
    'CONFIRME': ['CONFIRMAR NOVAMENTE', 'CONFIRMAR', 'CONFIRME', 'NOVAMENTE', '2', '[2]'],
    'CADASTRAR' : ['[1]', '1', 'CADASTRAR', 'CADASTRAR NOVO', 'CADASTRAR NOVO PROFISSIONAL'],
    'EDITAR' : ['[2]', '2', 'EDITAR', 'EDITAR INFORMAÇÕES', 'EDITAR INFORMACOES', 'EDITAR INFORMAÇOES', 'EDITAR INFORMACÕES']
}

YES_OPTIONS = {'SIM', 'YES'}
NO_OPTIONS = {'NÃO', 'NAO', 'NO'}

# Função para saber se o usuário quer cadastrar novo profissional ou alterar alguma informação do profissional que já existe
def where_to():
    while True:
        opcao_where_to = str(input('[1] Cadastrar novo profissional\n[2] Editar informações\n\n--> ')).upper().strip()
        if opcao_where_to in OPCOES['CADASTRAR']:
            return True
        elif opcao_where_to in OPCOES['EDITAR']:
            return False
        else:
            print('Invalido. Digite novamente.')

# Função para saber o que o usuario quer fazer após digitar não para confirmar profissional
def do_what():
    opcao_who = str(input('''O que você quer fazer?
    [1] Alterar nome
    [2] Confirmar novamente\n''')).upper().strip()

    if opcao_who in OPCOES['ALTERE']:
        return 'ALTERE'
    elif opcao_who in OPCOES['CONFIRME']:
        return 'CONFIRME'
    else:
        return 'NOVAMENTE'

# Função para obter a confirmação do usuário
def get_confirmation(name):
    while True:
        confirmation = str(input(f'Você confirma o nome do profissional como "{name}"? (SIM/NÃO)\n')).upper().strip()

        if confirmation in YES_OPTIONS:
            return True
        elif confirmation in NO_OPTIONS:
            return False
        else:
            print("Por favor, responda com 'sim' ou 'não'.")

# Função principal do programa
def main():
    input('Pressione <enter> para iniciar.')

    EXECUTE_WHERETO = where_to()
    if EXECUTE_WHERETO == True:
        while True:
            name = str(input('Qual o nome do profissional que deseja cadastrar?\n--> ')).title().strip()
            
            while True:
                confirmation = get_confirmation(name)

                if confirmation:
                    print(f'Profissional: {name}')
                    name = name.upper
                    break
                else:
                    action = do_what()
                    if action == 'ALTERE':
                        break

# Execução do programa
if __name__ == "__main__":
    main()
