from Account import Account

class driver(Account):
    car = str
    phonenumber = int
    def __init__(self, id, Status):
        super().__init__(id, Status)