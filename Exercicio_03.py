f = "Fazendeiro"
r = "Rapoza"
g = "Galinha"
m = "Milho"
conte = 0

RioE = [f, r, g, m]
RioD = ["Vazio", "Vazio", "Vazio", "Vazio"]

while RioE != [f"Sainda {f},"f"Sainda {r}",f"Sainda {g}",f"Sainda {m}"]:
    if conte == 0:
        print(f" Precisa levar  o {RioE} para o lado Direito do rio")
        print(f" porem tem apenas 1 barco e no barco vai apenas o {f} e mais uma carga.")
        print(f" Não pode deixar junto a {r} com a {g}, por que a {r} mata a {g}.")
        print(f" Não pode deixar a {g} junto com o {m} por que a {g} come o {m}.")
        conte = 1
        entrada = input(f"• Quem vai sair primeiro? {f}, {f} e {r}, {f} e {g}, {f} e {m}? ")

    if RioE == [f"Saida {f}",f"Saida {r}",f"Saida {g}",f"Saida {m}"]:
        print("• Você atravessou com todos para o lado Esquerdo do Rio!!!")
        break

    if entrada == f"{f}":
        RioE_entrada = RioE.pop(0)
        RioE.insert(0,f"Saida {f}")
        print(f"Esquerdo = {RioE}")
        RioD_entrada = RioD.pop(0)
        RioD.insert(0,f"Entrada {f}")
        print(f"Direito = {RioD}")
        
    elif entrada == f"{f} e {r}":
        RioE_entrada = RioE.pop(1)
        RioE_entrada = RioE.pop(0)
        RioE.insert(0,f"Saida {f}") ,RioE.insert(1,f"Saida {r}")
        print(f"Esquerdo = {RioE}")
        RioD_entrada = RioD.pop(1)
        RioD_entrada = RioD.pop(0)
        RioD.insert(0,f"Entrada {f}") ,RioD.insert(1,f"Entrada {r}")
        print(f"Direito = {RioD}")

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
        RioE.insert(0,f"Saida {f}") ,RioE.insert(3,f"Saida {m}")
        print(f"Esquerdo = {RioE}")
        RioD_entrada = RioD.pop(3)
        RioD_entrada = RioD.pop(0)
        RioD.insert(0,f"Entrada {f}") ,RioD.insert(3,f"Entrada {m}")
        print(f"Direito = {RioD}")

    entrada = 0

    if RioE == [f"Saida {f}",r,g,f"Saida {m}"]:
        print(f"• A {r} matou a {g}, RECOMECE!• • •")
        RioE = [f, r, g, m]
        conte = 0

    elif RioE == [f"Saida {f}",f"Saida {r}",g,m]:
        print(f"• A {g} comeu o {m}, RECOMECE!• • •")
        RioE = [f, r, g, m]
        conte = 0
    
    elif RioE == [f"Saida {f}",r,g,m]:
        print(f"• A {g} comeu o {m} e a {r} comeu a {g}, RECOMECE!• • •")
        RioE = [f, r, g, m]
        conte = 0


    if RioE == [f"Saida {f}",r,f"Saida {g}",m]:
        RioD = [f"Saida {f}","Vazio,",g,"Vazio"]
        print(f"{f} Retornando ao lado Esquerdo")
    if RioD == [f"Saida {f}","Vazio,",g,"Vazio"]:
        RioE == [f"Saida {f}", f"Saida {r}","Vazio",m]
        print(f"Retornando ao Lado direito com {f} e {r}")
    if RioE == [f"Saida {f}", f"Saida {r}","Vazio",m]:
        RioD = [f"Saida {f}",r,f"Saindo {g}","Vazio"]
        print(f"Retornando ao lado Direito com {f} e {g}")
    if RioD == [f"Saida {f}",r,f"Saindo {g}","Vazio"]:
        RioE = [f"Saida {f}","Vazio",g,f"Saida {m}"]
        print(f"Retornando ao lado Direito com {f} e {m}")     
    if RioE == [f"Saida {f}","Vazio",g,f"Saida {m}"]:
        RioD = [f"Saida {f}",r,"Vazio",m]
        print(f"{f} Retornando ao lado Esquerdo")
    if RioD == [f"Saida {f}",r,"Vazio",m]:
        RioE = [f"Saida {f}","Vazio",f"Saida {g}","Vazio"]
        print(f"{f} Retornando ao lado Esquerdo: {RioD}")
        RioE = [f"Sainda {f},"f"Sainda {r}",f"Sainda {g}",f"Sainda {m}"]

