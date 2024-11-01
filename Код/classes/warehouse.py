from classes.storage_locations import StorageLocation

class Warehouse:
    def __init__(self, id: int, address: str):
        self.id = id
        self.address = address
        self.storageLocations: list[StorageLocation] = []
    
    def addStorageLocation(self, storageLocation: StorageLocation):
        self.storageLocations.append(storageLocation)

    def getAvailableStorageLocation(self) -> StorageLocation:
        for location in self.storageLocations:
            if not location.isFull():
                return location
        
        print(f"Не удалось получить доступные места расположения для склада {self.id}")
