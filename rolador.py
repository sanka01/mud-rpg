from typing import Type

import Dado

import numpy as np

from Dado import Dado


def calculaEstatistica():
    dado: Type[Dado] = Dado.Dado
    dado.lados = 20
    dado.quantidadeRolagem = 10000000
    resultados = np.zeros(dado.lados)

    for i in range(dado.quantidadeRolagem):
        i = dado.rolar(dado)
        resultados[i - 1] = resultados[i - 1] + 1

    for i in range(dado.lados):
        print(str(i + 1), ": ", str(resultados[i] / 100000))


calculaEstatistica()
