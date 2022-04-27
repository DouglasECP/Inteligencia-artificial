f = "Fazendeiro"
r = "Rapoza"
g = "Galinha"
m = "Milho"


RioE = [f, r, g, m]
RioD = ["Vazio", "Vazio", "Vazio", "Vazio"]

while RioE == [f, r, g, m]:
    print(f"• Precisa levar  os {RioE} para o lado Direito do rio")
    print(f"• porem tem apenas 1 barco e no barco vai apenas o {f} e mais uma carga.")
    print(f"• Não pode deixar junto a {r} com a {g}, por que a {r} mata a {g}.")
    print(f"• Não pode deixar a {g} junto com o {m} por que a {g} come o {m}.")
    entrada = input(f"Quem vai sair primeiro ({f}, {f} e {r}, {f} e {g}, {f} e {m}? ")
    if entrada == f"{f}":
        RioE_entrada = RioE.pop(0)
        RioE.insert(0,f"Saida {f}")
        print(f"Esquerdo = {RioE}")
        RioD_entrada = RioD.pop(0)
        RioD.insert(0,f"Entrada {f}")
        print(f"Direito = {RioD}")
    elif entrada == f"{f} e {r}":
        RioE_entrada = RioE.pop(0)
        RioE_entrada = RioE.pop(1)
        RioE.insert(0,f"Saida {f}") ,RioE.insert(1,f"Saida {r}")
        print(f"Esquerdo = {RioE}")
        RioD_entrada = RioD.pop(0)
        RioD_entrada = RioD.pop(1)
        RioD.insert(0,f"Entrada {f}") ,RioD.insert(1,f"Entrada {r}")
        print(f"Direito = {RioD}")
        print(RioE)
    elif entrada == f"{f} e {g}":
        RioE_entrada = RioE.pop(2)
        RioE_entrada = RioE.pop(0)
        RioE.insert(0,f"Saida {f}") ,RioE.insert(2,f"Saida {g}")
        print(f"Esquerdo = {RioE}")
        RioD_entrada = RioD.pop(0)
        RioD_entrada = RioD.pop(2)
        RioD.insert(0,f"Entrada {f}") ,RioD.insert(2,f"Entrada {g}")
        print(f"Direito = {RioD}")
    elif entrada == f"{f} e {m}":
        RioE_entrada = RioE.pop(3)
        RioE_entrada = RioE.pop(0)
        RioE.insert(0,f"Sainda {f}") ,RioE.insert(3,f"Saida {m}")
        print(f"Esquerdo = {RioE}")
        RioD_entrada = RioD.pop(3)
        RioD_entrada = RioD.pop(0)
        RioD.insert(0,f"Entrada {f}") ,RioD.insert(3,f"Entrada {m}")
        print(f"Direito = {RioD}")

while RioD == [f"Entrada {f}","Vazio","Vazio","Vazio"]:
    print("PURO TESTE")