import datetime
from classes.operation import (
    OPERATION_ID,
    Operation,
    ShipmentOperation,
    ReceiptOperation,
)
from classes.product import Product
from classes.shipment import Shipment
from classes.warehouse import Warehouse
from classes.storage_locations import Cell, Rack, Shelf


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
