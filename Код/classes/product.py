from classes.storage_locations import StorageLocation

class Product:
    def __init__(self, id: int, name: str, category: str, size: int):
        self.id = id
        self.name = name
        self.category = category
        self.size = size
        self.storageLocation: StorageLocation = None

    def __str__(self):
        return f"{self.id}: {self.name}"
