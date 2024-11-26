conta_normal = False        #colocar True / false (para reconhecer o tipo de conta)
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450


if conta_normal:
    if saldo>= saque:
        print("Saque realizado com sucesso! ")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque! ")
elif conta_universitaria:
    if saldo >= saque:
        print ("Saque realizado com Sucesso!")
    else:
        print("Saldo insuficiente!!")
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com seu Gerente!" )