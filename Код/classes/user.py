import datetime
from classes.operation import OPERATION_ID, Operation, ShipmentOperation, ReceiptOperation
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
    
    def createWarehouse(self, address: str) -> Warehouse:
        return Warehouse(1, address)
    
    def createRack(self, warehouse: Warehouse, shelfCount: int, cellCount: int):
        rack = Rack(1, "")
        for _ in range(shelfCount):
            shelf = Shelf(1, "")
            rack.addShelf(shelf)
            for _ in range(cellCount):
                cell = Cell(1, "")
                shelf.addCell(cell)

        warehouse.addStorageLocation(rack)


class Manager(User):
    def __init__(self, id, name):
        super().__init__(id, name)
    
    def generateReport(self, startDate:datetime.datetime, endDate:datetime.datetime):
        Operation.fetchOperation(startDate, endDate)
        


