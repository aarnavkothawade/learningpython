grocery_prices = {
    "milk": 3.49,
    "eggs": 2.99,
    "coffee": 6.99,
    "bread": 1.99,
    "apples": 0.99,
    "banana": 0.50,
    "cheese": 5.44,
}

max = 0
for item in grocery_prices:
    if grocery_prices[item] > max:
        max = grocery_prices[item]

print(f"The maximum price is ${max:.2f}")