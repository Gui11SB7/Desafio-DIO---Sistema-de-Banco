menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito (utilize ponto para separar reais dos centavos): "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Erro: O valor informado é inválido.")
    
    elif opcao == "2":
        valor = float(input("Informe o valor do saque (utilize ponto para separar reais dos centavos): "))

        if valor > saldo:
            print("Erro: Você não tem saldo suficiente para realizar essa operação.")
        elif valor > limite:
            print("Erro: O valor excede o limite diário de R$ 500.00")
        elif numero_saques >= LIMITE_SAQUES:
            print("Erro: O limite de saques diários foi atingido.")
        elif valor <= 0:
            print("Erro: O valor informado é inválido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")