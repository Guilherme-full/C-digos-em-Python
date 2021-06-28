pratica = []
prova   = []
faltas  = []
for nota in range(4):
    pratica.append(int(input('Digite a nota da {}º prática     : '.format(nota+1))))
    prova.append(int(input('Digite a nota da {}º prova       : '.format(nota+1))))
    faltas.append(int(input('Digite as faltas do {}º bimestre : '.format(nota+1))))

somaPratica = 0
somaProva   = 0
somaFaltas  = 0
for n in range(4):
    somaPratica = somaPratica + pratica[n]
    somaProva   = somaProva   + prova[n]
    somaFaltas  = somaFaltas  + faltas[n]
mediaPratica = somaPratica / 4
mediaProva   = somaProva   / 4
PercentualFreq = (1 - somaFaltas / 40 )*100

print('Pratica   Prova     Média Geral')
for n in range(4):
    print(f'   {pratica[n]}        {prova[n]}     =    {(pratica[n]+prova[n])/2}')
print('--------------------------------')
mediaGeral = (mediaPratica+mediaProva)/2
print(f' {mediaPratica}      {mediaProva}    =  {mediaGeral}')
print('')
print('Frequência Geral = {}%'.format(PercentualFreq))
print('')
if mediaGeral >= 7 and PercentualFreq >= 75:
    print('Aprovado')
elif mediaGeral >= 5 and PercentualFreq >= 75:
    print('Recuperação')
else:
    print('Reprovado')
