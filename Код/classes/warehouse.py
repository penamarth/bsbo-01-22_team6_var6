from typing import Iterable
from classes.storage_locations import StorageLocation

class Warehouse:
    def __init__(self, id: int, address: str, totalCapacity: int, storageLocations: Iterable[StorageLocation]):
        self.id = id
        self.address = address
        self.totalCapacity = totalCapacity
        self.storageLocations = storageLocations
