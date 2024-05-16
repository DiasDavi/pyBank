menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if  opcao == "d":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if(valor_deposito > 0):
            saldo += valor_deposito
            extrato += f"Despósito de R${round(valor_deposito,2)} realizado\n"
        else:
            print("Valor invalido")

    elif opcao == "s":
        valor_saque = float(input("Digite o valor a ser sacado: "))
        if valor_saque > saldo:
            print("Saldo insuficiente")
        elif valor_saque < 0:
            print("Valor invalido")
        else:
            if numero_saques < LIMITE_SAQUES:
                if valor_saque < limite:
                    saldo -= valor_saque
                    extrato += f"Saque de R${round(valor_saque,2)} realizado\n"
                    numero_saques += 1
                else:
                    print("Seu limite de saque é de {}".format(limite))
            else:
                print("Você atingiu o limite de saques")

    elif opcao == "e":
        print("{}\n Saldo atual {}".format(extrato, saldo))

    elif opcao == "q":
        break

    else:
        print("Opção inválida")
