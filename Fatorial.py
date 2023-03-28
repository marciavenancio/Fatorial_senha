minuto_atual = int(input("Informe os minutos atuais: "))
fatorial = 1

for numero in range(1, minuto_atual+1):
    fatorial = fatorial * numero
print("A senha para o desbloqueio é LIBERDADE{}.".format(fatorial))