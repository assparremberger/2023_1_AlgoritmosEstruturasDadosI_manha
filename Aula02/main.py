from Pessoa import Pessoa
p1 = Pessoa("João", 30)
#p1.idade = 20
#p1.imprimir()

def imprimirPessoa(p):
    print("Nome: " , p.nome )
    print("Idade: " , p.idade )
    print("Telefone: " , p.fone )

imprimirPessoa( p1 )
