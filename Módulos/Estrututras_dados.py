# Listas

notas_alunos = [10, 7, 8, 5, 6, 8]

notas_alunos.append(27)
notas_alunos.append(57)
notas_alunos.pop(57)

print(notas_alunos(1)) # 7


# Exemplos

notas = []

while True:
    nota_aluno = int(input('Digite a nota do aluno ou -1 para sair: '))
    if nota_aluno == -1:
        break
    
    notas.append(nota_aluno)


soma = 0
qtd = 0
for i in notas:
    soma = soma + i
    qtd = qtd + 1
print(soma/qtd)

# Dicionários

pessoa = {'nome': 'Matheus', 'altura': '187', 'idade': 17}

pessoa['idade'] = '18'

print(pessoa) # 'Matheus', '187', '18' 

print(pessoa['nome']) # 'Matheus'
print(pessoa['altura']) # '187'