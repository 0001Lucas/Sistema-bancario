Menu = '''
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair
'''

Saldo = 500
LIMITE_SAQUE_DIARIO = 3
Limite = 500
Numero_Saques = 0
Extrato = ''

def teste():
    print(Extrato)


while True:
    Opção = input(Menu)
    if Opção == 'D':
        print('Depósito')
        Valor_Deposito = float(input('Digite o valor do depósito:'))

        if Valor_Deposito > 0:
            print('Depósito de {:.2f}R$ efetuado com sucesso!'.format((Valor_Deposito)))
            Saldo += Valor_Deposito
            Extrato += 'Depósito de {:.2f}R$\n'.format(Valor_Deposito)
            teste()

        else:
            print('Valor de depósito invalido!')

    elif Opção == 'S':
        print('Saque')
        if LIMITE_SAQUE_DIARIO > 0:
            Valor_Saque = float(input('Qual o valor do saque ?'))
            if Valor_Saque <= 500 and Saldo >= Valor_Saque:
                Confirmação_Saque = input('Confirma o saque no valor de {}R$ ?[S/N]'.format(Valor_Saque))
            else:
                print('Saldo insuficiente!')
            if Confirmação_Saque == 'S':
                print('Saque de {}R$ realizado!'.format(Valor_Saque))
                Saldo -= Valor_Saque
                LIMITE_SAQUE_DIARIO -= 1
                Numero_Saques += 1
                Registro_Saques.insert(Cont2, Valor_Saque)

    elif Opção == 'E':
        print('Extrato')
        for c in range(len(Registro_Depósitos)):
            print('{}'.format(Registro))

    elif Opção == 'Q':
        print('Sair')
        break

    else:
        print('Opção Inválida')