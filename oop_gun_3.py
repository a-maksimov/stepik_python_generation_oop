class Gun:
    def __init__(self):
        self.shots_counter = 0

    def shots_reset(self):
        self.shots_counter = 0

    def shoot(self):
        if self.shots_counter % 2 == 0:
            print('pif')
        else:
            print('paf')
        self.shots_counter += 1

    def shots_count(self):
        return self.shots_counter
