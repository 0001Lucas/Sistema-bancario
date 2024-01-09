def menu():
    Menu = '''
   [D] Depositar
   [S] Sacar
   [E] Extrato
   [U] Criar Usuario
   [C] Criar conta corrente
   [Q] Sair
   [L] Listar contas
   '''
    return Menu


def Saque(*, Saldo, Extrato, Numero_Saques, LIMITE_SAQUE_DIARIO, Valor_Saque):

    if Valor_Saque <= 500 and Saldo >= Valor_Saque:

        print('Saque de {:.2f}R$ efetuado com sucesso!'.format(Valor_Saque))
        Extrato += ('Saque de {:.2f}R$\n'.format(Valor_Saque))
        LIMITE_SAQUE_DIARIO -= 1
        Saldo -= Valor_Saque
        Numero_Saques += 1

    else:
        print('Saque não realizado!')
    return Saldo, Extrato, Numero_Saques, LIMITE_SAQUE_DIARIO


def Deposito(Saldo, Valor_Deposito, Extrato):

    if Valor_Deposito > 0:
        print('Depósito de {:.2f}R$ efetuado com sucesso!'.format(Valor_Deposito))
        Extrato += 'Depósito de {:.2f}R$\n'.format(Valor_Deposito)
        Saldo += Valor_Deposito

    else:
        print('Valor de depósito invalido!')
    return Saldo, Extrato


def extrato(Saldo, /, *, Extrato):
    print('-------------------Extrato-------------------')
    print(Extrato)
    print('Saldo disponivel: {:.2f}R$'.format(Saldo))


def Criar_Usuario(Usuarios):
    CPF = input('Digite seu CPF: (Somente Numeros!)')

    if filtrar_usuario(CPF, Usuarios):

       print('CPF já cadastrado!')

    else:

       Nome = str(input('Digite seu nome:'))
       Nascimento = input('Digite sua data de nascimento[00/00/0000]: ')
       Rua = str(input('Rua:'))
       Numero_Da_Casa = input('Numero da casa:')
       Bairro = input('Bairro:')
       Cidade = input('Cidade:')
       Endereço = '{}, N°{}, {} - {}'.format(Rua, Numero_Da_Casa, Bairro, Cidade)

       Usuarios.append({'Nome': Nome,'CPF': CPF, 'Nascimento': Nascimento, 'Endereço': Endereço})
       print('Usuario cadastrado com sucesso!')

def filtrar_usuario(CPF, Usuarios):

   filtro = [usuario for usuario in Usuarios if usuario['CPF'] == CPF]
   return filtro[0] if filtro else None

def Criar_Conta(Contas, Usuarios):

    print('Criar nova conta!')
    CPF = input('Digite seu CPF:')

    if filtrar_usuario(CPF, Usuarios):
       print('Conta criada com sucesso!')

       Contas.append({'Conta': len(Contas) + 1, 'Agencia':'0001','CPF':CPF})

    else:
       print('Você não possui cadastro!')

def Listar_Contas(Contas):
   for x in Contas:
      print('Conta: {}, Agência: {}'.format(x['Conta'], x['Agencia']))

Saldo = 0
LIMITE_SAQUE_DIARIO = 3
Numero_Saques = 0
Extrato = ''
Contas = []
Usuarios = [ ]

while True:

    Opção = input(menu()).upper()

    if Opção == 'D':

        Valor_Deposito = float(input('Qual valor você quer depositar ?'))
        Saldo, Extrato = Deposito(Saldo, Valor_Deposito, Extrato)

    elif Opção == 'S':
        Valor_Saque = float(input('Qual o valor do saque ?'))

        if Numero_Saques < 3:

            Saldo, Extrato, Numero_Saques, LIMITE_SAQUE_DIARIO = Saque(
                Saldo=Saldo,
                Extrato=Extrato,
                Numero_Saques=Numero_Saques,
                LIMITE_SAQUE_DIARIO=LIMITE_SAQUE_DIARIO,
                Valor_Saque=Valor_Saque
            )
        else:
            print('Limite de saques diarios atingido!')

    elif Opção == 'E':
        extrato(Saldo, Extrato=Extrato)

    elif Opção == 'U':
        Criar_Usuario(Usuarios)

    elif Opção == 'C':
        Criar_Conta(Contas, Usuarios)

    elif Opção == 'L':
       Listar_Contas(Contas)

    elif Opção == 'Q':
        print('Sair')
        break