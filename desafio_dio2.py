import textwrap

def menu():
    menu = '''\n
    --------------- MENU ---------------
    [d]\tDeposita
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [nu]\tNovo usuario
    [lc]\tListar contas
    [o]\tSair
     =>   '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print('\n=== Depósito realizado com sucesso! ===')
    else:
        print('\n@@@ Operção falhou! valor informado invalido. @@@')
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, num_saq, limite_saq):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = num_saq >= limite_saq

    if excedeu_saldo:
        print('\n@@@ Operação falhou! Sem saldo suficiente. @@@')
    elif excedeu_limite:
        print('\n@@@ Operação falhou! Valor ultrapassa o limite. @@@')
    elif excedeu_saques:
        print('\n@@@ Operação falhou! Limite de saques excedido. @@@')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\nR$ {valor:.2f}\n'
        num_saq += 1
        print('\n ::: Saque realizado com sucesso. :::')

    else:
        print('@@@ Operação falhou! Valor informado é invalido. @@@')
    
    return saldo, extrato 

def exibir_extrato(saldo, /, *, extrato):
    print('\n============Extrato============')
    print('Não foram realizadas movimentações.' if not extrato else extrato)   
    print(f'\nSaldo:\t\nR$ {saldo:.2f}')
    print('=================================')

def criar_usuario(usuarios):
    cpf = input('Insira seu cpf (somente o número): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n@@@ Já existe usário com este CPF! @@@')
        return
    nome = input('Digite seu nome completo: ')
    data_nasc = input('Digite sua data de nascimento (dd/mm/aaaa): ')
    endereco = input('Digite seu endereço(logradouro, nro - bairro - cidade estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nasc, 'cpf': cpf, 'endereco': endereco})

    print('=== Usuário criado com sucesso!! ====')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n=== Conta criada com sucesso! ===')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('\n@@@ Usuario não encontrado, fluxo de criação de conta encerrada!! @@@')

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('=' * 100)
        print(linha)


def main():
    limite_saq = 3
    agencia = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    num_saq = 0 
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Digite o valo a ser sacado: '))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saq=num_saq,
                limite_saq=limite_saq,        
            )
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao =='nu':
            criar_usuario(usuarios)
        
        elif opcao == 'nc':
            numero_conta = len (contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'o':
            break

        else:
            print('Operação inválida, por facor selecione novamnete a operação desejada.')


main()