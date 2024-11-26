MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Informe sua idade: "))

if idade >= 18 :
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar CNH.")



if idade >= MAIOR_IDADE:   # com o if / else
    print("Maior de idade, pode tirar a CNH.")
else:
    print ("Ainda não pode tirar CNH.")




if idade >= MAIOR_IDADE:   # com o if / elif / else
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas praticas")
else:
    print ("Ainda não pode tirar CNH.")