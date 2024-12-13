import datetime
from classes.storage_locations import Cell, Rack, Shelf, StorageLocation
from classes.operation import Operation, ReceiptOperation, ShipmentOperation, OPERATION_ID
from typing import TYPE_CHECKING
from classes.product import Product

from classes.user import Operator


class Warehouse:
    def __init__(self, id: int, address: str):
        self.id = id
        self.address = address
        self.storageLocations: list[StorageLocation] = []

    def addStorageLocation(self, storageLocation: StorageLocation):
        self.storageLocations.append(storageLocation)

    def getAvailableStorageLocation(self, prod: "Product") -> StorageLocation:
        for location in self.storageLocations:
            if location.wouldFit(prod.size):
                return location

        print(f"Не удалось получить доступные места расположения для склада {self.id}")

    def startOperationReceipt(self, oper: "Operator", product) -> ReceiptOperation:
        global OPERATION_ID
        OPERATION_ID += 1
        return ReceiptOperation(OPERATION_ID, oper).prepare(product, self).execute()
    
    def getProductById(self, id):
        for loc in self.storageLocations:
            for prod in loc.getAllProducts():
                if prod.id == id:
                    return prod

    def startOperationShipment(self, oper: "Operator", productIds) -> ShipmentOperation:
        global OPERATION_ID
        OPERATION_ID += 1
        operation = ShipmentOperation(OPERATION_ID, oper)
        for _id in productIds:
            prod = self.getProductById(_id)
            if prod:
                operation.shipment.add_product(prod)
        
        operation.execute()

    def generateReport(self, startDate: datetime.datetime, endDate: datetime.datetime):
        return Operation.fetchOperations(startDate, endDate)

    def performOperation(self, operation: Operation, oper: "Operator"):
        operation.user = oper
        operation.execute()

    def addRack(self, description: str, size: int):
        rack = Rack(1, description, size)
        self.addStorageLocation(rack)
        return rack
    
    def addShelf(self, rack: Rack, description, size):
        shelf = Shelf(1, description, size)
        rack.addLocation(
            shelf
        )
        return shelf
    
    def addCell(self, shelf: Shelf, descripion, size):
        cell = Cell(1, descripion, size)
        shelf.addLocation(cell)

    def createOperator(self, name):
        return Operator(1, name)
    
    def createProduct(self, id, name, category, size):
        return Product(id, name, category, size)