
from typing import Iterable, List
from classes.product import Product

class StorageLocation:
    def __init__(self, id:int, description: str):
        self.id = id
        self.description = description
        self.product = None

    def isFull(self) -> bool:
        return True
    
    def addProduct(self, product: Product):
        raise NotImplementedError
    
    def removeProduct(self, product: Product):
        raise NotImplementedError
    
    def getAllProducts(self) -> List[Product]:
        return self.product

class Rack(StorageLocation):
    def __init__(self, id:int, description: str):
        super().__init__(id, description)
        self.shelves = []

    def isFull(self):
        for shelf in self.shelves:
            if not shelf.isFull():
                return False
        
        return (self.product or self.shelves)
    
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

class Shelf(StorageLocation):
    def __init__(self, id:int, description: str):
        super().__init__(id, description)
        self.cells = []

    def isFull(self):
        for cell in self.cells:
            if not cell.isFull():
                return False
        return (self.product or self.cells)
    
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

        
        
        
        

class Cell(StorageLocation):
    def __init__(self, id:int, description: str):
        super().__init__(id, description)
        
    
    def isFull(self):
        return not self.product
    
    def addProduct(self, product):
        if not self.isFull():
            print(f"Продукт {product.name}({(product.id)}) размещен в ячейке {self.id}")
            self.product = product
        
        print(f"Не удалось разместить продукт {product.name}({(product.id)}) в ячейке {self.id}")
            
    
