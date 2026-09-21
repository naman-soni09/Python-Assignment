price = float(input("Enter item price: "))

if price >= 2000:
    discount = price * 20 / 100
    final_price = price - discount
else:
    final_price = price

print("Final price:", final_price)