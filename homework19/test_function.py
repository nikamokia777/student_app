import pytest
from homework19.function import process_orders
def test_product_not_found():
     orders = [
        {"product": "banana", "quantity": 2}
    ]

     inventory = {
        "apple": 10
    }
     with pytest.raises(ValueError):
          process_orders(orders, inventory)

def test_not_enough_stock():
    orders = [
         {'product': 'banana', 'quantity': 2}
         ]
    inventory = {
         'banana': 1
                 }
    with pytest.raises(ValueError):
         process_orders(orders, inventory)

def test_calculation():
      orders = [
         {'product': 'banana', 'quantity': 2}
         ]
      inventory = {
         'banana': 5
                 }
      result = process_orders(orders, inventory)
      assert result == orders
      assert inventory['banana'] == 3
      
     
     
