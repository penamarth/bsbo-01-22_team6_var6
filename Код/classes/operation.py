from datetime import datetime
from typing import TYPE_CHECKING
from classes.shipment import Shipment
OPERATION_ID = 0

if TYPE_CHECKING:
    from classes.warehouse import Warehouse
    from classes.product import Product

class Operation:
    def __init__(self, id: int, user):
        self.id = id
        self.date = datetime.now()
        self.user = user
    
    def execute(self):
        raise NotImplementedError

class ShipmentOperation(Operation):
    def __init__(self, id, user):
        self.is_sent = False
        self.shipment = Shipment()
        super().__init__(id, user)

    def execute(self):
        if not self.is_sent:
            self.is_sent = True
            self.shipment.send()
            print(f"Успех отправки {self.id}")

class ReceiptOperation(Operation):
    def __init__(self, id, user):
        super().__init__(id, user)
        self.warehouse: Warehouse = None
        self.product = None
        self.prepared = False
    
    def execute(self):
        if not self.prepared:
            print("Ошибка операции прибытия: невозможно выполнить пустую операцию")
            return 
        avail = self.warehouse.getAvailableStorageLocation()
        if not avail:
            print("Ошибка операции прибытия: склад переполнен")
            return
        avail.addProduct(self.product)

    def prepare(self, product: "Product", warehouse: "Warehouse") -> "ReceiptOperation":
        self.product = product
        self.warehouse = warehouse
        self.prepared = True
        return self

    
        