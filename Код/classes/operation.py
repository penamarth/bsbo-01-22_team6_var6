from datetime import datetime
from classes.shipment import Shipment

class Operation:
    def __init__(self, id: int, date: datetime, user):
        self.id = id
        self.date = date
        self.user = user
    
    def execute(self):
        raise NotImplementedError

class ShipmentOperation(Operation):
    def __init__(self, id, date, user):
        self.is_sent = False
        self.shipment = Shipment()
        super().__init__(id, date, user)

    def execute(self):
        if not self.is_sent:
            self.is_sent = True
            self.shipment.send()
            print(f"Успех отправки {self.id}")

    
    
        