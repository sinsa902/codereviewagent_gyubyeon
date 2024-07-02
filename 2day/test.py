class GameMachine:
    def __init__(self) -> None:
        self._totalCoin = 0

    def inputCoin(self, input_coin):
        if input_coin > 5:
            print("코인 5개 초과입니다. 불가능")
            return

        if self.__getTotalCoins() > 10:
            print("토탈 코인 10개 초과입니다. 불가능")
            return
        self._totalCoin += input_coin

    def playGame(self):
        if self.__getTotalCoins() < 1:
            print("토탈코인 0개 이하입니다. 예외처리")
            return
        self._totalCoin -= 1

    def _getTotalCoins(self):
        return self._totalCoin


game1 = GameMachine()
game1._
