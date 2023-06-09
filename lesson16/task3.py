# Write a class Product that has three attributes:
#     type
#     name
#     price
#
# Then create a class ProductStore, which will have some Products and will operate with all products in the store.
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
#
# Also, the ProductStore class must have the following methods:
# Tips: Use aggregation/composition concepts while implementing the ProductStore class.
# You can also implement additional classes to operate on a certain type of product, etc.
#
# Also, the ProductStore class must have the following methods:
# add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)

# set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers
# (type or name). The discount must be specified in percentage

# sell_product(product_name, amount) - removes a particular amount of products from the store if available,
# in other case raises an error. It also increments income if the sell_product method succeeds.

# get_income() - returns amount of many earned by ProductStore instance.

# get_all_products() - returns information about all available products in the store.

# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    total = 0
    discount = 0.3

    def __init__(self):
        self.products = []

    def __str__(self):
        print(self.products[0].name, self.products[0].amount, self.products[0].price)
        print(self.products[1].name, self.products[1].amount, self.products[1].price)

    def add(self, product, amount):
        if amount < 0:
            raise ValueError("Invalid amount")
        if not self.products:
            product.amount = amount
            self.products.append(product)
        else:
            for i in self.products:
                if product.name == i.name:
                    i.amount += amount
            else:
                product.amount = amount
                self.products.append(product)

    def set_discount(self, identifier, percent, identifier_type='name'):
        arr = []
        for p in self.products:
            if getattr(p, identifier_type) == identifier:
                p.amount *= (100 - percent) / 100

    def sell_product(self, product_name, amount):
        for i in self.products:
            if i.name == product_name:
                if i.amount - amount < 0:
                    raise ValueError("Insufficient stock")
                i.amount -= amount
                ProductStore.total = i.price * amount
                break
        else:
            raise ValueError("Product not found")

    def get_income(self):
        return print(ProductStore.total)

    def get_all_products(self):
        for p in self.products:
            print(f'name:{p.name}, type:{p.type}, amount:{p.amount}, price:{p.price}')

    def get_product_info(self, product_name):
        for p in self.products:
            if p.name == product_name:
                return (p.name, p.amount)


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)

s.get_income()

s.get_all_products()

assert s.get_product_info('Ramen') == ('Ramen', 290)
