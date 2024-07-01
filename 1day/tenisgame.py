# -*- coding: utf-8 -*-


class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def assert_error(self, result, ret):
        if ret != result:
            print(
                f"{self.p1points} : {self.p2points} 는 {result} 여야 합니다. 현재 결과는 {ret} 입니다"
            )
            print("FAIL")

    def won_player1_point(self):
        self.p1points += 1

    def won_player2_point(self):
        self.p2points += 1

    def insert_scores_for_two_players(self, p1Score, p2Score):
        for i in range(p1Score):
            self.won_player1_point()
        for i in range(p2Score):
            self.won_player2_point()

    def get_final_result(self):
        result = self.get_result_from_score()
        return result

    def get_result_from_score(self):
        result = ""
        if self.p1points == self.p2points:
            return self.classify_scores_in_drawcase()
        if self.p1points >= 4 or self.p2points >= 4:
            return self.classify_scores_over_endpoints()

        result = self.classify_scroes_under_endpoints()
        return result

    def classify_scroes_under_endpoints(self):
        result = ""
        tempScore = 0
        for i in range(1, 3):
            if i == 1:
                tempScore = self.p1points
            else:
                result += "-"
                tempScore = self.p2points
            result += {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
            }[tempScore]
        return result

    def classify_scores_over_endpoints(self):
        minusResult = self.p1points - self.p2points
        if minusResult == 1:
            result = "Advantage player1"
        elif minusResult == -1:
            result = "Advantage player2"
        elif minusResult >= 2:
            result = "Win for player1"
        else:
            result = "Win for player2"
        return result

    def classify_scores_in_drawcase(self):
        result = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.p1points, "Deuce")
        return result


if __name__ == "__main__":
    test_cases = [
        (0, 0, "Love-All", "player1", "player2"),
        (1, 1, "Fifteen-All", "player1", "player2"),
        (2, 2, "Thirty-All", "player1", "player2"),
        (3, 3, "Deuce", "player1", "player2"),
        (4, 4, "Deuce", "player1", "player2"),
        (1, 0, "Fifteen-Love", "player1", "player2"),
        (0, 1, "Love-Fifteen", "player1", "player2"),
        (2, 0, "Thirty-Love", "player1", "player2"),
        (0, 2, "Love-Thirty", "player1", "player2"),
        (3, 0, "Forty-Love", "player1", "player2"),
        (0, 3, "Love-Forty", "player1", "player2"),
        (4, 0, "Win for player1", "player1", "player2"),
        (0, 4, "Win for player2", "player1", "player2"),
        (2, 1, "Thirty-Fifteen", "player1", "player2"),
        (1, 2, "Fifteen-Thirty", "player1", "player2"),
        (3, 1, "Forty-Fifteen", "player1", "player2"),
        (1, 3, "Fifteen-Forty", "player1", "player2"),
        (4, 1, "Win for player1", "player1", "player2"),
        (1, 4, "Win for player2", "player1", "player2"),
        (3, 2, "Forty-Thirty", "player1", "player2"),
        (2, 3, "Thirty-Forty", "player1", "player2"),
        (4, 2, "Win for player1", "player1", "player2"),
        (2, 4, "Win for player2", "player1", "player2"),
        (4, 3, "Advantage player1", "player1", "player2"),
        (3, 4, "Advantage player2", "player1", "player2"),
        (5, 4, "Advantage player1", "player1", "player2"),
        (4, 5, "Advantage player2", "player1", "player2"),
        (15, 14, "Advantage player1", "player1", "player2"),
        (14, 15, "Advantage player2", "player1", "player2"),
        (6, 4, "Win for player1", "player1", "player2"),
        (4, 6, "Win for player2", "player1", "player2"),
        (16, 14, "Win for player1", "player1", "player2"),
        (14, 16, "Win for player2", "player1", "player2"),
    ]

    for p1Score, p2Score, result, name1, name2 in test_cases:
        game = TennisGame1(name1, name2)
        game.insert_scores_for_two_players(p1Score, p2Score)
        ret = game.get_final_result()

        game.assert_error(result, ret)
