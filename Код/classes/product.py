from classes.storage_locations import StorageLocation

class Product:
    def __init__(self, id: int, name: str, category: str):
        self.id = id
        self.name = name
        self.category = category
        self.storageLocation: StorageLocation = None
