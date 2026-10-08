from datetime import datetime

LIMITE_POR_SAQUE = 500.00
MAX_SAQUES_DIA = 3

contas = []  # cada conta é um dicionário


def linha():
    print('-=' * 20)


def moeda(valor):
    return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def ler_valor(msg):
    """Pede um valor positivo e repete até o usuário digitar certo."""
    while True:
        try:
            valor = float(input(msg).strip().replace(',', '.'))
        except ValueError:
            print('ERRO! Digite um número válido.')
            continue
        if valor <= 0:
            print('ERRO! O valor deve ser maior que zero.')
            continue
        return valor


def ler_cpf():
    while True:
        cpf = input('CPF (só números): ').strip()
        if len(cpf) == 11 and cpf.isdigit():
            return cpf
        print('ERRO! O CPF deve ter exatamente 11 números.')


def buscar_conta(cpf):
    for conta in contas:
        if conta['cpf'] == cpf:
            return conta
    return None


def registrar(conta, tipo, valor):
    agora = datetime.now().strftime('%d/%m/%Y %H:%M')
    conta['extrato'].append(f'{agora}  {tipo:<15} {moeda(valor):>15}')


def criar_conta():
    linha()
    print('NOVA CONTA')
    cpf = ler_cpf()
    if buscar_conta(cpf):
        print('ERRO! Já existe uma conta com esse CPF.')
        return
    nome = input('Nome completo: ').strip().title()
    if not nome:
        print('ERRO! O nome não pode ficar vazio.')
        return
    conta = {
        'numero': len(contas) + 1,
        'nome': nome,
        'cpf': cpf,
        'saldo': 0.0,
        'saques_hoje': 0,
        'extrato': [],
    }
    contas.append(conta)
    print(f'Conta {conta["numero"]} criada para {nome}!')


def pedir_conta():
    """Pede o CPF e devolve a conta, ou None se não existir."""
    conta = buscar_conta(ler_cpf())
    if conta is None:
        print('ERRO! Conta não encontrada.')
    return conta


def depositar():
    linha()
    print('DEPÓSITO')
    conta = pedir_conta()
    if conta is None:
        return
    valor = ler_valor('Valor do depósito: R$ ')
    conta['saldo'] += valor
    registrar(conta, 'Depósito', valor)
    print(f'Depósito realizado! Saldo: {moeda(conta["saldo"])}')


def sacar():
    linha()
    print('SAQUE')
    conta = pedir_conta()
    if conta is None:
        return
    if conta['saques_hoje'] >= MAX_SAQUES_DIA:
        print(f'ERRO! Limite de {MAX_SAQUES_DIA} saques diários atingido.')
        return
    valor = ler_valor('Valor do saque: R$ ')
    if valor > LIMITE_POR_SAQUE:
        print(f'ERRO! O limite por saque é {moeda(LIMITE_POR_SAQUE)}.')
    elif valor > conta['saldo']:
        print(f'ERRO! Saldo insuficiente. Saldo atual: {moeda(conta["saldo"])}')
    else:
        conta['saldo'] -= valor
        conta['saques_hoje'] += 1
        registrar(  conta, 'Saque', valor)
        print(f'Saque realizado! Saldo: {moeda(conta["saldo"])}')


def transferir():
    linha()
    print('TRANSFERÊNCIA')
    print('Conta de ORIGEM')
    origem = pedir_conta()
    if origem is None:
        return
    print('Conta de DESTINO')
    destino = pedir_conta()
    if destino is None:
        return
    if origem is destino:
        print('ERRO! Origem e destino são a mesma conta.')
        return
    valor = ler_valor('Valor da transferência: R$ ')
    if valor > origem['saldo']:
        print(f'ERRO! Saldo insuficiente. Saldo atual: {moeda(origem["saldo"])}')
        return
    origem['saldo'] -= valor
    destino['saldo'] += valor
    registrar(origem, f'Transf. p/ {destino["numero"]}', valor)
    registrar(destino, f'Transf. de {origem["numero"]}', valor)
    print('Transferência realizada!')


def mostrar_extrato():
    linha()
    print('EXTRATO')
    conta = pedir_conta()
    if conta is None:
        return
    linha()
    print(f'Titular: {conta["nome"]}  |  Conta: {conta["numero"]}')
    linha()
    if not conta['extrato']:
        print('Nenhuma movimentação.')
    else:
        for item in conta['extrato']:
            print(item)
    linha()
    print(f'Saldo atual: {moeda(conta["saldo"])}')


def menu():
    linha()
    print('        BANCO PYTHON')
    linha()
    print('[1] Criar conta')
    print('[2] Depositar')
    print('[3] Sacar')
    print('[4] Transferir')
    print('[5] Extrato')
    print('[0] Sair')
    return input('Escolha uma opção: ').strip()


def main():
    acoes = {
        '1': criar_conta,
        '2': depositar,
        '3': sacar,
        '4': transferir,
        '5': mostrar_extrato,
    }
    while True:
        opcao = menu()
        if opcao == '0':
            print('Obrigado por usar o Banco Python. Até logo!')
            break
        if opcao in acoes:
            acoes[opcao]()
        else:
            print('ERRO! Opção inválida.')


main()