from classes.storage_locations import StorageLocation
from classes.operation import Operation, ReceiptOperation, ShipmentOperation, OPERATION_ID
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from classes.user import Operator



class Warehouse:
    def __init__(self, id: int, address: str):
        self.id = id
        self.address = address
        self.storageLocations: list[StorageLocation] = []
    
    def addStorageLocation(self, storageLocation: StorageLocation):
        self.storageLocations.append(storageLocation)

    def getAvailableStorageLocation(self) -> StorageLocation:
        for location in self.storageLocations:
            if not location.isFull():
                return location
        
        print(f"Не удалось получить доступные места расположения для склада {self.id}")

    def startOperationReceipt(self, oper: "Operator") -> ReceiptOperation:
        global OPERATION_ID
        OPERATION_ID+=1
        return ReceiptOperation(OPERATION_ID, oper)
        
    def startOperationShipment(self, oper: "Operator") -> ShipmentOperation:
        global OPERATION_ID
        OPERATION_ID+=1
        return ShipmentOperation(OPERATION_ID, oper)
    
    
    def performOperation(self, operation: Operation, oper: "Operator"):
        operation.user = oper
        operation.execute()
