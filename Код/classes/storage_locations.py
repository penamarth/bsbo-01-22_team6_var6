
from typing import Iterable, List, TYPE_CHECKING

if TYPE_CHECKING:
    from classes.product import Product

class StorageLocation:
    def __init__(self, id:int, description: str):
        self.id = id
        self.description = description
        self.product = None

    def isFull(self) -> bool:
        return True
    
    def addProduct(self, product: "Product"):
        raise NotImplementedError
    
    def removeProduct(self, product: "Product"):
        raise NotImplementedError
    
    def getAllProducts(self) -> List["Product"]:
        return self.product

class Rack(StorageLocation):
    def __init__(self, id:int, description: str):
        super().__init__(id, description)
        self.shelves: list["Shelf"] = []

    def isFull(self):
        for shelf in self.shelves:
            if not shelf.isFull():
                return False
        
        return (bool(self.product) or bool(self.shelves))
    
    def addShelf(self, shelf: "Shelf"):
        if not self.product:
            self.shelves.append(shelf)
            return
        
        print(f"Не удалось добавить полку; шкаф {self.id} уже занят")

    def addProduct(self, product):
        for shelf in self.shelves:
            if not shelf.isFull():
                shelf.addProduct(product)
                return
        
        if not self.isFull():
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

class Shelf(StorageLocation):
    def __init__(self, id:int, description: str):
        super().__init__(id, description)
        self.cells: list["Cell"] = []

    def isFull(self):
        for cell in self.cells:
            if not cell.isFull():
                return False
        return (bool(self.product) or bool(self.cells))
    
    def addCell(self, cell: "Cell"):
        if not self.product:
            self.cells.append(cell)
            return
        
        print(f"Не удалось добавить ячейку; полка {self.id} уже занята")
    
    def addProduct(self, product):
        for cell in self.cells:
            if not cell.isFull():
                cell.addProduct(product)
                return
        if not self.isFull():
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
        
        
        

class Cell(StorageLocation):
    def __init__(self, id:int, description: str):
        super().__init__(id, description)
        
    
    def isFull(self):
        return self.product
    
    def addProduct(self, product):
        if not self.isFull():
            print(f"Продукт {product.name}({(product.id)}) размещен в ячейке {self.id}")
            self.product = product
        

        print(f"Не удалось разместить продукт {product.name}({(product.id)}) в ячейке {self.id}")
            
    
    def removeProduct(self, product):
        if self.product == product:
            self.product = None
            return True
        
        print(f"Не удалось удалить продукт {product.name} из ячейки {self.id}")

        return False