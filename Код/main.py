import datetime
from classes.storage_locations import Rack, Shelf
from classes.warehouse import Warehouse
from classes.product import Product
from classes.operation import ShipmentOperation

ware = Warehouse(1,"123")

rack = Rack(1, "123")

ware.addStorageLocation(rack)
rack.addShelf(Shelf(1, "blabla"))

prod = Product(1, "TestProduct", "tomato")

avail = ware.getAvailableStorageLocation()

avail.addProduct(prod)

avail = ware.getAvailableStorageLocation()


shpop = ShipmentOperation(1, datetime.datetime.now(), 123)
shpop.shipment.add_product(prod)
shpop.execute()

