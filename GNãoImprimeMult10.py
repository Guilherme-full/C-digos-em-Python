fim = int(input("DIGITE O ÚLTIMO NÚMERO A IMPRIMIR: "))
x = 1
while x <= fim:
     if x % 2 == 0 and x % 10 != 0:
         print('\033[1;31m', x)
     x = x + 1