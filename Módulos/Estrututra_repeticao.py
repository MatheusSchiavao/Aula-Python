# While

i = 0

while i <= 10:
    print('i')
    i = i + 1 # igual a i += 1

print('Fim do código')

# Exemplo com while
decisao = ''

while True:
    decisao = input('Digite a nota de um aluno ou -1 para sair: ')
    if decisao == '-1':
      break
      print(f'A nota do aluno é: {decisao}')

  # Exemplo 2 com while
numero = int(input('Digite um número: '))

i = 0

while i <= 10: 
  print(f'{numero} * {i} = {numero * i}')
  i = i+ 1


# For

numero = int(input('Digite um número: '))

for i in range(0, 11, 2): # Início, Termina, Passo
    print(f'{numero} X {i} = {numero * i}')

    for i in range(11, 0, -1):
      print(i)


# Exemplo com for

for i in range(0, 1001):
   if i % 2 == 0:
      print(i)