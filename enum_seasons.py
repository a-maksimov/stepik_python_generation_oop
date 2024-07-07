from enum import Enum

translations = {
            "WINTER": {"en": "winter", "ru": "зима"},
            "SPRING": {"en": "spring", "ru": "весна"},
            "SUMMER": {"en": "summer", "ru": "лето"},
            "FALL": {"en": "fall", "ru": "осень"}
        }


class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, code):
        return translations[self.name][code]


print(Seasons.FALL.text_value('ru'))
print(Seasons.FALL.text_value('en'))
