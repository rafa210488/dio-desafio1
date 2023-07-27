menu = '''
Bem vindo, qual serviço gostaria de utilizar?
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>'''

saldo = 0
limite = 500
extrato = ''
total_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == '1':
        print('Depósito')
        valor_deposito = float(input('Digite o valor desejado para depósito: R$ '))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'Depósito : R$ {valor_deposito:.2f}\n'
            print(f'Você depositou R$ {valor_deposito:.2f}')
        else:
            print('Valor para depósito inválido, por favor digite um valor válido para realizar o Depósito.')
    
    elif opcao == '2':
        print('Saque')
        valor_saque = float(input('Digite o valor desejado para Saque: R$'))
        
        if valor_saque > saldo:
            print('Saldo indisponível para realizar um saque.')
        elif valor_saque > limite:
            print('Valor acima do limite de saque.')
        elif total_saques >= LIMITE_SAQUES:
            print('Limite diário de saques foi atingido. Caso deseje realizar outro saque, volte amanhã.')
        elif valor_saque > 0 and valor_saque <= limite:  
            saldo -= valor_saque
            total_saques += 1
            extrato += f'Saque: R$ {valor_saque:.2f}\n'
            print(f'Você fez um saque de R$ {valor_saque:.2f}')
        else:
            print('ERRO, valor de saque inválido.')
                    
    elif opcao == '3':
        print('Extrato')
        print('-=' * 30)
        print('Sem movimentações no momento' if not extrato else extrato)
        print('-=' * 30)
        print(f'Saldo Total: R$ {saldo:.2f}')
        
    
    elif opcao == '4':
        print('Saindo')
        break
    
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada!.') 
print('Obrigado por utilizar nossos serviços. Volte Sempre!')     
        
