import re

domain_pattern = r'^[a-z]+\.[a-z]+$'
url_pattern = r'^https*://'
email_pattern = r'^[a-z]+@'


class DomainException(Exception):
    pass


class Domain:
    def __init__(self, domain):
        self.domain = domain

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        if not self._validate_domain(value):
            raise DomainException('Недопустимый домен, url или email')
        self._domain = value

    @staticmethod
    def _validate_domain(value):
        return re.search(domain_pattern, value)

    @classmethod
    def from_url(cls, url):
        match = re.search(url_pattern, url)
        if not match:
            raise DomainException('Недопустимый домен, url или email')
        domain = url.split(match.group(0))[1]
        domain_obj = cls(domain)
        domain_obj.domain = domain
        return domain_obj

    @classmethod
    def from_email(cls, email):
        match = re.search(email_pattern, email)
        if not match:
            raise DomainException('Недопустимый домен, url или email')
        domain = email.split(match.group(0))[1]
        domain_obj = cls(domain)
        domain_obj.domain = domain
        return domain_obj

    def __str__(self):
        return self._domain


# TEST_8:
emails = ['anan,i86@example.org', 'konovalovkondrat@@example.net', 'efimmaksimov@example..net', 'marfa_.04@example.com',
          'vlasovstanimir@example.org.', '.anikita_04@example.net', '@loginovroman@example.org', 'abc@@mail.ru',
          'novikovasinklitikija@example.net@', 'elizar_1978@example@.com', 'kasjan_1972@example.org', '@a.ru', 'abc@.ru']

for email in emails:
    try:
        domain = Domain.from_email(email)
        print(domain)
    except DomainException as e:
        print(e)

# TEST_8:
# Недопустимый домен, url или email
# Недопустимый домен, url или email
# Недопустимый домен, url или email
# Недопустимый домен, url или email
# Недопустимый домен, url или email
# Недопустимый домен, url или email
# Недопустимый домен, url или email
# Недопустимый домен, url или email
# Недопустимый домен, url или email
# Недопустимый домен, url или email
# Недопустимый домен, url или email
# Недопустимый домен, url или email
# Недопустимый домен, url или email
