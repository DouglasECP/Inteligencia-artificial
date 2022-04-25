Salas=(0,1,2)
situacao=((0,'sujo'),(1,'Limpo'))
global roboPos
roboPos=0
SituaSalas=([0,0],[1,0],[2,0])
caminho=((0,1),(1,0),(1,2),(2,1))
cont=0

def procSala(pos):
    roboPos=pos
    for i in range(len(caminho)):
            if caminho[i][0]==roboPos:
                if SituaSalas[caminho[i][1]][1]==0:
                    roboPos=caminho[i][1]
                    break
    i=0
    return roboPos


while SituaSalas[0][1]==0 or SituaSalas[1][1]==0 or SituaSalas[2][1]==0 or cont<10:
    print("Sala ",Salas[roboPos]+1," está ",situacao[SituaSalas[roboPos][1]][1])
    if SituaSalas[roboPos][1]==0:
        print("Limpando sala ",Salas[roboPos]+1," ...")
        SituaSalas[roboPos][1]=1
        if SituaSalas[roboPos][1]==1:
            print("Sala ",Salas[roboPos]+1," Limpa")
        else:
            print("Sala ",Salas[roboPos]+1," não pode ser limpa!")
        roboPos=procSala(roboPos)
        cont+=1
    elif SituaSalas[0][1]==1 and SituaSalas[1][1]==1 and SituaSalas[2][1]==1:
        break
    else:
        print("Robo entrou na sala errada, sala ",Salas[roboPos]+1," já está limpa!")
        roboPos=procSala(roboPos)
        if SituaSalas[roboPos][1]==1:
            print("Robo ficou sem salas para ir")
            break
print("Situação das salas:")
print(" Sala 1: ",situacao[SituaSalas[0][1]][1])
print(" Sala 2: ",situacao[SituaSalas[1][1]][1])
print(" Sala 3: ",situacao[SituaSalas[2][1]][1])
print(" Bateria restante: ",10-cont)