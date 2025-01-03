from collections import Counter



inventory = Counter(apple=50, mango=100, orange=70)

def update_inventory(ordered):
    inventory.subtract(ordered)

order = Counter(apple=10, banana=12, orange=5)
update_inventory(order)

print(inventory)

