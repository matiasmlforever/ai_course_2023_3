# This is a sample Python script.
import datetime

from model.Agente import Agente
from model.Ambiente import Ambiente

MAX_AGENTES = 2;


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    humeldo = "HUMELDO"
    print_hi(humeldo)
    agentes = []

    # MAX_AGENTES agentes
    print("")
    for i in range(0, MAX_AGENTES):
        print(f'buena{humeldo}')
        agentes.append(Agente(id=1, name=f'Agente{i}'))

    print(agentes)

    ambiente = Ambiente(size=100, timestamp="22:32", agentes=agentes)
    ambiente.agentes = agentes

    print(ambiente)
    # ENTONCES LOS AGENTES ESTAN CONTENIDOS EN AMBIENTE
