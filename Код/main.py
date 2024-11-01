import datetime
from classes.storage_locations import Rack, Shelf
from classes.warehouse import Warehouse
from classes.product import Product
from classes.operation import ShipmentOperation
from classes.user import Operator

ware = Warehouse(1,"123")

rack = Rack(1, "123")

ware.addStorageLocation(rack)
rack.addShelf(Shelf(1, "blabla"))

prod = Product(1, "TestProduct", "tomato")

oper = Operator(1, "testoper")

oper.startOperationReceipt().prepare(prod, ware).execute()

shipment = oper.startOperationShipment()
shipment.shipment.add_product(prod)
shipment.execute()

