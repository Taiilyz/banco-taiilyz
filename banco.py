menu = '''
    BANCO TAIILYZ

[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
'''

saldo = 0
limite = 500.00
extrato = ""
LIMITE_SAQUE = 3
saques_realizados = 0

while (True):

    opcao = input(menu + "\nSelecione uma opção: ")
    
    if opcao == "1":
        valor = float(input("\nInforme valor para depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print ("\nDepósito efetuado com sucesso")
        else:
            print ("\nOperação inválida, valor deve ser maior que zero")
    
    elif opcao == "2":
        if LIMITE_SAQUE <= 0:
            print ("\nOperação inválida, ultrapassou o limite diário de saques")
            continue
        saque = float(input("\nInforme valor de saque: "))
        if saque > saldo:
            print ("\nOperação inválida, saldo insuficiente")
        elif saque > limite:
            print ("\nOperação inválida, valor do saque ultrapassa o limite")
        elif saque <= 0:
            print ("\nOperação inválida, valor deve ser maior que zero")
        else:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            saques_realizados += 1
            LIMITE_SAQUE -= 1
            print ("\nSaque efetuado com sucesso")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================\n")
    
    elif opcao == "4":
        print("\nObrigado por utilizar o Banco Tailyz!")
        break

    else:
        print("\nOperação inválida, por favor selecione uma opção válida")
