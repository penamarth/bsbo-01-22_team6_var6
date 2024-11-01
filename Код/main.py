from classes.storage_locations import Rack, Shelf
from classes.warehouse import Warehouse
from classes.product import Product

ware = Warehouse(1,"123")

rack = Rack(1, "123")

ware.addStorageLocation(rack)
rack.addShelf(Shelf(1, "blabla"))

prod = Product(1, "TestProduct", "tomato")

avail = ware.getAvailableStorageLocation()

avail.addProduct(prod)

avail = ware.getAvailableStorageLocation()
