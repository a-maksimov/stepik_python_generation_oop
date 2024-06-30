from functools import singledispatchmethod


class IPAddress:
    def __init__(self, ipaddress):
        self.ipaddress = self.format(ipaddress)

    @singledispatchmethod
    def format(self, ipaddress):
        ipaddress = map(str, ipaddress)
        return '.'.join(ipaddress)

    @format.register(str)
    def format_str(self, ipaddress):
        return ipaddress

    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"

    def __str__(self):
        return self.ipaddress
