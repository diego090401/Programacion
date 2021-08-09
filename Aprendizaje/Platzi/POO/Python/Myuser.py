from Account import Account

class Myuser (Account):
    preference = str
    pollito  = str
    def __init__(self, id, Status):
        super().__init__(id, Status)
