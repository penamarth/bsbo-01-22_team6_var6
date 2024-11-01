from classes.operation import OPERATION_ID, Operation, ShipmentOperation, ReceiptOperation
from classes.product import Product
from classes.shipment import Shipment


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

   
    
    def perform_operation(self, operation: Operation):
        operation.user = self
        operation.execute()


class Operator(User):
    def __init__(self, id, name):
        super().__init__(id, name)

    def startOperationReceipt(self) -> ReceiptOperation:
        global OPERATION_ID
        OPERATION_ID+=1
        return ReceiptOperation(OPERATION_ID, self)
        
    def startOperationShipment(self) -> ShipmentOperation:
        global OPERATION_ID
        OPERATION_ID+=1
        return ShipmentOperation(OPERATION_ID, self)
    

class Manager(User):
    def __init__(self, id, name):
        super().__init__(id, name)
    
    def generateReport():
        pass
        


