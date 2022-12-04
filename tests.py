import unittest

from shopping_cart import ShoppingCartConcreteCreator
from test_utils import Capturing

# add elements to test_options array if other printing layouts  and tests for 
# them are created.
test_options = ["key", "price"]
# change which element in the array order equals for testing different printing
# layouts.
testing = test_options[0]
class ShoppingCartTest(unittest.TestCase):
    
    def test_print_receipt(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        with Capturing() as output:
            sc.print_receipt()
        if testing == "key":
            self.assertEqual("apple \t- 2 \t- 100", output[0])
            self.assertEqual("Total \t-\t- 200", output[2])
        elif testing == "price":
            self.assertEqual("100 \t- 2 \t- apple", output[0])
            self.assertEqual("200 \t-\t- Total", output[2])

    def test_doesnt_explode_on_mystery_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        sc.add_item("banana", 5)
        sc.add_item("pear", 5)
        with Capturing() as output:
            sc.print_receipt()
        if testing == "key":
            self.assertEqual("apple \t- 2 \t- 100", output[0])
            self.assertEqual("banana \t- 5 \t- 200", output[1])
            self.assertEqual("pear \t- 5 \t- 0", output[2])
            self.assertEqual("Total \t-\t- 1200", output[4])
        elif testing == "price":
            self.assertEqual("100 \t- 2 \t- apple", output[0])
            self.assertEqual("200 \t- 5 \t- banana", output[1])
            self.assertEqual("0 \t- 5 \t- pear", output[2])
            self.assertEqual("1200 \t-\t- Total", output[4])
        
    def test_prints_in_order_of_scan(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("banana", 5)
        sc.add_item("apple", 2)
        sc.add_item("pear", 5)
        with Capturing() as output:
            sc.print_receipt()
        if testing == "key":
            self.assertEqual("banana \t- 5 \t- 200", output[0])
            self.assertEqual("apple \t- 2 \t- 100", output[1])
            self.assertEqual("pear \t- 5 \t- 0", output[2])
            self.assertEqual("Total \t-\t- 1200", output[4])
        elif testing == "price":
            self.assertEqual("200 \t- 5 \t- banana", output[0])
            self.assertEqual("100 \t- 2 \t- apple", output[1])
            self.assertEqual("0 \t- 5 \t- pear", output[2])
            self.assertEqual("1200 \t-\t- Total", output[4])
  
    def test_mixed_order_scan(self):
        # tests if system system adds number of items if scanned between
        # different items and if it prints in order of when the first iterstion
        # of an item was scanned.
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("banana", 1)
        sc.add_item("apple", 2)
        sc.add_item("pear", 4)
        sc.add_item("banana", 2)
        sc.add_item("pear", 2)
        with Capturing() as output:
            sc.print_receipt()
        if testing == "key":
            self.assertEqual("banana \t- 3 \t- 200", output[0])
            self.assertEqual("apple \t- 2 \t- 100", output[1])
            self.assertEqual("pear \t- 6 \t- 0", output[2])
            self.assertEqual("Total \t-\t- 800", output[4])
        elif testing == "price":  
            self.assertEqual("200 \t- 3 \t- banana", output[0])
            self.assertEqual("100 \t- 2 \t- apple", output[1])
            self.assertEqual("0 \t- 6 \t- pear", output[2])
            self.assertEqual("800 \t-\t- Total", output[4])

unittest.main(exit=False)
