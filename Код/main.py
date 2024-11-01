import datetime
from classes.storage_locations import Rack, Shelf
from classes.warehouse import Warehouse
from classes.product import Product
from classes.operation import ShipmentOperation
from classes.user import Operator


prod = Product(1, "TestProduct", "tomato")

oper = Operator(1, "testoper")

ware = oper.createWarehouse("blahblah street")

oper.createRack(ware, 2, 10)

oper.startOperationReceipt().prepare(prod, ware).execute()

shipment = oper.startOperationShipment()
shipment.shipment.add_product(prod)
oper.performOperation(shipment)

