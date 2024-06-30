class Postman:
    def __init__(self):
        self._delivery_data = []

    @property
    def delivery_data(self):
        return self._delivery_data

    def add_delivery(self, *address):
        self._delivery_data.append(address)

    def get_houses_for_street(self, street):
        houses = []
        for address in self._delivery_data:
            if address[0] == street:
                if address[1] not in houses:
                    houses.append(address[1])
        return houses

    def get_flats_for_house(self, street, house):
        flats = []
        for address in self._delivery_data:
            if address[0] == street and address[1] == house:
                if address[2] not in flats:
                    flats.append(address[2])
        return flats


