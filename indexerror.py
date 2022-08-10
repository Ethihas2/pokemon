list_items = ["apple","mango","tomato"]

try:
    print(list_items[5])
except IndexError:
    print("list index is out of range")