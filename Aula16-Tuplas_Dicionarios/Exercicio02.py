# Construa um algoritmo que peça ao usuário para informar 
# o nome, a nota01 e a nota02 de um aluno. Guarde estas 
# informações em um dicionário. Após, calcule a nota final 
# deste aluno [(nota01 + nota02) /2] e adicione ao 
# dicionário. Ao final, imprima todos os dados do dicionário.

nome = input("Digite seu nome: ")
n1 = float( input("Digite sua primeira nota: ") )
n2 = float( input("Digite sua segunda nota: ") )
aluno = {
    "nome" : nome ,
    "nota01" : n1 ,
    "nota02" : n2
}
nf = (n1 + n2) / 2
aluno["notaFinal"] = nf
print( aluno )