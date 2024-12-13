import datetime


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Operator(User):
    def __init__(self, id, name):
        super().__init__(id, name)


class Manager(User):
    def __init__(self, id, name):
        super().__init__(id, name)
