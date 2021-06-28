import random

vNumeroImaginado = random.randint(1,100)
for vChance in range(1,11):
    vChute = int(input('Entre com seu {}º chute: '.format(vChance)))
    if vChute == vNumeroImaginado:
        print("Você acertou!! e usou ", vChance, " tentativa(s)")
        break
    else:
        if  vChute > vNumeroImaginado:
            print("Seu chute foi alto")
        else:
            print("Seu chute foi baixo")
if vChance >= 10:
   print("Você não acertou com as 10 chances")
else:
   print("Parabéns")