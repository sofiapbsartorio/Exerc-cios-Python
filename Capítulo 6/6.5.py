alunos_notas = {}
num_alunos = int(input("Quantos alunos? "))
for i in range(num_alunos):
    nome = input(f"Informe o nome do aluno {i+1}: ")
    nota = float(input(f"Informe a nota do aluno {i+1}: "))
    alunos_notas[nome] = nota
alunos_aprovados = {nome: nota for nome, nota in alunos_notas.items() if nota >= 7}
print("\nAlunos aprovados:")
for nome, nota in alunos_aprovados.items():
    print(f"{nome}: {nota}")
