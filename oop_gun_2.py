class Gun:
    def __init__(self):
        self.shoot_count = False

    def shoot(self):
        if not self.shoot_count:
            print('pif')
        else:
            print('paf')
        self.shoot_count = not self.shoot_count
