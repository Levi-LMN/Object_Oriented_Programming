def calculate_price(item_prices, combo_discount, gift_discount):
    # Create a dictionary to store item prices
    items = {
        "Item 1": item_prices[0],
        "Item 2": item_prices[1],
        "Item 3": item_prices[2]
    }
    
    # Calculate combo prices
    combo_prices = {
        "Combo 1(Item 1 + 2)": items["Item 1"] + items["Item 2"],
        "Combo 2(Item 2 + 3)": items["Item 2"] + items["Item 3"],
        "Combo 3(Item 1 + 3)": items["Item 1"] + items["Item 3"],
        "Combo 4(Item 1 + 2 + 3)": sum(item_prices)
    }
    
    # Calculate discounted prices for combos and gift pack
    discounted_prices = {}
    for combo, price in combo_prices.items():
        discounted_prices[combo] = price * (1 - combo_discount)
    
    gift_pack_price = sum(item_prices) * (1 - gift_discount)
    
    # Print the catalog
    print("Online Store")
    print("Product(S) Price")
    
    for item, price in items.items():
        print(f"{item} {price:.1f}")
    
    for combo, price in discounted_prices.items():
        print(f"{combo} {price:.1f}")
    
    print(f"Gift Pack (Item 1 + Item 2 + Item 3) {gift_pack_price:.1f}")
    print("For delivery Contact: 98764678899")

# Define the prices for individual items
item_prices = [200.8, 400.8, 600.0]

# Define discount percentages
combo_discount = 0.10  # 10% discount for combo packs
gift_discount = 0.25  # 25% discount for gift pack

# Call the function with the given inputs
calculate_price(item_prices, combo_discount, gift_discount)
