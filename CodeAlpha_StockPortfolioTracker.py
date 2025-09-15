# Hardcoded stock prices
stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 2800, "MSFT": 320}

portfolio = {}
total_value = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks:", stock_prices)

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("⚠ Invalid stock symbol! Try again.")
        continue
    qty = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty
    total_value += stock_prices[stock] * qty

print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares worth ${stock_prices[stock] * qty}")

print("💰 Total Investment Value:", total_value)

# Save to file
with open("portfolio.txt", "w") as f:
    f.write("Stock Portfolio Summary\n")
    for stock, qty in portfolio.items():
        f.write(f"{stock}: {qty} shares worth ${stock_prices[stock] * qty}\n")
    f.write(f"\nTotal Investment Value: ${total_value}\n")

print("✅ Portfolio saved to portfolio.txt")
