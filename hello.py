#nome = input("Qual é seu nome: ")
#print("Seu nome é: " + nome)

#numero1 = int(input("Numero: "))
#numero2= int(input("Numero: "))
#print(numero1 * numero2)

#numero = 15
#if numero == 15:
#    print("VERDADEIRO")

lista = [0,1,2,3]
print(lista)
""" lista.append(4) 
print(lista) """
numeroRetirado = lista.pop(1)
print(numeroRetirado)
print(lista)
lista.insert(0,"Douglas")
print(lista)

#pos = lista.index('DOUGLAS')
#print(pos)

# TUPLAS
""" tupla = ("Douglas", "João",[1, 2, 3])
print(tupla)
pos = tupla.index("João")
print(pos)
pessoa = "Maria"
tupla = pessoa
print(tupla)  """

# CONJUTNOS
""" conjunto = {"Diego", "João", "Maria"}
conjunto2 = {"Diego", "Fulano"}
print(conjunto.difference(conjunto2))  """

# Dicionário
""" dic = {
    "nome1": "Diego",
    "nome2": "João",
    "nome3": "Maria",
}

for chave, valor in dic.items():
    print(chave, valor) """

# String - manipulação
""" nome = "Diego"
nome1 = "diego"
nome2 = "DIEGO"
sobrenome = "Araujo"
nome_completo = "Diego araujo"
name = nome_completo.split()
nome_mudado = nome_completo.replace("Diego", "João")

print('meu nome é: ', nome)
print('meu nome é ' + nome)
print('meu ome completo é: %s %s' %(nome, sobrenome))
print(f'meu nome é: {nome} {sobrenome}') 

print(nome1.upper())
print(nome2.lower())
print(sobrenome.lower().count('a'))

print(name[1])
print(nome_mudado) 
print(nome.find('o'))

 """


#Exercicio
""" 
lista = []
dic = {}
nome = "Diego"
idade = 18
email = "diego@example.com"

lista.append(nome)
lista.append(idade)
lista.append(email)
dic['info'] = lista

print(dic) """

#and, or e not
""" 
and = verdadeiro e verdadeiro = verdade
and = verdadeiro e falso = falso
and = falso e verdadeiro = falso
and = falso e falso = falso

or = verdadeiro ou verdadeiro = verdade
or = verdadeiro ou falso = verdade
or = falso ou verdadeiro = verdade
or = falso ou falso = falso

not = não verdadeiro = falso
not = não falso = verdade """

#prática if elif e else (and or not)
""" if not "a" == "b" and "c" == "c":
    print("verdade") """

""" nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2)/2

if media >= 6 and media <=10:
    print(f"aprovado com nota final {media}")
elif media < 6 and media >=2:
  print(f"Recuperação com nota {media}")
elif media < 2:
  print(f"Reprovado com nota {media}")
else:
    print("Está nota não existe") """

# Sintaxe
""" for numero in range(11, 0, -2):
    print(numero) """

""" primeiro_nome = 'Douglas'

for letra in primeiro_nome:
    print(letra) """

""" nomes = ['Douglas', 'Diego', "Maria", 'Jose']
for nome in nomes:
    print(nome) """

""" dicionario = {"chave 1": "Diego", "chave 2": "João","Chave 2": "Maria"}
""" 

""" for chave in dicionario:
    print(chave)

for chave in dicionario:
    print(dicionario[chave])
 
for chave in dicionario:
    print(chave, dicionario[chave]) """

# While 
""" x=0 """
""" while x <= 10:
    print(x)
    x += 1100 """

""" lista = ["banana", "maça", "uva", "limão"]
while x < len(lista):
    print(lista[x])
    x += 1 """

""" cod = 0
while True:
    cod = int(input('Número: '))
    if cod ==1:
        print(f"você digitou o número {cod}, vamos prosseguir")
    elif cod ==2:
        print(f"vc dgt o Nr {cod}, vamos prosseguir")
    elif cod ==3:
        print(f"vc dgt o Nr {cod}, vamos parar!")
        break  """
 
#Metodos
""" nome = "douglas"
print(nome.upper()) """

""" def imprime ():
    print("Hello world")

imprime() """

"""  def soma (x, y):
    return x+y

resultado = soma(2, 7)
print(resultado) 
 """
""" def mult (a, b):
    return a*b 

resultado = mult(2, 4)
print(resultado) """

""" def sub(c, d):
    res_soma = soma(c, d)
    res_multp = mult(c, d)
    return res_multp - res_soma """

""" resultado = sub(4, 5)
print(resultado) 
 """

