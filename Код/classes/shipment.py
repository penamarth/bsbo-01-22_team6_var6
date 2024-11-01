
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classes.product import Product

class Shipment:
    def __init__(self):
        self.shipmentNumber: int = 1
        self.products: list["Product"] = []

    def add_product(self, product: "Product"):
        self.products.append(product)
    
    def send(self):
        for product in self.products:
            if product.storageLocation:
                product.storageLocation.removeProduct(product)
                print(f"Продукт {product.name}({product.id}) выбыл с расположения {product.storageLocation.id}")

        
