from abc import ABC, abstractmethod
from typing import Dict

from shopping_cart_interface import IShoppingCart
from pricer import Pricer

# add elements to print_order_options array if other printing layouts are
# created.
print_order_options = ["key", "price"]
# change which element in the array order equals for different printing layouts.
order = print_order_options[0]

class ShoppingCart(IShoppingCart):
    """
    Implementation of the shopping tills in our supermarket.
    """
    def __init__(self, pricer: Pricer):
        self.pricer = pricer
        self._contents: Dict[str,int] = {}

    def add_item(self, item_type: str, number: int):
        # adds new item to or update existing item in the shopping cart
        if item_type not in self._contents:
            self._contents[item_type] = number
        else:
            self._contents[item_type] = self._contents[item_type] + number

    def print_receipt(self):
        # The below format can be duplicated and edited to support any other
        # printing layout that may be desried. (print total price per item,
        # different ordering of fields, etc.) Global array print_order_options
        # must be edited to include a keyword for the new layout.
        if order == "key":   # print key first
            total = 0
            for key, value in self._contents.items():
                price = self.pricer.get_price(key)
                print(f"{key} \t- {value} \t- {price}")
                total = total + (price * value)
            print(f"----------------------")    # added for readability for customer
            print(f"Total \t-\t- {total}")
        
        elif order == "price":   # print price first
            total = 0
            for key, value in self._contents.items():
                price = self.pricer.get_price(key)
                print(f"{price} \t- {value} \t- {key}")
                total = total + (price * value)
            print(f"----------------------")    # added for readability for customer
            print(f"{total} \t-\t- Total")


class ShoppingCartCreator(ABC):
    """
    Interface for the ShoppingCart creator.
    The creation process will be delegated to the subclasses of this class.
    """
    @abstractmethod
    def factory_method(self) -> ShoppingCart:
        # return the ShoppingCart object
        pass

    def operation(self) -> ShoppingCart:
        # Here more operations can be performed on the ShoppingCart object
        # returns ShoppingCart object
        return self.factory_method()

class ShoppingCartConcreteCreator(ShoppingCartCreator):
    """
    Concrete class for the ShoppingCart creator.
    Implements the factory_method
    """
    def factory_method(self) -> ShoppingCart:
        # returns ShoppingCart object
        return ShoppingCart(Pricer())
