from classes.warehouse import Warehouse


ware = Warehouse(1, "blabla")
prod = ware.createProduct(1, "TestProduct", "tomato", 10)

rack = ware.addRack("", 100)
shelf = ware.addShelf(rack,1, 10)
ware.addCell(shelf,1,5)
oper = ware.createOperator(1, 'test')

ware.addStorageLocation(rack)
print(*map(str, rack.getAllProducts()))
ware.startOperationReceipt(oper).prepare(prod, ware).execute()
shipment = ware.startOperationShipment(oper)
shipment.shipment.add_product(prod)
ware.performOperation(shipment, oper)
print()

