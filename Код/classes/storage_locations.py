
from typing import Iterable, List, TYPE_CHECKING

if TYPE_CHECKING:
    from classes.product import Product


class Composite:
    def __init__(self):
        self.locations = []
    
    def addLocation(self,loc: "StorageLocation"):
        self.locations.append(loc)

    def removeLocation(self, loc: "StorageLocation"):
        self.locations.remove(loc)

    def getLocations(self):
        return self.locations

class StorageLocation:
    def __init__(self, id:int, description: str, size: int):
        self.id = id
        self.description = description
        self.size = size
        self.product = None

    def getFreeSize(self) -> int:
        raise NotImplementedError
    
    def isFull(self) -> bool:
        return True

    def wouldFit(self, size) -> bool:
        return False
    
    def addProduct(self, product: "Product"):
        raise NotImplementedError
    
    def removeProduct(self, product: "Product"):
        raise NotImplementedError
    
    def getAllProducts(self) -> List["Product"]:
        return self.product

class Rack(StorageLocation, Composite):
    def __init__(self, id:int, description: str, size:int):
        super().__init__(id, description, size)
        self.shelves: list["Shelf"] = []

    def getFreeSize(self):
        allocated = sum(shelf.size for shelf in self.shelves)
        if self.product:
            prod = self.product.size
        else:
            prod = 0
        return self.size - allocated - prod

    def wouldFit(self,size):
        for shelf in self.shelves:
            if shelf.wouldFit(size):
                return True
        
        return (not self.product) and (self.getFreeSize() > size)
    
    def addLocation(self, shelf: "Shelf"):
        if not self.product:
            self.shelves.append(shelf)
            return
        
        print(f"Не удалось добавить полку; шкаф {self.id} уже занят")
    

    def addProduct(self, product):
        for shelf in self.shelves:
            if shelf.wouldFit(product.size):
                shelf.addProduct(product)
                return
        
        if self.wouldFit(product.size):
            self.product = product
            product.storageLocation = self
            print(f"Продукт {product.name}({(product.id)}) размещен в шкафу {self.id}")
            return
        
        print(f"Не удалось разместить продукт {product.name}({(product.id)}) в шкафу {self.id}")


    def removeProduct(self, product):
        if self.product == product:
            self.product = None
            return True
        
        for shelf in self.shelves:
            if shelf.removeProduct(product):
                return True
        
        print(f"Не удалось удалить продукт {product.name} из шкафа {self.id}")
        return False
    

    def getAllProducts(self):
        res = []
        for shelf in self.shelves:
            res.extend(shelf.getAllProducts())
        if self.product:
            res.append(self.product)
        return res

class Shelf(StorageLocation, Composite):
    def __init__(self, id:int, description: str, size:int):
        super().__init__(id, description, size)
        self.cells: list["Cell"] = []
    
    def getFreeSize(self):
        allocated = sum(cell.size for cell in self.cells)
        if self.product:
            prod = self.product.size
        else:
            prod = 0

        return self.size - allocated - prod
    
    def wouldFit(self, size):
        for cell in self.cells:
            if cell.wouldFit(size):
                return True
        
        return (not self.product) and (self.getFreeSize() > size)
    
    def addLocation(self, cell: "Cell"):
        if not self.product:
            self.cells.append(cell)
            return
        
        print(f"Не удалось добавить ячейку; полка {self.id} уже занята")
    
    def addProduct(self, product):
        for cell in self.cells:
            if cell.wouldFit(product.size):
                cell.addProduct(product)
                return
        if self.wouldFit(product.size):
            self.product = product
            product.storageLocation = self
            print(f"Продукт {product.name}({(product.id)}) размещен на полке {self.id}")
            return
        
        print(f"Не удалось разместить {product.name}({(product.id)}) на полке {self.id}")

    def removeProduct(self, product):
        if self.product == product:
            self.product = None
            return True
        
        for cell in self.cells:
            if cell.removeProduct():
                return True

        print(f"Не удалось удалить продукт {product.name} из полки {self.id}")
        return False
        
        
    def getAllProducts(self):
        res = []
        for cell in self.cells:
            res.extend(cell.getAllProducts())
        
        if self.product:
            res.append(self.product)

        return res

class Cell(StorageLocation):
    def __init__(self, id:int, description: str, size:int):
        super().__init__(id, description, size)
        
    
    def getFreeSize(self):
        return self.size if not self.product else 0
    
    def wouldFit(self, size) -> bool:
        return (not self.product) and (self.size > size)
    
    def addProduct(self, product):
        if self.wouldFit(product.size):
            print(f"Продукт {product.name}({(product.id)}) размещен в ячейке {self.id}")
            self.product = product
            return
        

        print(f"Не удалось разместить продукт {product.name}({(product.id)}) в ячейке {self.id}")
            
    
    def removeProduct(self, product):
        if self.product == product:
            self.product = None
            return True
        
        print(f"Не удалось удалить продукт {product.name} из ячейки {self.id}")

        return False
    
    def getAllProducts(self):
        return [self.product] if self.product else []
    
