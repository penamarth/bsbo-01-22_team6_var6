from datetime import datetime, timedelta
from classes.warehouse import Warehouse
from classes.operation import OPERATIONS

ware = Warehouse(1, "blabla")
prod = ware.createProduct(1, "TestProduct", "tomato", 10)

rack = ware.addRack("", 100)
shelf = ware.addShelf(rack,1, 10)
ware.addCell(shelf,1,5)
oper = ware.createOperator('test')

ware.addStorageLocation(rack)
print(*map(str, rack.getAllProducts()))


ware.startOperationReceipt(oper, prod)

ware.startOperationShipment(oper, (1,))


print(list(map(str, ware.generateReport(datetime(2000,1,1),datetime.now()+timedelta(12)))))


