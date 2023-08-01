saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = '0001'
clientes = []
contas = []

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
        
    if valor > saldo:
        print('Saldo indisponível para realizar um saque.')
    elif valor > limite:
        print('Valor acima do limite de saque.')
    elif numero_saques >= limite_saques:
        print('Limite diário de saques foi atingido. Caso deseje realizar outro saque, volte amanhã.')
    elif valor > 0 and valor <= limite:  
        saldo -= valor
        numero_saques += 1
        extrato += f'Saque: R$ {valor:.2f}\n'
        print(f'Você fez um saque de R$ {valor:.2f}')
    else:
        print('ERRO, valor de saque inválido.')
    
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):
    
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f'Depósito : R$ {valor_deposito:.2f}\n'
        print(f'Você depositou R$ {valor_deposito:.2f}')
    else:
        print('Valor para depósito inválido, por favor digite um valor válido para realizar o Depósito.')
    
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print('Extrato')
    print('-=' * 30)
    print('Sem movimentações no momento' if not extrato else extrato)
    print('-=' * 30)
    print(f'Saldo Total: R$ {saldo:.2f}')

def verificar_cliente(cpf, clientes):
    clientes_verificados = [cliente for cliente in clientes if cliente['cpf'] == cpf]
    return clientes_verificados[0] if clientes_verificados else None

def criar_cliente(clientes):
    cpf = input('Informe o CPF do cliente a ser cadastrado (Somente números): ')
    cliente = verificar_cliente(cpf, clientes)
    
    if cliente in clientes:
        print('Cliente já correntista do nosso Banco!')
        return
         
    
    nome = input('Informe o nome completo do cliente: ')
    data_nascimento = input('Informe a data de nascimento do cliente (dd/mm/aaaa): ')
    endereco = input('Informe o endereço do cliente (logradouro, numero / bairro / cidade-sigla estado): ')
    
    clientes.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereço': endereco})
    print('Cliente cadastrado com sucesso. Obrigado por escolher nosso Banco!')

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Digite o cpf do cliente desejado (Somente números): ')
    cliente = verificar_cliente(cpf, clientes)
    
    if cliente in clientes:
        print('Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'cliente': cliente}

    print('Cliente não encontrado, favor cadastrar o cliente antes da criação da conta')

def mostrar_contas(contas):
    print('-=' * 30)
    for conta in contas:
        print(f"""Agência: {conta['agencia']}\n
              C/C: {conta['numero_conta']}\n
              Cliente: {conta['cliente']['nome']}""")    
    
menu = '''
Bem vindo, qual serviço gostaria de utilizar?
[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Cliente
[5] Cadastrar Conta
[6] Mostrar Contas
[e] Sair

=>'''

while True:
    
    opcao = input(menu)
    
    if opcao == '1':
        print('Depósito')
        valor_deposito = float(input('Digite o valor desejado para depósito: R$ '))
        
        saldo, extrato = depositar(saldo, valor_deposito, extrato)
    
    elif opcao == '2':
        print('Saque')
        valor_saque = float(input('Digite o valor desejado para Saque: R$'))
        saldo, extrato, numero_saques = saque(
            saldo=saldo,
            valor=valor_saque,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES )
                        
    elif opcao == '3':
        mostrar_extrato(saldo, extrato=extrato)
    
    elif opcao == '4':
        criar_cliente(clientes)
            
    elif opcao == '5':
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, clientes)
        
        if conta not in contas:
            contas.append(conta)
        
    elif opcao == '6':
        mostrar_contas(contas)  
          
    elif opcao == 'e':
        print('Saindo')
        break
    
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada!.') 
print('Obrigado por utilizar nossos serviços. Volte Sempre!')     
