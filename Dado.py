import random as r


class Dado:
    resultado = 0
    quantidadeRolagem = 1
    lados = 20

    def __init__(self) -> None:
        super().__init__()

    def dF(self, bonuses=0):
        r.seed()
        dadoFudge = (-1, 0, +1)
        D = 0

        for x in range(4):
            D = D + r.choice(dadoFudge)

        return D + bonuses

    def rolar(self, bonuses: int = 0) -> int:
        """

        :rtype: int
        """
        r.seed()
        self.resultado = r.choice(range(self.lados)) + 1 + bonuses
        return self.resultado
