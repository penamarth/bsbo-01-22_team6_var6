class StorageLocation:
    def __init__(self, id:int, description: str, warehouse: "Warehouse", products: Iterable[Product]):
        self.id = id
        self.description = description
        self.warehouse = warehouse
        self.products = products

class Rack(StorageLocation):
    def __init__(self, id, description, warehouse, products):
        super().__init__(id, description, warehouse, products)

class Shelf(StorageLocation):
    def __init__(self, id, description, warehouse, products, rack: Rack):
        super().__init__(id, description, warehouse, products)
        self.rack = rack

class Cell(StorageLocation):
    def __init__(self, id, description, warehouse, products, shelf: Shelf):
        super().__init__(id, description, warehouse, products)
        self.shelf = shelf