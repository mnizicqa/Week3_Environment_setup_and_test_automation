import json

# The DictObject is a utility class to access dictionary values using object notation
class DictObject(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)

    @classmethod
    def from_dict(cls, d):
        return json.loads(json.dumps(d), object_hook=DictObject)

#From here we will feed data into our test
USERS = DictObject.from_dict({
    'user_credentials': {
        'first_name': 'Mario',
        'last_name': 'Nizic',
        'date_of_birth': '1990-09-13',
        'street': 'Ive Andrica 1',
        'postal_code': '71000',
        'city': 'Sarajevo',
        'state': 'Kanton Sarajevo',
        'country': 'BA',
        'phone': '061905161',
        'email': 'marion02@msn.com',
        'password': 'Qatester17!',
        'payment_method': 'credit-card',
        'credit_card_number': '0000-0000-0000-0000',
        'expiration_date': '12/2028',
        'cvv': '123',
        'card_holder_name': 'Mario'
    }
})