idade = int(input('Informe sua idade: '))
if idade < 18:
    print('R$ 20,00')
else:
    sexo = input('Informe o sexo M/F: ').upper()
    if idade >= 65:
        if sexo == 'F':
            print('R$ 13,50')
        else:
            print('R$ 15,00')
    else:
        if sexo == 'F':
            print('R$ 36,00')
        else:
            print('R$ 40,00')

#Solução alternativa
print('Solução alternativa')

if idade < 18:
   print('R$ 20,00')
elif idade >= 65 and sexo == 'F':
    print('R$ 13,50')
elif idade >= 65 and sexo == 'M':
    print('R$ 15,00')
elif idade >= 18 and sexo == 'F':
    print('R$ 36,00')
else:
    print('R$ 40,00')
