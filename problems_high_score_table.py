class HighScoreTable:
    def __init__(self, max_records):
        self._max_records = max_records
        self._scores = []

    @property
    def scores(self):
        return sorted(self._scores, reverse=True)

    def update(self, score):
        if len(self._scores) < self._max_records:
            self._scores.append(score)
        else:
            worst_score = self.scores[-1]
            if score > worst_score:
                self._scores.remove(worst_score)
                self._scores.append(score)

    def reset(self):
        self._scores.clear()


# TEST_3:
high_score_table = HighScoreTable(3)

print(high_score_table.scores)
high_score_table.update(10)
high_score_table.update(8)
high_score_table.update(12)
print(high_score_table.scores)

high_score_table.update(18)
high_score_table.update(11)
high_score_table.update(13)
print(high_score_table.scores)

# TEST_3:
# []
# [12, 10, 8]
# [18, 13, 12]
