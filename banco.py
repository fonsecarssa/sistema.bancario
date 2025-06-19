#contém 4 operações: deposito, saque, extrato e cadastro de usuário


transacoes = list()
saldo = 0
limite = 500.00
saques_diarios = 0


#menu do banco
def menu():
    print('''
        --------------------------------------------
                    Banco Python
        --------------------------------------------
        ''')
    print('''
        --------------------------------------------
                    [1] Depositar
                    [2] Sacar
                    [3] Extrato
                    [4] Criar Usuário
                    [5] Sair
        --------------------------------------------
    ''')   
    return (input('''
        --------------------------------------------                
                Digite uma opção: 
        --------------------------------------------          
                '''))


#deposito
#deposito: adiciona o valor ao saldo, se o valor for positivo
#todos os depositos devem ser armazenados numa variavel e exibido na opção de extrato
def depositar():
    global saldo
    print('''
        --------------------------------------------
                        Deposito:
        --------------------------------------------
        ''')
    
    valor_deposito = input('Digite o valor do deposito:')
    if valor_deposito.replace('.', '', 1).isdigit()  and float(valor_deposito) > 0:
        valor_deposito = float(valor_deposito)
        #adiciona o valor do deposito ao saldo
        saldo += valor_deposito
        transacoes.append(f'\nDepósito: R$ {valor_deposito:.2f}')
        print(f'''
    -------------------------------------------------------
    Deposito de {valor_deposito:.2f} realizado com sucesso!
          
    Saldo atual: R$ {saldo:.2f}
    -------------------------------------------------------
            ''')
    else:
        print('ERRO: O valor do deposito deve ser positivo')

#todos os saques devem ser armazenados numa variavel e exibido na opção de extrato
#se o usuario tentar sacar um valor maior que o saldo, deve ser exibida uma mensagem de erro
#se o usuario tentar sacar um valor maior que o limite, deve ser exibida uma mensagem de erro
#saque: retira o valor do saldo, se houver saldo suficiente
#se o usuario tentar sacar um valor maior que o limite, deve ser exibida uma mensagem de erro
#se o usuario nao tiver saldo na conta, deve ser exibida uma mensagem de erro
def saque():
    global saldo, saques_diarios
    print('''
        --------------------------------------------
                    Saque:
        --------------------------------------------
        ''')

    print(f'Saldo atual: R$ {saldo:.2f}')

    valor_saque = input('Digite o valor do saque: ')

    if valor_saque.replace('.', '', 1).isdigit():
        valor_saque = float(valor_saque)

        if valor_saque > saldo:
            print('ERRO: Saldo insuficiente')
        elif valor_saque > limite:
            print('ERRO: Limite de saque excedido')
        elif saques_diarios >= 3:
            print('ERRO: Limite de saques diários excedido')
        else:
            saldo -= valor_saque
            saques_diarios += 1
            transacoes.append(f'\nSaque: R$ {valor_saque:.2f}')
            print(f'''
        ----------------------------------------------------            
            Saque de {valor_saque:.2f} realizado com sucesso!                 
        -----------------------------------------------------
                ''')
    else:
        print('ERRO: O valor do saque deve ser um número positivo')        
    
#o extrato deve listar todos os depositos e saques realizados na conta, e no final mostra o saldo atual da conta
#todos os saques devem ser armazenados numa variavel e exibido na opção de extrato
#extrato: mostra o saldo atual e as transações realizadas

def extrato():
    global saldo, saques_diarios
    print('''
        --------------------------------------------
                        Extrato:
        --------------------------------------------
    ''')
    if len(transacoes) == 0:
        print('''
        --------------------------------------------
            Nenhuma transação realizada.
        ---------------------------------------------
            ''')
    else:
        for i in (transacoes):
            print(i)
        print(f'''
        -----------------------------------------------
                    Extrato do dia:
              
            => Total de depósitos: {len([i for i in transacoes if 'Depósito' in i])}
            => Total de saques: {saques_diarios}
            => Saldo atual: R$ {saldo:.2f}
        ------------------------------------------------
            ''') 

usuarios = list()  
def criarusuario():
    print('''
    --------------------------------------------
                Cadastro de Usuário:
    --------------------------------------------''')

    cpf = int(input('Informe seu CPF (Somente números): '))

    usuario_existente = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    if usuario_existente:
        print("Erro: Já existe um usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ").strip()
    nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ").strip()

    usuarios.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário cadastrado com sucesso!")

#loop principal do programa

while True:
    opcao = menu()
    if opcao == "1":
        depositar()
    elif opcao == "2":
        saque()
    elif opcao == "3":
        extrato()
    elif opcao == "4":
        criarusuario()       
    elif opcao == "5":
        print('''
        --------------------------------------------
                    Saindo do sistema...
        --------------------------------------------''')
        break
    else:
        print('Opção inválida! Tente novamente.')

print(''' 
        --------------------------------------------
                    Volte sempre!
        --------------------------------------------''')


    


