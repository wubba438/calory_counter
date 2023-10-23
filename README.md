# calory counter 2023-9-10-11
This is my solution for the calory counter exercises

## Requirements

Python 3.10^

## Installation

Clone the repository :

```bash
git clone git@github.com:wubba438/calory_counter.git
cd calory_counter
```

Create and activate a virtual envirnment :

```bash
python3 -m venv .my_venv
source .my_venv/bin/activate
```
or

```bash
python -m venv .my_venv
source .my_venv/bin/activate
```
Install dependencies (inside virtual environment):

```bash
python -m pip install -r requirements.txt
```

### Files
MOst of the code is located in the `module` module. It contains:

- The main class `Order` in the orders.py file
- Functions to calculate the price and calories in the functions.py
- Custom Exceptions in the exceptions.py file
- Data about the menu,  in json format in the data directory and imported into python objects in the data.py file
- Tests in the tests directory

### The Order class

To create an order, you must import the `Order` class from module.orders and create an instance by passing it the ordered items ids :

```python
from module.orders import Order

order_1 = Order(["meal-1","combo-2"])
```

If the total calories count of the order is greater than 2000 calories, it will be refused. If an order contains an unknown item id, it will also be refused.

A refused order has its `order_accepted` attribute set to False, and the reason for the refusal is stored in the `order_refused_reason` attribute. 

### Data analysis

Example data has been provided in the calory_counter directory. There is also a data_analysis.ipynb file in the same directory for you to do some basic data analysis.

In case you encounter ModuleNotFoundError, try restart.

## Run tests

```bash
python -m unittest
```