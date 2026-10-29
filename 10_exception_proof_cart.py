item_prices = []

while True:
    try:
        item_price = input("Enter item price (Q to quit): ")
        if item_price.upper() == "Q":
            break
        item_price = float(item_price)
        if item_price < 0:
            print("Invalid price!")
        else:
            item_prices.append(item_price)
            print("Item added!")
            print("Entry processed.")
    except ValueError:
        print("Invalid price!")

print(f"\nItems purchased: {len(item_prices)}")
print(f"Total: ${sum(item_prices):.2f}")