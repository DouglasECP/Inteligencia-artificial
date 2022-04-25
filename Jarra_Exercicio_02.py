CapacidadeMaxJarro1 = 3
CapacidadeMaxJarro2 = 4
Jarro1 = 0
Jarro2 = 0

print(f"• Jarro 1 tem capacidade de {CapacidadeMaxJarro1}L, Jarro 2 tem capacidade de {CapacidadeMaxJarro2}L")
print(f"• Jarro 1 está com {Jarro1}L, Jarro 2 está com {Jarro2}L.")

while Jarro1 >= 0 and Jarro1 <3:
        Jarro1 += 1
        print(f"Enchendo Jarra 1, agora possui {Jarro1}L")
while Jarro2 >= 0 and Jarro2 <4:
        Jarro2 += 1
        print(f"Enchendo Jarra 2, agora possui {Jarro2}L")

print(f"• Objetivo: Jarro 2 com 2 litros de águal")

def esvaziarJarro1 (x):
      while x >= 3:
        x -= 1
        print(f"esvaziando Jarro 02 em -1L, jarro 2 = {x}")
        return x

def esvaziarJarro2 (y):
       while y >= 4:
        y -= 1
        print(f"esvaziando Jarro 02 em -1L, jarro 2 = {y}")
        return y

Jarro1 = esvaziarJarro1(Jarro1)
Jarro2 = esvaziarJarro2(Jarro2)

