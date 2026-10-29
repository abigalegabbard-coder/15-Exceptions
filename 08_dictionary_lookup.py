try:
    prices = {"pizza": 12, "burger": 8, "fries": 4, "soda": 2}
    user_select = input("Enter a food: ")
    print(prices[user_select])
except KeyError:
    print("Sorry, that item is not on the menu.")