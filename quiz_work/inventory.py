class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)

# 1.Great! Now override the add_item method.
# Use super() in it to make sure the item
# still gets added to the list.
# 2.Sorted inventories should be just that:
# sorted. Right now, we just add an item onto the
# slots list whenever our add_item method is called.
# Use the list.sort() method to make sure the slots
# list gets sorted after an item is added. Only do
# this in the SortedInventory class.
class SortedInventory(Inventory):
    def add_item(self, item): #copy this line from previous Method
        super().add_item(item)
        self.slots.sort()