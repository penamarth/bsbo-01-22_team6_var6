from classes.product import Product

class Product:
    def __init__(self, id: int, name: str, category: str, storageLocation: "StorageLocation"):
        self.id = id
        self.name = name
        self.category = category
        self.storageLocation = storageLocation
