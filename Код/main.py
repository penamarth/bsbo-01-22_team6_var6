import datetime
from classes.storage_locations import Cell, Rack, Shelf
from classes.warehouse import Warehouse
from classes.product import Product
from classes.operation import ShipmentOperation
from classes.user import Operator


prod = Product(1, "TestProduct", "tomato", 10)


ware = Warehouse(1, "blabla")

rack = Rack(1, "", 100)
shelf = Shelf(1,1, 10)
shelf.addCell(Cell(1,1,5))
oper = Operator(1, 'test')

rack.addShelf(shelf)
ware.addStorageLocation(rack)
print(*map(str, rack.getAllProducts()))
ware.startOperationReceipt(oper).prepare(prod, ware).execute()
shipment = ware.startOperationShipment(oper)
shipment.shipment.add_product(prod)
ware.performOperation(shipment, oper)
print()

