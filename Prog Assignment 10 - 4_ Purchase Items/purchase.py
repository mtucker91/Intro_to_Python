class ItemToPurchase:
    pass
    # FIXME 1: Complete the __init__ method
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # FIXME 2: Complete print_item method. no return in this method
    def print_item_cost(self):
        self.total = self.price * self.quantity
        print(f'{self.name} {self.quantity} @ ${self.price} = ${self.total}')

if __name__ == "__main__":
    # FIXME main a: Prompt the user for two items and create two objects of the ItemToPurchase class
    item = ['','']
    comb_total = 0.00
    for i in range(2):
        print(f'Item {i + 1}')
        name = str(input('Enter the item name:\n'))
        price = float(input('Enter the item price:\n'))
        quantity = int(input('Enter the item quantity:\n'))
        item[i] = ItemToPurchase(name, price, quantity)
        comb_total = comb_total + (price * quantity)
        print('')
    
    # FIXME main b: Add the costs of the two items together and output the total cost.
    print('TOTAL COST')
    for i in range(len(item)):
        item[i].print_item_cost()
    
    print('')
    print(f'Total: ${comb_total}')